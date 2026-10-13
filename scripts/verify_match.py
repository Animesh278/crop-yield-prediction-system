"""scripts/verify_match.py — verify model and preprocessor feature counts match."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

MODELS_DIR = Path("models")

# Load preprocessor
pp = joblib.load(str(MODELS_DIR / "preprocessor.pkl"))

# Transform a single representative row (not empty!)
sample_row = pd.DataFrame({
    "crop":                    ["RICE"],
    "state":                   ["Punjab"],
    "season":                  ["KHARIF"],
    "crop_year":               [2014],
    "area":                    [1.0],
    "mean_temperature":        [24.5],
    "total_precipitation":     [650.0],
    "mean_relative_humidity":  [58.0],
    "mean_solar_radiation":    [18.5],
    "irrigation_coverage_pct": [94.0],
    "npk_consumption_kg_per_ha": [248.0],
})

pp_features = pp.transform(sample_row)
if hasattr(pp_features, "toarray"):
    pp_features = pp_features.toarray()
n_preprocessor = pp_features.shape[1]

# Load model
booster = xgb.Booster()
booster.load_model(str(MODELS_DIR / "model.json"))
n_model = int(booster.num_features())

# Load schema
with open(MODELS_DIR / "feature_schema.json") as f:
    schema = json.load(f)
n_schema = schema["n_output_features"]

print(f"Preprocessor outputs: {n_preprocessor} features")
print(f"Model expects:        {n_model} features")
print(f"Schema says:          {n_schema} features")

if n_preprocessor == n_model == n_schema:
    print("\nALL MATCH -- ready to deploy!")
else:
    print("\nMISMATCH DETECTED -- do not deploy!")
    sys.exit(1)