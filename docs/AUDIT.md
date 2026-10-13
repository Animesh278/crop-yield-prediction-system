# System Audit & Gap Analysis

**Date:** 2026-10-12  
**Auditor:** Senior ML Engineer & Full-Stack Python Developer  
**Status:** Audit Complete (Phase 0)  
**Spec Document:** `README.md` (v3.2.0)

---

## 1. Executive Summary

A comprehensive audit of the repository (`Crop-Yield-Prediction-System-main`) was conducted against `README.md` (the system spec) and runtime behavior. 
While core components for data handling, XGBoost modeling, FastAPI serving, and Streamlit visualization exist, critical structural gaps, data leakage/filtering bugs, broken standalone scripts, and severe UI styling defects prevent the system from meeting the production specification.

---

## 2. File Tree Audit vs. README Spec

| README Spec File / Directory | Actual Repository Status | Severity / Impact |
| :--- | :--- | :--- |
| `Dockerfile` | **Missing** | High (Container deployment fails) |
| `docker-compose.yml` | **Missing** | High (Cannot launch API + Dashboard simultaneously) |
| `.streamlit/config.toml` | **Missing** | High (Causes white header defect & default red theme) |
| `.env.example` | **Missing** | Medium (Environment configuration undocumented) |
| `requirements-dev.txt` | **Missing** | Medium (Developer dependencies unpinned) |
| `run.ps1` / `run.sh` / `Makefile` | **Missing** | Medium (Cross-platform CLI runners absent) |
| `tests/` directory | **Missing** | High (Zero automated pytest coverage) |
| `data/reference/` | **Missing** (Data in `data/raw/`) | Medium (Reference lookup tables unversioned) |
| `scripts/prepare_new_dataset.py` | **Missing** | Critical (Required in Quick Start for 15-crop 50K prep) |
| `scripts/compute_metrics.py` | **Broken** (Fails on `'state'`) | Critical (Cannot evaluate held-out test metrics) |
| `scripts/build_preprocessor.py` | **Broken** (Fails on `'state_name'`) | High (Cannot rebuild preprocessor from raw data) |
| `scripts/warm_weather_cache.py` | **Broken** (KeyError `'state'`) | High (Crashes when preloading NASA weather cache) |
| `docs/AUDIT.md` | Created in Phase 0 | Completed |
| `docs/CHANGELOG.md` | Pending Phase 1-8 | Will document all changes |

---

## 3. Entrypoint Execution Audit

Each project entry point was executed and audited in the active Python 3.11 virtual environment:

### 3.1 `python scripts/prepare_new_dataset.py`
- **Result:** `FileNotFoundError` (Script missing from repository).
- **Impact:** Quick Start Step 2 cannot be executed. Raw Kaggle CSV is not cleaned, stratified to 50K rows, or filtered to the 15 crops.

### 3.2 `python scripts/build_preprocessor.py`
- **Result:** Loads `data/raw/crop_production_india.csv`, prints:
  `WARNING: No 'state' column — skipping enrichment`.
- **Root Cause:** Column casing in raw data is `State_Name`, which `build_preprocessor.py` lowered to `state_name`, but the enrichment routines look for `state`.
- **Impact:** Fails to enrich with weather, fertilizer, or irrigation.

### 3.3 `python scripts/compute_metrics.py`
- **Result:** Crashes with `ERROR: Missing columns: ['state']`.
- **Root Cause:** Hardcoded to read `data/raw/crop_production_india.csv` directly without normalizing `state_name` -> `state`, and ignores `data/processed/test.csv`.

### 3.4 `python scripts/warm_weather_cache.py`
- **Result:** Crashes with `KeyError: 'state'`.
- **Root Cause:** Reads `data/raw/crop_production_india.csv` expecting `state` instead of `State_Name`.

### 3.5 `python -m src.pipeline.train_pipeline`
- **Result:** Executes, but trains on unfiltered dataset (~124 crops, including APPLE, BANANA, ARCANUT), resulting in 168 one-hot features instead of the spec's 15 crops (~59-62 features).

### 3.6 `python -m api` and `python -m uvicorn api.main:app`
- **Result:** Operates, but returns schema for 124 crops instead of 15 crops.

### 3.7 `streamlit run dashboard/app.py`
- **Result:** Runs, but displays all Section 1 visual and functional defects.

---

## 4. Observed Defects & Confirmed Root Causes

### Defect 1: Large white top header bar over dark page
- **Symptom:** White `#FFFFFF` banner across the top of `localhost:8501`.
- **Root Cause:** Absence of `.streamlit/config.toml` configuring `[theme] base = "dark"`. Streamlit defaults to light chrome, and the custom CSS in `dashboard/app.py` does not target `header[data-testid="stHeader"]`.
- **Fix:** Create `.streamlit/config.toml` with deep green/gold dark theme tokens, and add CSS rules overriding `header[data-testid="stHeader"]` background and deploy button.

