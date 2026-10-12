
"""
Data ingestion: load crop production data, derive yield,
validate columns, and create train/test datasets.
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
        """Load, clean, derive yield, and split the dataset."""

        logging.info("Started data ingestion")

        try:
            if not os.path.isfile(DATA_PATH):
                raise FileNotFoundError(
                    f"Dataset not found: {DATA_PATH}"
                )

            df = pd.read_csv(DATA_PATH)

            if df.empty:
                raise ValueError("The input dataset is empty.")

            logging.info(
                "Loaded %d rows and %d columns",
                len(df), len(df.columns)
            )

            # Normalize column names
            df.columns = [
                str(col).strip().lower().replace(" ", "_")
                for col in df.columns
            ]

            # Validate required columns
            required = {"crop", "area", "production"}
            missing = required - set(df.columns)

            if missing:
                raise ValueError(
                    f"Missing columns: {sorted(missing)}. "
                    f"Available columns: {df.columns.tolist()}"
                )

            # Convert values to numeric
            df["area"] = pd.to_numeric(
                df["area"], errors="coerce"
            )
            df["production"] = pd.to_numeric(
                df["production"], errors="coerce"
            )

            # Remove invalid records
            df.dropna(
                subset=["crop", "area", "production"],
                inplace=True
            )

            df["crop"] = df["crop"].astype(str).str.strip()

            df = df[
                (df["crop"] != "")
                & (df["area"] > 0)
                & (df["production"] >= 0)
            ].copy()

            if df.empty:
                raise ValueError(
                    "No valid rows remain after cleaning."
                )

            # Assumption: production is in tonnes and area
            # is in hectares. Result is quintals per hectare.
            df["yield"] = (
                df["production"] / df["area"]
            ) * 10

            df.replace(
                [np.inf, -np.inf], np.nan, inplace=True
            )
            df.dropna(subset=["yield"], inplace=True)

            if df.empty:
                raise ValueError(
                    "No valid yield values could be calculated."
                )

            # Prepare output directory
            os.makedirs(
                os.path.dirname(self.config.train_data_path),
                exist_ok=True
            )

            # Save cleaned data
            df.to_csv(
                self.config.raw_data_path, index=False
            )

            # Split data. If a crop has only one row,
            # stratification is impossible, so use a random split.
            crop_counts = df["crop"].value_counts()
            rare_crops = crop_counts[crop_counts < 2]

            if not rare_crops.empty:
                logging.warning(
                    "Rare crops found; using random split: %s",
                    rare_crops.to_dict()
                )

                train_set, test_set = train_test_split(
                    df,
                    test_size=0.2,
                    random_state=42,
                    shuffle=True
                )
            else:
                train_set, test_set = train_test_split(
                    df,
                    test_size=0.2,
                    random_state=42,
                    stratify=df["crop"]
                )

            # Save train and test data
            train_set.to_csv(
                self.config.train_data_path, index=False
            )
            test_set.to_csv(
                self.config.test_data_path, index=False
            )

            logging.info(
                "Split complete: train=%d, test=%d",
                len(train_set), len(test_set)
            )

            print("\nData ingestion completed successfully.")
            print(f"Total rows: {len(df):,}")
            print(f"Training rows: {len(train_set):,}")
            print(f"Testing rows: {len(test_set):,}")
            print(f"Number of crops: {df['crop'].nunique()}")
            print(
                "Yield summary:\n",
                df["yield"].describe().to_string()
            )

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            logging.exception("Data ingestion failed")
            raise CustomException(e, sys) from e
