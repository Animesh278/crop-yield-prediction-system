"""
scripts/rebuild_schema.py

Rebuild feature_schema.json from the EXISTING preprocessor.pkl
(from train_pipeline). Does NOT refit the preprocessor.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
import numpy as np
import pandas as pd

from src.components.fertilizer_data import (
    FERTILIZER_FEATURE,
    enrich_dataframe_with_fertilizer,
)
from src.components.irrigation_data import (
    IRRIGATION_FEATURE,
    enrich_dataframe_with_irrigation,
)
from src.components.weather_data import (
    WEATHER_FEATURES,
    enrich_dataframe_with_weather,
)

MODELS_DIR = Path("models")
DATA_RAW_DIR = Path("data") / "raw"
SCHEMA_PATH = MODELS_DIR / "feature_schema.json"


def clean_columns(df):
    cleaned = []
    for col in df.columns:
        new_col = re.sub(r"[^a-z0-9]+", "_", col.strip().lower()).strip("_")
        cleaned.append(new_col)
    df.columns = cleaned
    yc = [c for c in df.columns if "yield" in c]
    if yc and yc[0] != "yield":
        df.rename(columns={yc[0]: "yield"}, inplace=True)
    for exc in ["production", "district"]:
        if exc in df.columns:
            df.drop(columns=[exc], inplace=True)
    return df


def main():
    pp_path = MODELS_DIR / "preprocessor.pkl"
    if not pp_path.exists():
        print("ERROR: preprocessor.pkl not found. Run train_pipeline first.")
        sys.exit(1)

    # Load existing preprocessor (DO NOT refit)
    preprocessor = joblib.load(str(pp_path))
    print(f"Loaded preprocessor.pkl from train_pipeline")

    # Determine feature columns from the preprocessor
    cat_cols = []
    num_cols = []
    for name, transformer, columns in preprocessor.transformers_:
        if name == "cat":
            cat_cols = list(columns)
        elif name == "num":
            num_cols = list(columns)
    feature_columns = cat_cols + num_cols
    print(f"Feature columns ({len(feature_columns)}): {feature_columns}")

    # Get output feature names from the FITTED preprocessor
    try:
        output_names = list(preprocessor.get_feature_names_out())
    except Exception:
        # Fallback for older sklearn
        output_names = []
        for name, transformer, columns in preprocessor.transformers_:
            if hasattr(transformer, "get_feature_names_out"):
                try:
                    out = list(transformer.get_feature_names_out(columns))
                    output_names.extend(out)
                except Exception:
                    output_names.extend(list(columns))
            else:
                output_names.extend(list(columns))

    print(f"Output features: {len(output_names)}")

    # Load dataset for unique values
    csv_path = DATA_RAW_DIR / "crop_production_india.csv"
    if not csv_path.exists():
        print(f"WARNING: {csv_path} not found — schema will lack dropdown values")
        unique = {}
        stats_area = {}
    else:
        df = pd.read_csv(csv_path)
        df = clean_columns(df)

        # Handle original column naming (State_Name -> state, District_Name -> district)
        if "state_name" in df.columns and "state" not in df.columns:
            df.rename(columns={"state_name": "state"}, inplace=True)
        if "district_name" in df.columns and "district" not in df.columns:
            df.rename(columns={"district_name": "district"}, inplace=True)

        # Normalize crop/state/season to uppercase
        for col in ["crop", "state", "season"]:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
                if col in ("crop", "season"):
                    df[col] = df[col].str.upper()

        # Enrich for stats (irrigation and fertilizer only — weather takes too long)
        if IRRIGATION_FEATURE not in df.columns:
            try:
                df = enrich_dataframe_with_irrigation(df, state_col="state")
            except Exception:
                df[IRRIGATION_FEATURE] = np.nan
        if FERTILIZER_FEATURE not in df.columns:
            try:
                df = enrich_dataframe_with_fertilizer(df, state_col="state")
            except Exception:
                df[FERTILIZER_FEATURE] = np.nan

        unique = {}
        for col in ["crop", "state", "season"]:
            if col in df.columns:
                unique[f"unique_{col}"] = sorted(
                    df[col].dropna().unique().tolist()
                )
        if "crop_year" in df.columns:
            unique["unique_crop_year"] = sorted(
                [int(x) for x in df["crop_year"].dropna().unique().tolist()]
            )

        stats_area = {}
        if "area" in df.columns:
            a = df["area"].dropna()
            stats_area = {
                "min": round(float(a.min()), 1),
                "max": round(float(a.max()), 1),
                "mean": round(float(a.mean()), 1),
                "median": round(float(a.median()), 1),
                "std": round(float(a.std()), 1),
            }

    # Read actual training sample count from metadata if available
    metadata_path = MODELS_DIR / "model_metadata.json"
    n_training_samples = 0
    if metadata_path.exists():
        try:
            with open(metadata_path) as f:
                meta = json.load(f)
            n_training_samples = meta.get("training_data", {}).get("n_train", 0)
        except Exception:
            pass

    schema = {
        "feature_columns": feature_columns,
        "categorical_columns": cat_cols,
        "numerical_columns": num_cols,
        "target_column": "yield",
        "target_unit": "Quintals/Hectare",
        "yield_calculation": "yield = (Production_tonnes / Area_hectares) * 10",
        "output_feature_names": output_names,
        "n_output_features": len(output_names),
        "crop_column": "crop" if "crop" in feature_columns else None,
        "state_column": "state" if "state" in feature_columns else None,
        "stats_area": stats_area,
        "n_training_samples": n_training_samples,
        **unique,
    }

    with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2, default=str)

    print(f"\nSaved: {SCHEMA_PATH}")
    print(f"Output features: {len(output_names)}")
    print(f"Crops: {len(unique.get('unique_crop', []))}")
    print(f"States: {len(unique.get('unique_state', []))}")
    print(f"Seasons: {len(unique.get('unique_season', []))}")
    print("\nDONE — schema matches preprocessor from train_pipeline")


if __name__ == "__main__":
    main()