### Defect 2: Sidebar inputs white with pale-green text (unreadable)
- **Symptom:** Number inputs and dropdowns in sidebar have bright white background with light green font, failing WCAG AA contrast.
- **Root Cause:** Custom CSS in `dashboard/app.py` styled general text color to `#c8e6c9` but did not override BaseWeb UI input containers (`div[data-baseweb="input"]`, `div[data-baseweb="select"]`, `input`, `button`).
- **Fix:** Explicitly style all BaseWeb input containers, buttons, and dropdowns with dark backgrounds (`#142014`), distinct borders (`#2e4a2e`), and crisp readable text.

### Defect 3: Red default slider and red "Predict Yield" button
- **Symptom:** Accent elements render in Streamlit's default red (`#FF4B4B`).
- **Root Cause:** Missing `primaryColor = "#f9a825"` in `.streamlit/config.toml`.
- **Fix:** Set `primaryColor = "#f9a825"` (gold accent) in `config.toml` and add custom CSS for button hover/active states.

### Defect 4: Selected crop is APPLE (README specifies exactly 15 crops)
- **Symptom:** Crop selector lists APPLE, ARCANUT, etc.
- **Root Cause:** Ingestion and training never filtered `Crop` to the 15 spec crops: `[RICE, WHEAT, MAIZE, POTATO, ONION, GROUNDNUT, DRY CHILLIES, RAPESEED &MUSTARD, SUNFLOWER, SESAMUM, MOONG(GREEN GRAM), URAD, JOWAR, GRAM, ARHAR/TUR]`.
- **Fix:** Implement `scripts/prepare_new_dataset.py` to filter raw data strictly to the 15 crops, build a clean 50K stratified dataset, and retrain the model and preprocessor.

### Defect 5: Gauge fixed 0 to 100 with arbitrary zones
- **Symptom:** Predicted yield gauge is locked to 0-100 regardless of crop.
- **Root Cause:** `GAUGE_MAX_BY_CROP` dictionary in `dashboard/app.py` is hardcoded with static numbers rather than data-driven percentiles stored in `feature_schema.json`.
- **Fix:** In `build_preprocessor.py`, calculate 99th percentile yields per crop from training data, store them in `models/feature_schema.json`, and dynamically scale the gauge max and green/yellow/red zones.

### Defect 6: Inconsistent emoji icon rendering
- **Symptom:** System renders mismatched platform emoji fonts.
- **Root Cause:** Ad-hoc Unicode emojis embedded across strings without fallback styles.
- **Fix:** Standardize status indicators and icons with consistent SVGs / clean badge components.

### Defect 7: Inconsistent/hardcoded numbers
- **Symptom:** Discrepancies between displayed metrics, metadata, and README.
- **Root Cause:** Metrics calculated separately in different scripts rather than single-sourced from `models/model_metadata.json` and `models/feature_schema.json`.
- **Fix:** Centralize all metrics reading strictly from `models/model_metadata.json`.

---

## 5. README Inconsistencies & Spec Truths

1. **Endpoint Count:** README text states "15 endpoints", but the table lists 16 distinct endpoints (`/`, `/docs`, `/api/v1/health`, `/api/v1/model/info`, `/api/v1/model/metrics`, `/api/v1/crops`, `/api/v1/states`, `/api/v1/seasons`, `/api/v1/weather`, `/api/v1/forecast`, `/api/v1/irrigation`, `/api/v1/fertilizer`, `/api/v1/fertilizer/all`, `/api/v1/risk`, `/api/v1/risk/all`, `/api/v1/predict`).
   - **Resolution:** Reconcile count to **16 endpoints** in README text and table.
2. **RMSE Metrics:** Mentioned as 12.07 q/ha in one section and 11.5 q/ha in another.
   - **Resolution:** Measure exact held-out test RMSE on the new 15-crop 50K dataset and synchronize all occurrences.
3. **Feature Count:** Stated as 59 encoded features.
   - **Calculation:** 15 crops (15) + 33 states (33) + 6 seasons (6) + 8 numerical features = 62 encoded features.
   - **Resolution:** Measure post-ColumnTransformer output dimension and update README, schema, and UI together.
4. **Implausible Forecast Example:**
   - Sample response lists precipitation 1660.7 mm, +21.8 pts humidity delta, 4.61 °C spread, 45-day horizon (conflicting with 180-day text).
   - **Resolution:** Test Open-Meteo seasonal forecast API, verify daily aggregation units, and capture real response payload.
5. **Badge Versions:**
   - Streamlit 1.60 -> current stable is 1.40+ / 1.65.
   - FastAPI 0.140 -> current stable is 0.115 / 0.143.
   - Check real installed versions from environment (`xgboost==3.2.0`, `scikit-learn==1.7.2`, `streamlit==1.65.0`, `fastapi==0.143.0`, `shap==0.51.0`, `plotly==7.1.0`) and pin in requirements and badges.

---

## 6. Architecture & Data Integrity Verification

- **Target Unit:** Quintals per Hectare ($1\text{ q/ha} = 0.1\text{ t/ha} = 100\text{ kg/ha}$).
- **Formula:** $\text{yield} = \frac{\text{Production (tonnes)} \times 10}{\text{Area (hectares)}}$.
- **Target Leakage:** `Production` and `yield` excluded from $X$.
- **Offline Reliability:** All enrichment defaults to `cache_only=True` to guarantee zero network latency and no external dependency failures during batch inference and training.
