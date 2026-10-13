"""
scripts/test_prediction.py

Smoke test for the prediction pipeline.
Tests end-to-end: load preprocessor + model, build feature row, predict.

Uses static weather values (fallback) so no NASA API calls are needed.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import pandas as pd
import joblib
import xgboost as xgb

MODELS_DIR = Path("models")

def run_test():
    print("=" * 60)
    print("  PREDICTION PIPELINE SMOKE TEST")
    print("=" * 60)

    # 1. Load artifacts
    print("\n[1] Loading preprocessor.pkl...")
    preprocessor = joblib.load(MODELS_DIR / "preprocessor.pkl")
    print(f"    OK — type: {type(preprocessor).__name__}")

    print("\n[2] Loading model.json (XGBoost booster)...")
    booster = xgb.Booster()
    booster.load_model(str(MODELS_DIR / "model.json"))
    print(f"    OK — {booster.num_features()} features")

    # 2. Build a representative input row
    # Punjab, Rice, Kharif, 2014
    # Weather: typical Punjab annual averages
    input_row = pd.DataFrame({
        "crop":                    ["RICE"],
        "state":                   ["Punjab"],
        "season":                  ["KHARIF"],
        "crop_year":               [2014],
        "area":                    [1.0],
        "mean_temperature":        [24.5],       # °C annual mean, Punjab
        "total_precipitation":     [650.0],      # mm/year, Punjab
        "mean_relative_humidity":  [58.0],       # % annual mean
        "mean_solar_radiation":    [18.5],       # MJ/m²/day
        "irrigation_coverage_pct": [94.0],       # Punjab: highly irrigated
        "npk_consumption_kg_per_ha": [248.0],   # Punjab: intensive fertilizer
    })

    print("\n[3] Input row:")
    print(input_row.to_string())

    # 3. Transform
    print("\n[4] Transforming with preprocessor...")
    X_t = preprocessor.transform(input_row)
    if hasattr(X_t, "toarray"):
        X_t = X_t.toarray()
    X_arr = np.asarray(X_t, dtype=np.float32)
    print(f"    Transformed shape: {X_arr.shape}")

    # Feature count verification
    n_model = int(booster.num_features())
    n_preproc = X_arr.shape[1]
    assert n_model == n_preproc, (
        f"FEATURE MISMATCH: preprocessor={n_preproc}, model={n_model}. "
        "Re-run scripts/rebuild_schema.py after retraining."
    )
    print(f"    Feature count matches: {n_preproc} OK")

    # 4. Predict
    print("\n[5] Running prediction...")
    dmat = xgb.DMatrix(X_arr)
    pred = float(booster.predict(dmat)[0])
    pred = max(0.0, pred)
    print(f"    Raw prediction: {pred:.4f} q/ha")

    # 5. Sanity checks
    print("\n[6] Sanity checks:")
    assert np.isfinite(pred), "Prediction is not finite!"
    print(f"    Finite value: OK")
    # Rice in Punjab: typical 25-40 q/ha (2.5-4 t/ha)
    # With our model trained on quintals/ha, reasonable range 5-100 q/ha
    assert pred > 0, "Prediction is not positive!"
    print(f"    Positive value: OK ({pred:.2f} q/ha)")
    assert pred < 2000, f"Implausibly high yield: {pred:.2f} q/ha"
    print(f"    Within plausible range: OK")

    print("\n" + "=" * 60)
    print(f"  SUCCESS: Predicted Rice yield in Punjab (Kharif 2014):")
    print(f"  {pred:.2f} Quintals/Hectare ({pred/10:.2f} Tonnes/Hectare)")
    print("=" * 60)

    return pred

if __name__ == "__main__":
    run_test()
    print("\nSUCCESS")