
"""
Data ingestion: load crop production data, derive yield,
validate columns, and create train/test datasets.

Dataset: crop_production_india.csv
  State_Name, District_Name, Crop_Year, Season, Crop, Area, Production
  Area: hectares
  Production: tonnes (except Coconut which is in numbers)
  Yield = (Production / Area) * 10  => Quintals per Hectare
  (1 tonne = 10 quintals)

Coconut is measured in 000s of nuts per some Indian datasets, but in this
dataset the unit appears to be consistent (tonnes). However many coconut
records show unrealistic yield (>500 q/ha) likely due to data entry errors.

Outlier removal strategy (per-crop agronomic upper bounds):
  - Values above per-crop cap are physically implausible and are removed.
  - Caps are derived from documented agronomic maxima for India.
  - We report every removal so the user can audit.
"""

import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception.exception import CustomException
from src.logging.logger import logging


DATA_PATH = os.path.join(
    "data", "raw", "crop_production_india.csv"
)

# ---------------------------------------------------------------------------
#  Agronomic yield caps (Quintals/Hectare).
#  Source: FAO, ICAR crop production statistics for India.
#  Any record above the crop-specific cap is treated as a data error.
# ---------------------------------------------------------------------------
_CROP_YIELD_CAPS = {
    "SUGARCANE":       2000,   # ~200 t/ha absolute max; normal 50-80 t/ha
    "COCONUT":          500,   # coconut max ~50 t/ha copra-equivalent
    "BANANA":           600,   # banana max ~60 t/ha
    "POTATO":           500,   # potato max ~50 t/ha
    "ONION":            500,   # onion max ~50 t/ha
    "TAPIOCA":          500,
    "PAPAYA":           400,
    "SWEET POTATO":     400,
    "CABBAGE":          400,
    "TOMATO":           500,
}
_DEFAULT_YIELD_CAP = 500   # conservative cap for all other crops


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(
        "data", "processed", "train.csv"
    )
    test_data_path: str = os.path.join(
        "data", "processed", "test.csv"
    )
    raw_data_path: str = os.path.join(
        "data", "processed", "crop_production_india.csv"
    )


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """Load, clean, derive yield, remove outliers, and split the dataset."""

        logging.info("Started data ingestion")

        try:
            if not os.path.isfile(DATA_PATH):
                raise FileNotFoundError(
                    f"Dataset not found: {DATA_PATH}"
                )

            df = pd.read_csv(DATA_PATH)

            if df.empty:
                raise ValueError("The input dataset is empty.")

            n_raw = len(df)
            logging.info(
                "Loaded %d rows and %d columns",
                n_raw, len(df.columns)
            )

            # -----------------------------------------------------------------
            # Step 1: Normalize column names
            # -----------------------------------------------------------------
            df.columns = [
                str(col).strip().lower().replace(" ", "_")
                for col in df.columns
            ]

            # Rename expected columns
            rename_map = {}
            if "state_name" in df.columns and "state" not in df.columns:
                rename_map["state_name"] = "state"
            if "district_name" in df.columns and "district" not in df.columns:
                rename_map["district_name"] = "district"
            if rename_map:
                df.rename(columns=rename_map, inplace=True)
                logging.info("Renamed columns: %s", rename_map)

            # -----------------------------------------------------------------
            # Step 2: Validate required columns
            # -----------------------------------------------------------------
            required = {"crop", "area", "production", "state", "crop_year", "season"}
            missing = required - set(df.columns)
            if missing:
                raise ValueError(
                    f"Missing columns after renaming: {sorted(missing)}. "
                    f"Available: {df.columns.tolist()}"
                )

            # -----------------------------------------------------------------
            # Step 3: Normalize string columns
            # -----------------------------------------------------------------
            df["crop"] = df["crop"].astype(str).str.strip().str.upper()
            df["state"] = df["state"].astype(str).str.strip()
            # Season: normalize to UPPERCASE (dataset has title-case: 'Kharif')
            df["season"] = df["season"].astype(str).str.strip().str.upper()

            # -----------------------------------------------------------------
            # Step 4: Convert numeric columns
            # -----------------------------------------------------------------
            df["area"] = pd.to_numeric(df["area"], errors="coerce")
            df["production"] = pd.to_numeric(df["production"], errors="coerce")
            df["crop_year"] = pd.to_numeric(df["crop_year"], errors="coerce")

            # -----------------------------------------------------------------
            # Step 5: Remove invalid records
            # -----------------------------------------------------------------
            n_before = len(df)

            # Drop rows with missing required values
            df.dropna(subset=["crop", "state", "season", "crop_year", "area"], inplace=True)

            # Drop rows where production is NaN (cannot compute yield)
            n_missing_prod = df["production"].isna().sum()
            df.dropna(subset=["production"], inplace=True)
            logging.info("Removed %d rows with missing production", n_missing_prod)

            # Remove invalid area/production values
            df = df[
                (df["crop"] != "")
                & (df["area"] > 0)
                & (df["production"] >= 0)
            ].copy()

            n_after_basic = len(df)
            logging.info(
                "Basic cleaning: %d -> %d rows (removed %d)",
                n_before, n_after_basic, n_before - n_after_basic
            )

            # -----------------------------------------------------------------
            # Step 6: Derive yield
            # Unit: (tonnes / hectares) * 10 = Quintals/Hectare
            # 1 tonne = 10 quintals
            # -----------------------------------------------------------------
            df["yield"] = (df["production"] / df["area"]) * 10

            # Remove infinite / NaN yields (e.g., area=0 edge cases)
            df.replace([np.inf, -np.inf], np.nan, inplace=True)
            df.dropna(subset=["yield"], inplace=True)

            # -----------------------------------------------------------------
            # Step 7: Remove yield outliers (per-crop agronomic caps)
            # -----------------------------------------------------------------
            n_before_cap = len(df)
            removed_per_crop = {}

            for crop, cap in _CROP_YIELD_CAPS.items():
                bad = (df["crop"] == crop) & (df["yield"] > cap)
                n_bad = bad.sum()
                if n_bad > 0:
                    removed_per_crop[crop] = {
                        "cap_qha": cap, "removed": int(n_bad)
                    }
                    df = df[~bad]

            # Apply default cap to all remaining crops
            bad_default = df["yield"] > _DEFAULT_YIELD_CAP
            n_default_bad = bad_default.sum()
            if n_default_bad > 0:
                removed_per_crop["_other_crops"] = {
                    "cap_qha": _DEFAULT_YIELD_CAP,
                    "removed": int(n_default_bad)
                }
                df = df[~bad_default]

            n_after_cap = len(df)
            total_removed_outliers = n_before_cap - n_after_cap

            logging.info(
                "Outlier removal: %d rows removed (%.2f%% of data). Per-crop: %s",
                total_removed_outliers,
                100 * total_removed_outliers / max(n_before_cap, 1),
                removed_per_crop
            )

            if df.empty:
                raise ValueError(
                    "No valid rows remain after outlier removal. "
                    "Review yield cap thresholds."
                )

            # -----------------------------------------------------------------
            # Step 8: Prepare output directory
            # -----------------------------------------------------------------
            os.makedirs(
                os.path.dirname(self.config.train_data_path),
                exist_ok=True
            )

            # Save cleaned data (preserves original raw CSV)
            df.to_csv(self.config.raw_data_path, index=False)

            # -----------------------------------------------------------------
            # Step 9: Train/test split (random, reproducible)
            # -----------------------------------------------------------------
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42,
                shuffle=True
            )

            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)

            logging.info(
                "Split complete: train=%d, test=%d",
                len(train_set), len(test_set)
            )

            print("\n" + "=" * 60)
            print("  DATA INGESTION COMPLETED")
            print("=" * 60)
            print(f"Raw rows loaded    : {n_raw:,}")
            print(f"After basic filter : {n_after_basic:,}")
            print(f"After outlier cap  : {n_after_cap:,}")
            print(f"Outliers removed   : {total_removed_outliers:,} ({100*total_removed_outliers/max(n_raw,1):.1f}%)")
            print(f"Training rows      : {len(train_set):,}")
            print(f"Testing rows       : {len(test_set):,}")
            print(f"Unique crops       : {df['crop'].nunique()}")
            print(f"Unique states      : {df['state'].nunique()}")
            print(f"Unique seasons     : {sorted(df['season'].unique())}")
            print(f"\nYield stats (Quintals/Hectare):")
            print(df["yield"].describe().round(2).to_string())
            print(f"\nOutliers removed per crop:")
            for crop, info in removed_per_crop.items():
                print(f"  {crop}: {info['removed']} rows (cap={info['cap_qha']} q/ha)")

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            logging.exception("Data ingestion failed")
            raise CustomException(e, sys) from e
