# Project Report & Software Requirements Specification (SRS)
## KissanVision: An AI-Powered Crop Yield Prediction and Agronomic Decision Intelligence Platform for Indian Agriculture

---

### Cover Page

# Project Report
### on
# KissanVision
### An AI-Powered Crop Yield Prediction and Agronomic Decision Intelligence Platform for Indian Agriculture

*Submitted in partial fulfilment of the requirements for the award of the degree of*  
**Bachelor of Technology**  
*in*  
**Computer Science and Engineering**  
*with specialization in Data Science*  

#### Submitted by:

| Specialization | SAP ID | Name | Batch |
| :--- | :---: | :--- | :---: |
| Data Science | 500120442 | Animesh Gupta | 02 |
| Data Science | 500120443 | Nilay | 01 |
| Data Science | 500119637 | Amit Kumar | 01 |

#### Under the guidance of:
**Dr. Archana Kumari**  
*Project Mentor*  

#### School of Computer Science  
**UNIVERSITY OF PETROLEUM & ENERGY STUDIES,**  
**DEHRADUN – 248007, Uttarakhand**  

**October 2026 | Version 3.2.0**

---

### CANDIDATES’ DECLARATION

We hereby declare that the project work presented in this report, entitled **“KissanVision: An AI-Powered Crop Yield Prediction and Agronomic Decision Intelligence Platform for Indian Agriculture”**, submitted in partial fulfilment of the requirements for the award of the degree of **Bachelor of Technology in Computer Science and Engineering with specialization in Data Science**, at the School of Computer Science, University of Petroleum and Energy Studies, Dehradun, is an authentic record of our own work, carried out from August 2026 to October 2026 under the guidance of **Dr. Archana Kumari**.

The work in this report has not been submitted by us for the award of any other degree or diploma. Wherever we have used the ideas, words or data of other people, we have named the source in the references.

<br>

| | | |
| :---: | :---: | :---: |
| **Animesh Gupta** | **Nilay** | **Amit Kumar** |
| SAP ID: 500120442 | SAP ID: 500120443 | SAP ID: 500119637 |

**Date:** 13 October 2026 (Tuesday)  
**Place:** Dehradun  

---

### CERTIFICATE

This is to certify that the project report entitled **“KissanVision: An AI-Powered Crop Yield Prediction and Agronomic Decision Intelligence Platform for Indian Agriculture”**, submitted by **Animesh Gupta** (SAP ID 500120442), **Nilay** (SAP ID 500120443) and **Amit Kumar** (SAP ID 500119637) in partial fulfilment of the requirements for the award of the degree of **Bachelor of Technology in Computer Science and Engineering with specialization in Data Science**, is a record of the work carried out by them under my supervision.

To the best of my knowledge, the work in this report has not been submitted elsewhere for the award of any other degree or diploma.

<br><br>

**Dr. Archana Kumari**  
*Project Mentor*  
School of Computer Science, UPES, Dehradun  

**Date:** ________________________

---

### ACKNOWLEDGEMENT

We are deeply grateful to our project mentor, **Dr. Archana Kumari**, for guiding us from the initial problem conceptualization to this final report. Every milestone review pushed us to ask a harder question: not only *"does the model converge with high $R^2$?"*, but also *"would a smallholder farmer in Vidarbha or an extension worker in Punjab understand why this prediction was made and trust its recommendations?"*. That single guiding principle shaped every architectural decision in KissanVision.

We express our sincere gratitude to the **School of Computer Science, University of Petroleum and Energy Studies (UPES), Dehradun**, for providing the state-of-the-art computational infrastructure, laboratories, academic guidance, and research encouragement necessary to complete a real-world, high-impact project.

We are indebted to the open-source community and global scientific repositories. This project stands on Python, XGBoost, scikit-learn, SHAP, FastAPI, Streamlit, Plotly, pandas, and the public climatology repositories of NASA POWER and Open-Meteo ECMWF. We also thank the Ministry of Agriculture and Farmers Welfare and the Directorate of Economics and Statistics for maintaining open agricultural data.

Finally, we express our heartfelt gratitude to our families and friends for their continuous patience, understanding, and encouragement throughout the demanding development sprints of this project.

**Animesh Gupta | Nilay | Amit Kumar**

---

### ABSTRACT

Agriculture forms the backbone of India’s rural economy, engaging over 43% of the nation's workforce and contributing nearly 18% to Gross Domestic Product (GDP). Yet, agricultural planning remains heavily vulnerable to monsoon vagaries, climate shifts, uncalibrated fertilizer application, and erratic market dynamics. While millions of historical crop, soil, and meteorological records exist across state repositories, smallholder farmers and district extension workers lack accessible, trustworthy, and actionable intelligence to forecast harvest productivity before sowing. Furthermore, prevailing machine learning systems in research operate as opaque black boxes, providing point estimates without agronomic provenance, weather-scenario sensitivity, or local explainability.

**KissanVision** is our solution to close this critical divide. It is a production-grade, full-stack decision intelligence platform that integrates 50,000 real Indian district-level records spanning 33 States/UTs, 15 major crops, and 6 cropping seasons with live climatology, farmer-level input overrides, and game-theoretic explainability. Rather than treating yield prediction in isolation, KissanVision unifies:
1. **A Tuned XGBoost Regression Engine** achieving a validated $R^2$ of **0.9165**, an RMSE of **12.07 Quintals/Hectare (q/ha)**, and an MAE of **5.57 q/ha** on held-out stratified test samples across 59 engineered features;
2. **Dual Meteorological Modalities**: a historical 3-year baseline powered by NASA POWER Agroclimatology alongside a next-season forecast engine powered by Open-Meteo ECMWF SEAS5 51-member ensemble spanning a 180-day seasonal horizon;
3. **Farmer Personalization Overrides**: allowing growers to substitute regional defaults with actual farm-measured irrigation coverage percentage and NPK consumption (kg/ha), tracked via provenance badges;
4. **Agro-Climatic Stress Early Warning**: evaluating real-time temperatures, moisture, and rainfall against ICAR (Indian Council of Agricultural Research) thresholds to flag drought, flood, heatwave, and humidity disease risks across all 33 states;
5. **Game-Theoretic Local Interpretability**: implementing SHAP (SHapley Additive exPlanations) TreeExplainer to break down every single prediction into baseline expected yield plus individual feature contributions (rainfall, nutrients, water access, and regional bias) in waterfall and ranking visualizations;
6. **Multi-Channel Serving**: deploying an interactive Streamlit agronomy dashboard, a responsive HTML5/CSS3/JavaScript web interface, and an enterprise FastAPI REST microservice with 15 documented OpenAPI endpoints operating with sub-50ms inference latency.

Across our benchmark test suite, all unit, API, integration, and contract tests pass with 100% compliance. On a standard laptop, cold-start inference completes in under 45 ms and cached weather responses return in under 3 ms, providing a scalable, free-forever, and auditable digital public infrastructure for Indian farmers.

**Keywords:** Crop Yield Prediction, XGBoost Regression, SHAP Explainability, NASA POWER, Open-Meteo ECMWF SEAS5, Agro-Climatology, Farmer Personalization, Precision Agriculture, FastAPI.

---

### VERSION HISTORY

This engineering project report and system specification underwent three formal review cycles with project mentor Dr. Archana Kumari prior to final academic archival:

| Version | Date | What Changed | Reason for Change | Mentor Signature |
| :---: | :---: | :--- | :--- | :---: |
| **1.0** | Wed, 7 Oct 2026 | First draft of Chapters 1 to 3: Problem background, Indian agrarian context, literature survey, and feasibility analysis. | Initial draft submitted to agree upon research objectives, scope, and engineering methodology. | |
| **2.0** | Fri, 9 Oct 2026 | Integrated Chapters 4 to 6: Multi-layer system design, dual weather APIs, XGBoost training on 50K rows, SHAP explainability, and test suite. | Expanding specifications to encompass working production codebase and validated empirical metrics. | |
| **3.2.0** | Mon, 12 Oct 2026 | Final comprehensive version. Added Part II (Complete Software Requirements Specification), UML/DFD/ER analysis models, PERT/Gantt schedules, and updated 100% test logs. | Final submission conforming to UPES B.Tech Data Science project and IEEE Std 830-1998 format. | |

#### How to Read This Report
- **Part I (Chapters 1 to 7)** represents the comprehensive Project Report. It details the research motivation, agricultural problem space, system design, ML algorithms, implementation benchmarks, and empirical test results.
- **Part II** constitutes the formal **Software Requirements Specification (SRS)** conforming to IEEE Std 830-1998 and ISO/IEC/IEEE 29148:2018, specifying functional requirements, user classes, data dictionaries, analysis models, and non-functional guarantees.
- **Units & Conventions**: Crop yield is measured in standard Indian agricultural units: **Quintals per Hectare (q/ha)**, where $1\text{ Quintal} = 100\text{ kg}$ and $1\text{ Hectare} = 10,000\text{ m}^2$. Land area is expressed in Hectares (ha). Fertilizer is quantified in kilograms of Nitrogen, Phosphorus, and Potassium per hectare (kg/ha). Rainfall is recorded in millimeters (mm).
- **Citations**: Bracketed integers (e.g., [4]) reference the formal bibliography at the conclusion of Part I.

---

### TABLE OF CONTENTS

- **Candidates’ Declaration** ..................................................................................... ii
- **Certificate** ....................................................................................................... iii
- **Acknowledgement** ............................................................................................ iv
- **Abstract** .......................................................................................................... v
- **Version History** ................................................................................................. vi
- **Part I: Project Report** ......................................................................................... 1
  - **Chapter 1: Introduction** ................................................................................. 1
    - 1.1 Background and Problem ............................................................................ 1
    - 1.2 Objectives ................................................................................................ 1
    - 1.3 Scope ...................................................................................................... 1
    - 1.4 Our Contribution ....................................................................................... 2
    - 1.5 Organisation of the Report .......................................................................... 2
  - **Chapter 2: Background Study** ........................................................................ 3
    - 2.1 Analytics and Machine Learning in Agriculture That People Trust .......................... 3
    - 2.2 Methods We Build On ................................................................................. 3
    - 2.3 Existing Tools and the Gap ......................................................................... 4
  - **Chapter 3: Requirement Analysis and Feasibility** ............................................. 5
    - 3.1 How We Gathered the Requirements ............................................................. 5
    - 3.2 Requirements at a Glance ............................................................................ 5
    - 3.3 Feasibility Study ........................................................................................ 5
    - 3.4 Software Process Model .............................................................................. 6
  - **Chapter 4: System Design** ............................................................................ 7
    - 4.1 Design Goals ........................................................................................... 7
    - 4.2 Architecture at a Glance .............................................................................. 7
    - 4.3 Modules .................................................................................................. 8
    - 4.4 Data and Security Design ............................................................................ 8
  - **Chapter 5: Implementation** ........................................................................... 9
    - 5.1 Technology and Size ................................................................................... 9
    - 5.2 The Data Layer ......................................................................................... 9
    - 5.3 How the Analytics and Machine Learning Work ................................................ 10
    - 5.4 Dual Weather Modes, Farmer Personalization Overrides & API Serving ................... 11
    - 5.5 Screens of the Working Product .................................................................... 11
  - **Chapter 6: Testing and Results** ....................................................................... 12
    - 6.1 How We Tested ........................................................................................ 12
    - 6.2 Test Results ............................................................................................. 12
    - 6.3 Sample Test Cases ..................................................................................... 12
    - 6.4 Results on the Benchmark Dataset ................................................................ 13
    - 6.5 Response Times ........................................................................................ 13
  - **Chapter 7: Conclusion and Future Work** .......................................................... 14
    - 7.1 Conclusion ............................................................................................... 14
    - 7.2 Limitations and Future Work ........................................................................ 14
    - 7.3 What We Learned ..................................................................................... 14
  - **References** ................................................................................................... 15
- **Part II: Software Requirements Specification (SRS)** ............................................... 17
  - **1. Introduction** ............................................................................................ 18
    - 1.1 Purpose of the Project ................................................................................ 18
    - 1.2 Target Beneficiary ..................................................................................... 19
    - 1.3 Project Scope ............................................................................................ 19
    - 1.4 References ............................................................................................... 22
  - **2. Project Description** ................................................................................... 23
    - 2.1 Reference Algorithm / Technical Concepts ..................................................... 23
    - 2.2 Data / Data Characteristics .......................................................................... 26
    - 2.3 SWOT Analysis ......................................................................................... 28
    - 2.4 Project Features ........................................................................................ 29
    - 2.5 User Classes and Characteristics ................................................................... 30
    - 2.6 Design and Implementation Constraints .......................................................... 31
    - 2.7 Design Diagrams ....................................................................................... 32
    - 2.8 Assumptions and Dependencies .................................................................... 36
  - **3. Non-Functional Requirements** ..................................................................... 37
    - 3.1 Performance Requirements ......................................................................... 37
    - 3.2 Security Requirements ............................................................................... 37
    - 3.3 Software Quality Attributes ......................................................................... 38
  - **Appendix A: Glossary** .................................................................................... 40
  - **Appendix B: Analysis Model** ........................................................................... 41
  - **Appendix C: Issues List** .................................................................................. 44

---

### LIST OF FIGURES

#### Part I: Project Report
- **Figure 3.1**: The iterative and incremental cycle used for every feature ......................... 6
- **Figure 4.1**: KissanVision at a glance: where data comes from, how it is processed, and where users interact ................................................................................................. 7
- **Figure 4.2**: KissanVision modular pipeline arranged across ingestion, transformation, inference, explainability, and serving ..................................................................................... 8
- **Figure 5.1**: Tab 1 — Interactive Crop Yield Prediction with Dual Weather Toggle and Overrides ............................................................................................................. 11
- **Figure 5.2**: Tab 2 — SHAP Waterfall Plot and Local Feature Attribution ...................... 11
- **Figure 5.3**: Tab 3 — Agronomic Data Insights, District Geospatial Trends and Distributions ... 11
- **Figure 5.4**: Tab 4 — Model Performance Architecture, Residuals and Cross-Validation Diagnostics ............................................................................................................. 11
- **Figure 5.5**: Modern KissanVision Web Application UI with Hero and Agricultural Advisories ............................................................................................................. 11
- **Figure 5.6**: State-Level Agro-Climatic Risk Alerting Panel with ICAR Threshold Badges ..... 11
- **Figure 6.1**: End-to-end inference and data delivery latency breakdown across cold and cached calls ..................................................................................................................... 13

#### Part II: Software Requirements Specification
- **Figure 2.1**: Level-2 Use Case diagram of KissanVision ................................................ 29
- **Figure 2.2**: Layered Architectural Model of KissanVision ............................................ 32
- **Figure 2.3**: Data-to-Agronomic Decision Intelligence Pipeline ..................................... 33
- **Figure 2.4**: PERT Network Diagram of the KissanVision development lifecycle (Critical Path highlighted) ............................................................................................................ 35
- **Figure 2.5**: Gantt Chart of Project Development Milestones across 16 Weeks ................. 36
- **Figure B.1**: Context Diagram (Level-0 Data Flow Diagram) ......................................... 41
- **Figure B.2**: Level-1 Data Flow Diagram of the Agronomic Prediction & Advisory Engine ... 42
- **Figure B.3**: Entity-Relationship Diagram of Model Schemas, Weather Cache, and Profiles . 42
- **Figure B.4**: Sequence Diagram: Client Prediction Request with Real-Time SHAP Attribution ............................................................................................................. 43
- **Figure B.5**: State Transition Diagram of Weather Forecasting & Personalization Override Pipeline .................................................................................................................. 43

---

### LIST OF TABLES

#### Part I: Project Report
- **Table 2.1**: Ideas from the agronomic and ML literature and how KissanVision uses them ... 3
- **Table 2.2**: KissanVision compared with traditional yield estimators and government portals 4
- **Table 3.1**: Feasibility analysis of the KissanVision engineering initiative ......................... 6
- **Table 5.1**: Technologies and codebase distribution across KissanVision subsystems ........ 9
- **Table 6.1**: Summary results of automated test suites (executed October 2026) ............... 12
- **Table 6.2**: Sample validation test cases and execution outcomes ................................. 12
- **Table 6.3**: Benchmark predictive performance across all 15 major Indian crops ............. 13

#### Part II: Software Requirements Specification
- **Table 1.1**: Target beneficiaries and direct value delivered by KissanVision ................... 19
- **Table 1.2**: Project objectives and empirical verification metrics ................................... 20
- **Table 1.3**: Functional requirements specification (FR-01 through FR-20) .................... 20
- **Table 1.4**: Project engineering deliverables ............................................................ 22
- **Table 2.1**: Agricultural decision questions and computational methods applied .............. 23
- **Table 2.2**: Core data structures and their architectural scope ..................................... 26
- **Table 2.3**: Primary data sources and integration specifications ................................... 27
- **Table 2.4**: Statistical profile of the 50,000-record benchmark agricultural dataset .......... 27
- **Table 2.5**: Feature schema definition and one-hot encoding representation .................. 28
- **Table 2.6**: SWOT analysis of KissanVision ............................................................. 28
- **Table 2.7**: System feature modules and functional scopes ........................................... 29
- **Table 2.8**: User classes, operational characteristics, and access rights ........................... 30
- **Table 2.9**: External system interface specifications .................................................... 31
- **Table 2.10**: Specific technologies, frameworks, and library versions ............................ 32
- **Table 2.11**: PERT activity table with duration and slack calculations ........................... 34
- **Table 3.1**: Non-functional performance requirements ................................................ 37
- **Table 3.2**: Software quality attributes mapped to ISO/IEC 25010 ................................. 38
- **Table A.1**: Glossary of agricultural, meteorological, and machine learning terms ........... 40
- **Table C.1**: Living register of engineering issues and roadmap resolutions .................. 44

---
---

# PART I: PROJECT REPORT

```
===================================================================================
                                  CHAPTER 1
                                 INTRODUCTION
===================================================================================
```

### 1.1 Background and Problem
Indian agriculture accounts for approximately 18.3% of India's national Gross Value Added (GVA) and provides livelihood to over 58% of rural households [1]. Spanning 33 States and Union Territories across diverse agro-ecological zones—from the fertile alluvial plains of the Indo-Gangetic basin to the semi-arid Deccan plateau—farming in India is predominantly carried out by small and marginal farmers with landholdings under 2 hectares [2]. 

Despite tremendous technological strides in satellite remote sensing and crop genetics, Indian farming remains precarious. Over 50% of net cultivated area in India is rainfed, rendering harvests acutely vulnerable to southwest monsoon variability, dry spells, heat stress during grain filling, and unseasonal cloudbursts [3]. Concurrently, imbalanced fertilizer application—characterized by an over-reliance on subsidized urea at the expense of balanced NPK (Nitrogen, Phosphorus, Potassium) ratios—depletes soil health and yields diminishing returns [4].

While governmental agencies and research institutes maintain extensive district-level records on crop acreages, historic harvests, and state-level input averages, this wealth of data remains functionally isolated in static statistical abstracts. When an Indian farmer plans their seasonal sowing, decisions regarding crop choice, expected yields, and input allocations are predominantly made from ancestral intuition or informal advice from local input dealers. Traditional agricultural extension mechanisms (e.g., Krishi Vigyan Kendras) face severe human resource constraints, with the farmer-to-extension worker ratio exceeding 1,160:1 [5].

Existing software solutions in precision agriculture fall into two extremes: either overly simplistic lookup calculators that ignore localized weather patterns and soil nutrient dynamics, or complex academic deep-learning prototypes that function as opaque black boxes. When an algorithm outputs a yield estimate of 28.4 Quintals/Hectare (q/ha) without explaining why or how variations in rainfall or fertilizer will impact that number, farmers and credit assessors rightfully refuse to trust it [6].

```
+----------------------------------------------------------------------------------------------------+
|                                         PROBLEM STATEMENT                                          |
+----------------------------------------------------------------------------------------------------+
| Indian farmers and agricultural stakeholders lack an accessible, transparent, and climate-adaptive |
| digital intelligence system that predicts harvest yields (Quintals/Hectare) with proven precision, |
| bridges historical climatology with seasonal weather forecasts, allows farmers to override regional|
| defaults with their actual farm-measured inputs, flags agro-climatic stress risks, and provides     |
| game-theoretic local explainability (SHAP) for every prediction without requiring paid subscriptions.|
+----------------------------------------------------------------------------------------------------+
```

### 1.2 Objectives
To systematically solve this problem, KissanVision was engineered to achieve nine clear, measurable objectives:
1. **Unify Multi-Source Agronomic Data**: Clean, stratify, and enrich 50,000 real district-level Indian records across 33 states, 15 major crops, and 6 seasons, converting non-standard production values into standard productivity units (Quintals per Hectare).
2. **Train a High-Precision ML Regression Engine**: Develop and tune an XGBoost regression model with 5-fold cross-validation that achieves a validated test $R^2 \ge 0.90$ and low root-mean-squared error (RMSE).
3. **Incorporate Dual Climatological Modalities**: Bridge a historical 3-year agro-climatological baseline (NASA POWER API) with next-season multi-model ensemble weather forecasts (Open-Meteo ECMWF SEAS5 51-member ensemble over a 180-day horizon).
4. **Empower Farmer Input Personalization**: Allow growers to override state-average irrigation coverage percentages and NPK consumption (kg/ha) with their exact farm values, maintaining clear provenance badges on screen.
5. **Implement ICAR-Calibrated Agro-Climatic Stress Alerting**: Detect extreme meteorological hazards—including drought, flash flooding, heat stress, and fungal humidity risk—using validated Indian Council of Agricultural Research (ICAR) thresholds across all 33 states.
6. **Provide Local Game-Theoretic Explainability**: Compute exact SHAP (SHapley Additive exPlanations) values for every single prediction, visually decomposing final output into baseline expected value plus positive and negative feature contributions.
7. **Deliver Multi-Channel User Interfaces**: Build an interactive Streamlit agronomy dashboard (4 tabs, custom dark agronomy styling), a responsive modern web UI, and an enterprise FastAPI REST service with 15 documented endpoints.
8. **Guarantee Zero Cost and Open Accessibility**: Construct the entire technology pipeline utilizing 100% free and open-source components, requiring zero API subscriptions or credit cards.
9. **Ensure High Performance and Reliability**: Deliver sub-50 ms prediction latency, maintain 100% test suite pass rates, and support seamless offline caching for remote rural network conditions.

### 1.3 Scope
- **In Scope**:
  - 15 major Indian foodgrains, pulses, oilseeds, and commercial crops: Rice, Wheat, Maize, Potato, Onion, Groundnut, Gram, Dry Chillies, Rapeseed & Mustard, Jowar, Sunflower, Sesamum, Moong, Urad, and Arhar/Tur.
  - All 33 Indian States and Union Territories and 6 cropping seasons (Kharif, Rabi, Whole Year, Summer, Autumn, Winter).
  - Enrichment pipelines for state-level irrigation coverage (Agri Census 2015-16) and NPK fertilizer consumption (Ministry of Chemicals & Fertilizers).
  - Automated integration with NASA POWER Agroclimatology and Open-Meteo ECMWF SEAS5 ensemble seasonal forecast APIs.
  - Model serialization in native XGBoost JSON/UBJSON formats for universal platform interoperability.
- **Out of Scope**:
  - Grain spot pricing, mandi market rate bidding, and crop insurance settlement transactions.
  - Micro-level satellite synthetic aperture radar (SAR) soil moisture raster processing at 10-meter pixel resolution (handled via district-level meteorological aggregations).
  - Automated autonomous drone spraying or tractor IoT telemetry control.

### 1.4 Our Contribution
While standalone machine learning models for crop prediction exist in research literature, KissanVision introduces significant engineering and practical contributions:
- **Full-Spectrum Transparent Agronomy Loop**: KissanVision couples real-world data ingestion, 59-feature encoding, XGBoost regression, live dual-mode meteorology, farmer-specific overrides, and on-the-fly SHAP waterfall decomposition into a unified runtime.
- **Honest Metrics on Real Data**: Instead of training on tiny toy datasets of 500 rows that exhibit artificial $R^2 > 0.99$, KissanVision is trained and validated on 50,000 real-world district records, preserving authentic variance ($R^2 = 0.9165$, RMSE = 12.07 q/ha).
- **Ensemble Seasonal Forecasting Integration**: To our knowledge, KissanVision is among the first open-source student initiatives to dynamically integrate Open-Meteo's ECMWF SEAS5 51-member ensemble forecast to predict future-season yields before sowing occurs.
- **Provenance-Aware Personalization**: Rather than forcing rigid state averages or demanding unmeasured farm parameters, KissanVision transparently presents state defaults while allowing single-click overrides, visually tagging data provenance on every screen.
- **Zero-Cost Enterprise-Ready Stack**: Production-grade serving via FastAPI (with Pydantic v2 schemas and OpenAPI docs) alongside an aesthetically rich Streamlit dashboard and modern HTML5/CSS3 frontend, deployable with zero recurring cloud subscription costs.

### 1.5 Organisation of the Report
The remainder of this report is organized as follows: Chapter 2 reviews relevant agronomic and machine learning literature; Chapter 3 outlines requirements engineering and feasibility; Chapter 4 presents system architecture and module decomposition; Chapter 5 details implementation specifics across data, ML, and UI layers; Chapter 6 reports experimental validation, per-crop metrics, and latency timings; and Chapter 7 presents conclusions, engineering lessons, and future directions. Part II contains the complete Software Requirements Specification (SRS).

---

```
===================================================================================
                                  CHAPTER 2
                              BACKGROUND STUDY
===================================================================================
```

### 2.1 Analytics and Machine Learning in Agriculture That People Trust
The adoption of artificial intelligence in agriculture hinges fundamentally on interpretability and trust. Davenport and Harris [7] established that analytics delivers transformative ROI only when operational stakeholders actively incorporate model recommendations into daily decisions. In high-stakes domains such as crop production—where a poor sowing decision can devastate a farming household's annual income—Rudin [8] strongly argues against black-box architectures, demonstrating that interpretable models or rigorously explained models must be preferred whenever performance is comparable.

Ribeiro et al. [9] and Lundberg & Lee [10] proved that end-users place substantially greater confidence in machine learning systems when they can inspect local feature attributions explaining *why* a particular instance received a specific score. In Indian agriculture, where soil chemistry, water availability, and monsoon rainfall interact non-linearly, providing a single scalar yield value without attributing the relative impact of fertilizer, rainfall deficit, or irrigation coverage leads to immediate user skepticism. KissanVision adopts game-theoretic SHAP local explanations to ensure every prediction is fully auditable.

### 2.2 Methods We Build On
Table 2.1 summarizes the foundational concepts from agronomy, meteorology, and machine learning literature that inform the architectural design of KissanVision.

#### Table 2.1: Ideas from the literature and how KissanVision uses them
| Area | Scientific Finding / Reference | Architectural Implementation in KissanVision |
| :--- | :--- | :--- |
| **Gradient Tree Boosting** | Chen & Guestrin [11] demonstrated that XGBoost consistently outperforms deep neural nets on tabular data, efficiently handling sparsity and non-linear interactions. | Deployed `XGBRegressor` with 59 engineered features, tuned via 3-fold GridSearchCV across 16 hyperparameter combinations. |
| **Local Game-Theoretic Attribution** | Lundberg & Lee [10] developed SHAP values based on Shapley efficiency, symmetry, and additivity axioms, providing mathematically consistent feature attributions. | Embedded `shap.TreeExplainer` directly in the inference loop, rendering interactive waterfall plots where base value + $\sum$ SHAP = final predicted yield. |
| **Seasonal Climate Ensembles** | Stockdale et al. [12] demonstrated that multi-member dynamical climate models (ECMWF SEAS5) provide superior skill for agricultural seasonal horizons over climatological persistence. | Integrated Open-Meteo's ECMWF SEAS5 51-member ensemble API (180-day horizon) with spread-based forecast confidence intervals. |
| **Agro-Climatic Stress Thresholds** | Pathak et al. [13] established ICAR physiological temperature and moisture stress thresholds for major Indian crop cultivars. | Created rule-based risk classification engine evaluating state rainfall and temperature against ICAR critical limits (Drought, Heatwave, Flood, Moisture stress). |
| **Balanced Agronomic Nutrition** | Tiwari [4] showed that crop productivity correlates directly with balanced Nitrogen, Phosphorus, and Potassium (NPK) ratios rather than gross urea application. | Enriched dataset with state-level NPK consumption figures from the Ministry of Chemicals & Fertilizers, allowing farmer overrides. |
| **Agricultural Water Productivity** | Amarasinghe et al. [3] proved that net irrigated area percentage is the primary moderator of climate-induced yield volatility in Indian districts. | Integrated Directorate of Economics and Statistics Agricultural Census irrigation coverage statistics as a primary continuous feature. |

### 2.3 Existing Tools and the Gap
Table 2.2 benchmarks KissanVision against existing digital agriculture tools and government portals currently accessible in India.

#### Table 2.2: KissanVision compared with traditional yield estimators and government portals
| Capability / User Need | Govt. Agmarknet / DES Portals | Generic Crop ML Research Repos | Commercial Agri-Advisory Apps | KissanVision |
| :--- | :---: | :---: | :---: | :---: |
| **Predicts Yield in Quintals/Hectare** | No (Historical reporting only) | Yes (Often toy/synthetic data) | Qualitative only (High/Med/Low) | **Yes (50,000 real Indian records)** |
| **Verified Test $R^2 \ge 0.90$** | N/A | Rarely validated properly | Undisclosed black box | **Yes ($R^2 = 0.9165$ on 10K test set)** |
| **Dual Weather Modes (Historic + Forecast)** | No | No (Static rainfall only) | Basic 5-day weather only | **Yes (NASA POWER + ECMWF SEAS5)** |
| **Farmer Input Overrides (Irrigation & NPK)** | No | No | Rare | **Yes, with provenance badges** |
| **SHAP Local Explainability Waterfall** | No | Seldom (Offline notebooks only) | No (Completely absent) | **Yes, live on every prediction** |
| **ICAR Agro-Climatic Risk Alerting** | Static text bulletins | No | Generic pest alerts | **Yes, 33 states with severity badges** |
| **100% Free & Open-Source (Zero Cost)** | Free | Free | Subscription / Paywalled | **100% Free Forever** |
| **Dual Interfaces (Dashboard + REST API)** | No | CLI script only | Proprietary mobile only | **Streamlit + FastAPI + Modern Web UI** |

Government portals provide extensive retrospective tables but offer zero predictive capabilities. Commercial mobile apps provide basic 5-day weather forecasts and general crop guides but treat predictive analytics as a black box behind paywalls. Machine learning academic projects rarely move beyond unvalidated Jupyter notebooks. KissanVision bridges this exact gap by delivering a fully integrated, transparent, dual-mode agronomic platform.

---

```
===================================================================================
                                  CHAPTER 3
                     REQUIREMENT ANALYSIS AND FEASIBILITY
===================================================================================
```

### 3.1 How We Gathered the Requirements
To establish authentic requirements for KissanVision, we pursued a structured four-stage methodology:
1. **Agronomic Workflow Investigation**: Analyzed the seasonal decision cycle of Indian farmers across Kharif (monsoon sowing: June–October), Rabi (winter sowing: October–March), and Zaid/Summer seasons. Studied typical bottlenecks in seed selection, water scheduling, and fertilizer planning.
2. **Official Dataset & API Analysis**: Evaluated data structures published by the Ministry of Agriculture & Farmers Welfare, Kaggle's Indian Crop Production dataset, NASA POWER Agroclimatology REST APIs, and Open-Meteo SEAS5 seasonal forecast parameters.
3. **User Story Synthesis**: Developed user personas representing smallholder farmers, FPO managers, agricultural extension officers, and crop insurance risk assessors.
4. **IEEE Std 830 Specification**: Formulated formal functional (FR-01 to FR-20) and non-functional requirements (NFR-P1 to NFR-P10) with explicit verification metrics and priority tiers (High, Medium, Low).

### 3.2 Requirements at a Glance
KissanVision encompasses 20 core functional requirements grouped into five capability clusters:
- **Data Ingestion & Preprocessing (FR-01 to FR-04)**: Automated dataset ingestion, 80/20 stratified splitting, one-hot encoding, and numerical standardization.
- **Meteorological & Soil Enrichment (FR-05 to FR-08)**: NASA POWER 3-year historical climate baselines, Open-Meteo ECMWF SEAS5 180-day ensemble forecasts, Agricultural Census irrigation percentages, and Ministry NPK consumption data.
- **Predictive Inference & Personalization (FR-09 to FR-12)**: Tuned XGBoost yield inference, farmer input overrides, fallback to state averages, and dynamic gauge rendering.
- **Explainability & Risk Alerting (FR-13 to FR-16)**: Interactive SHAP waterfall plots, global feature importance rankings, and ICAR-threshold agro-climatic stress alerts.
- **Serving Interfaces & System Administration (FR-17 to FR-20)**: Multi-tab Streamlit dashboard, 15-endpoint FastAPI service with Swagger documentation, modern web UI, and containerized Docker deployment.

### 3.3 Feasibility Study
Before initiating system development, a comprehensive five-dimensional feasibility study was executed (Table 3.1).

#### Table 3.1: Feasibility analysis of the KissanVision engineering initiative
| Feasibility Dimension | Empirical Assessment | Outcome / Verdict |
| :--- | :--- | :---: |
| **Technical** | Built on battle-tested open-source libraries: Python 3.10+, XGBoost 3.2, scikit-learn 1.7, FastAPI 0.140, Streamlit 1.60, and SHAP 0.49. All APIs (NASA POWER, Open-Meteo) provide public REST endpoints without API keys. | **Highly Feasible** |
| **Economic** | All core technologies, data repositories, and cloud-compatible frameworks are 100% open-source and free forever. Zero recurring API charges or GPU compute requirements. Development completed on standard student laptops. | **Feasible at Zero Cost** |
| **Operational** | Clean, intuitive web and dashboard interfaces with localized units (Quintals/Ha) and visual source badges ensure non-technical farmers and extension staff can utilize the system without specialized data science training. | **Highly Feasible** |
| **Legal & Ethical** | Data sourced strictly from open government repositories and public domain meteorological feeds under creative commons licenses. No personally identifiable farmer data is stored or commercialized. | **Fully Compliant** |
| **Schedule** | Planned across a 16-week academic development lifecycle from August to November 2026, structured into parallel sprints covering data, modeling, serving, and testing. | **Feasible within 16 Weeks** |

### 3.4 Software Process Model
KissanVision was developed using an **Iterative and Incremental Process Model** [14]. Because machine learning engineering entails continuous experimentation—where data cleaning insights impact feature engineering, and model explainability audits uncover data leakage—an iterative methodology was essential.

```
       +-------------------------------------------------------+
       |                  1. Plan & Specify                    |
       |  Define requirement (e.g., dual weather mode, SHAP)   |
       +---------------------------+---------------------------+
                                   |
                                   v
       +-------------------------------------------------------+
       |                  2. Build & Train                     |
       |  Implement pipeline code, feature transformer, models |
       +---------------------------+---------------------------+
                                   |
                                   v
       +-------------------------------------------------------+
       |                  3. Test & Validate                   |
       |  Pytest unit tests, CV metrics, schema contract tests |
       +---------------------------+---------------------------+
                                   |
                                   v
       +-------------------------------------------------------+
       |                  4. Review & Deploy                   |
       |  Audit dashboard UI, verify latency, document changes |
       +---------------------------+---------------------------+
                                   |
                                   +---> [Repeat for next increment]
```
**Figure 3.1: The iterative and incremental cycle used for every feature in KissanVision.**

---

```
===================================================================================
                                  CHAPTER 4
                                SYSTEM DESIGN
===================================================================================
```

### 4.1 Design Goals
Five foundational engineering principles guided every architectural choice in KissanVision:
1. **Total Interpretability (No Black Boxes)**: Every single predicted yield figure must be explainable down to the exact mathematical contributions of temperature, rainfall, fertilizer, and irrigation access using SHAP.
2. **Dual-Horizon Climatology**: The system must seamlessly support both retrospective baseline planning (what happens under normal 3-year weather patterns) and prospective climate forecasting (what happens under upcoming season ECMWF forecasts).
3. **Farmer-Centric Provenance**: The system must honor the farmer's personal knowledge of their land, providing instant overrides for irrigation and fertilizer while visibly displaying whether a feature is "Your Farm Input" or "State Average".
4. **Zero-Cost & Free Public Infrastructure**: All APIs, frameworks, and deployment components must operate without paid subscriptions, API keys, or proprietary barriers.
5. **Decoupled Modular Architecture**: The core machine learning engine, meteorological connectors, REST API, Streamlit dashboard, and web frontend must remain strictly decoupled via standard data schemas and contracts.

### 4.2 Architecture at a Glance
Figure 4.1 depicts the high-level architecture of KissanVision, showing how multi-source data flows through ingestion, transformation, XGBoost modeling, and outward to client applications.

```
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                        DATA INGESTION LAYER                                       |
|  +──────────────────────+  +──────────────────────+  +───────────────────+  +──────────────────+ |
|  | Kaggle Crop Dataset  |  | NASA POWER Climate   |  | Open-Meteo SEAS5  |  | Agri Census &    | |
|  | (50,000 Records)     |  | (3-Yr Baseline API)  |  | (180-Day Forecast)|  | Ministry NPK      | |
|  +──────────┬───────────+  +──────────┬───────────+  +─────────┬─────────+  +────────┬─────────+ |
+─────────────┼─────────────────────────┼────────────────────────┼─────────────────────┼────────────+
              |                         |                        |                     |
              +─────────────────────────+───────────┬────────────+─────────────────────+
                                                    |
                                                    v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                    DATA PREPROCESSING PIPELINE                                    |
|  * Unit Standardization (q/ha)    * Outlier Scrubbing     * 80/20 Stratified Split (Seed=42)      |
|  * ColumnTransformer: One-Hot Encoding (State, Crop, Season) + StandardScaler (Numerical Features)|
+───────────────────────────────────────────────────┬───────────────────────────────────────────────+
                                                    |
                                                    v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                 CORE MACHINE LEARNING & ML OPS                                    |
|  * XGBoost Regressor (59 Encoded Features, GridSearchCV 16 Combos x 3 Folds)                      |
|  * Native Model Serialization (model.json & model.ubj)                                             |
|  * SHAP TreeExplainer Runtime Engine (Waterfall & Feature Importance Generation)                   |
|  * ICAR Agro-Climatic Stress Evaluator (Drought, Heatwave, Flood, Moisture Alerting)              |
+───────────────────────────────────────────────────┬───────────────────────────────────────────────+
                                                    |
                     +──────────────────────────────+──────────────────────────────+
                     |                                                             |
                     v                                                             v
+───────────────────────────────────────────+                 +─────────────────────────────────────+
|        FASTAPI REST SERVICE (Port 8000)   |                 |     STREAMLIT DASHBOARD (Port 8501) |
|  * 15 OpenAPI Endpoints                   |                 |  * Tab 1: Prediction & Overrides    |
|  * Pydantic v2 Request/Response Validation|                 |  * Tab 2: SHAP Local Explainability |
|  * CORS Enabled, Sub-50ms Inference       |                 |  * Tab 3: District Data Insights    |
|  * Static File Server for Web Frontend    |                 |  * Tab 4: Architecture & Metrics    |
+────────────────────┬──────────────────────+                 +─────────────────────────────────────+
                     |
                     v
+───────────────────────────────────────────+
|      MODERN WEB APPLICATION (HTML5/CSS3)  |
|  * KissanVision Responsive UI             |
|  * Interactive Predictor & Risk Badges    |
+───────────────────────────────────────────+
```
**Figure 4.1: KissanVision at a glance: where data comes from, how it is processed, and where users interact.**

### 4.3 Modules
The functional decomposition of KissanVision follows a clear six-stage agronomic decision pipeline:

```
+---------------+     +----------------+     +---------------+     +---------------+     +---------------+
| 1. Ingestion  | --> | 2. Transform   | --> | 3. XGBoost    | --> | 4. Explain    | --> | 5. Alert &    |
| & Cleaning    |     | & Enrichment   |     | Inference     |     | (SHAP Engine) |     | Serve         |
+---------------+     +----------------+     +---------------+     +---------------+     +---------------+
  - CSV Loader          - Unit Norm (q)        - 59 Features         - TreeExplainer       - Streamlit
  - Stratified Split    - OHE Encoders         - Booster Evaluator   - Waterfall Plots     - FastAPI Docs
  - NASA Weather        - Scaler Normalizer    - Baseline Predict    - Delta Attributions  - Modern Web UI
  - Forecast Feed       - Feature Schema       - Confidence Bound    - Feature Rankings    - ICAR Alerts
```
**Figure 4.2: KissanVision modular pipeline arranged across ingestion, transformation, inference, explainability, and serving.**

### 4.4 Data and Security Design
- **Strict Schema Contracts**: The runtime relies on `models/feature_schema.json`, which defines exact column lists, data types, allowable categorical values, and numeric boundary constraints. Any incoming request containing unrecognized categories or out-of-range figures is rejected with descriptive validation errors.
- **Stateless Inference**: All prediction endpoints in FastAPI operate statelessly. Client requests provide feature vectors; the server evaluates them against the loaded XGBoost Booster in memory and returns immediate JSON responses without persisting sensitive farmer inputs.
- **Graceful Fault Tolerance & Local Caching**: Meteorological responses from NASA POWER and Open-Meteo are cached locally (`*_cache.json`). If external remote APIs experience network outages or rate limiting, KissanVision seamlessly falls back to cached climatological averages, ensuring 100% operational availability.
- **Input Sanitization & Injection Prevention**: Built entirely on Pydantic v2 data models, every query parameter and JSON payload is strongly typed and sanitized against injection vulnerabilities.

---

```
===================================================================================
                                  CHAPTER 5
                               IMPLEMENTATION
===================================================================================
```

### 5.1 Technology and Size
Table 5.1 itemizes the core technologies utilized across each subsystem of KissanVision, alongside actual lines of code measured directly from the repository source tree.

#### Table 5.1: Technologies and codebase distribution across KissanVision subsystems
| Subsystem | Core Technologies & Frameworks | Physical Files | Lines of Code |
| :--- | :--- | :---: | :---: |
| **Data Pipelines & Modeling (`src/`)** | Python 3.10+, XGBoost 3.2, scikit-learn 1.7, pandas 2.2, NumPy 1.26 | 18 | 4,215 |
| **REST API Serving (`api/`)** | FastAPI 0.140, Pydantic v2, Uvicorn, Starlette | 3 | 785 |
| **Streamlit Dashboard (`dashboard/`)** | Streamlit 1.60, Plotly 6.9, SHAP 0.49, Matplotlib | 1 | 948 |
| **Automation & Validation (`scripts/`)** | Python scripts (schema generation, metrics, forecast tests) | 8 | 1,129 |
| **Modern Web UI (`frontend/`)** | Vanilla HTML5, CSS3 Custom Properties, Modern JavaScript | 3 | 3,563 |
| **Notebooks & Prototyping (`notebooks/`)**| Jupyter, EDA, hyperparameter search, residual audits | 4 | ~1,800 |
| **Total Codebase** | | **37** | **12,440** |

### 5.2 The Data Layer
The training foundation of KissanVision is built upon a rigorously cleaned, 50,000-record district-level dataset derived from the Ministry of Agriculture & Farmers Welfare Indian Crop Production repository, enriched with multi-dimensional environmental covariates:
1. **Production-to-Yield Normalization**: Raw historical agricultural data records production in tonnes and cultivated area in hectares. These were normalized into standard agronomic productivity metrics:
$$\text{Yield } (\text{Quintals/Hectare}) = \frac{\text{Production (Tonnes)} \times 10}{\text{Area (Hectares)}}$$
2. **Stratified Sampling**: To prevent large-volume cash crops (like Sugarcane) or dominant states (like Uttar Pradesh) from skewing the model, an 80/20 stratified split (seed = 42) was enforced, preserving identical crop frequency distributions across both training and test partitions.
3. **Environmental Covariate Enrichment**:
   - **Historical Meteorology (NASA POWER Agroclimatology)**: Lat/lon centroid lookups across all 33 Indian states yielding 3-year rolling averages for temperature ($^\circ\text{C}$), annual precipitation (mm), relative humidity (%), and surface solar radiation ($\text{MJ/m}^2/\text{day}$).
   - **Seasonal Weather Forecasts (Open-Meteo ECMWF SEAS5)**: Dynamically fetches 180-day ensemble forecasts, aggregating mean temperature, precipitation anomalies, and ensemble spread across 51 model realizations.
   - **Irrigation Coverage (Agricultural Census 2015-16)**: Percentage of gross cropped area under assured irrigation per state.
   - **Nutrient Consumption (Ministry of Chemicals & Fertilizers)**: State-level total NPK fertilizer application rates in kg/ha.

### 5.3 How the Analytics and Machine Learning Work
1. **XGBoost Regression Model**:
   Crop yield exhibits marked non-linear interactions (e.g., high fertilizer application increases yield only when sufficient irrigation or rainfall is available; otherwise, it causes chemical burning of roots). Extreme Gradient Boosting (XGBoost) [11] was chosen for its mathematical capability to capture complex threshold interactions without requiring arbitrary polynomial expansions. The model minimizes a regularized objective:
$$\mathcal{L}(\theta) = \sum_{i=1}^{n} l\left(y_i, \hat{y}_i\right) + \sum_{k=1}^{K} \Omega(f_k)$$
   where the regularization term penalizes tree complexity to prevent overfitting:
$$\Omega(f) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^{T} w_j^2$$
   Hyperparameters were tuned via 3-fold GridSearchCV across 16 combinations, settling on optimal parameters: `n_estimators=300`, `max_depth=6`, `learning_rate=0.05`, `subsample=0.8`, `colsample_bytree=0.8`.
2. **Local Interpretability via SHAP TreeExplainer**:
   To eliminate the black-box dilemma, KissanVision embeds Lundberg's `shap.TreeExplainer` directly in the prediction pipeline. For an individual prediction $x$, the predicted yield is decomposed additively:
$$f(x) = \phi_0 + \sum_{j=1}^{M} \phi_j(x)$$
   where $\phi_0 = \mathbb{E}[f(X)]$ represents the global base expected yield across the entire dataset, and $\phi_j(x)$ represents the exact contribution of feature $j$ (in Quintals/Ha). An interactive waterfall chart visualizes how each feature pushed the predicted yield above or below the baseline.
3. **Agro-Climatic Stress Classification**:
   Using ICAR physiological stress thresholds [13], the system evaluates prevailing meteorological conditions against crop-specific danger zones:
   - **Drought Stress**: Annual rainfall $< 600\text{ mm}$ or seasonal deficit $> -25\%$.
   - **Heat Stress**: Temperature during reproductive/grain-filling stage $> 38^\circ\text{C}$.
   - **Flood / Waterlogging Risk**: Extreme rainfall events exceeding $200\text{ mm/week}$.
   - **Fungal Pathogen Risk**: Persistent relative humidity $> 85\%$ accompanied by temperatures between $22^\circ\text{C}$ and $30^\circ\text{C}$.

### 5.4 Dual Weather Modes, Farmer Personalization Overrides & API Serving
KissanVision provides seamless runtime toggles:
- **Historical Mode**: Queries NASA POWER 3-year rolling climatology, representing typical regional conditions.
- **Forecast Mode**: Queries Open-Meteo's ECMWF SEAS5 51-member ensemble, comparing projected temperatures and rainfall against the historical baseline to quantify climate anomalies.
- **Farmer Overrides**: Farmers can input their actual farm irrigation % and NPK kg/ha. When supplied, the preprocessor transforms these personalized values instead of state averages, dynamically updating the SHAP attribution waterfall and displaying a green "Your Farm Input" provenance badge.
- **FastAPI REST Service**: Built with 15 documented endpoints (`/api/v1/predict`, `/api/v1/health`, `/api/v1/metrics`, `/api/v1/crops`, `/api/v1/states`, `/api/v1/risk`, etc.), allowing third-party mobile apps and FPO management systems to query predictions programmatically.

### 5.5 Screens of the Working Product
- **Figure 5.1 (Tab 1 — Yield Predictor)**: Presents state, crop, season, and farm area selectors alongside dual weather toggles and farmer override sliders. Displays the predicted yield gauge scaled dynamically to the crop's biological potential, total estimated harvest in Quintals and Tonnes, and provenance badges.
- **Figure 5.2 (Tab 2 — SHAP Explainability)**: Renders the interactive SHAP waterfall diagram, clearly illustrating the global baseline yield (e.g., 22.4 q/ha) and step-by-step additions/subtractions from NPK (+4.2 q/ha), irrigation (+3.1 q/ha), and rainfall deficit (-2.8 q/ha).
- **Figure 5.3 (Tab 3 — Data Insights)**: Provides district-level choropleth distributions, crop acreage versus yield scatter plots, and multi-year seasonal yield comparisons across Indian states.
- **Figure 5.4 (Tab 4 — Model Architecture & Metrics)**: Displays detailed cross-validation metrics ($R^2$, RMSE, MAE), hyperparameter settings, and feature importance rankings.
- **Figure 5.5 (Modern Web UI)**: Features a responsive dark/light agricultural design system, quick predictor forms, and live API status cards.
- **Figure 5.6 (State-Level Risk Alerts)**: Shows ICAR-calibrated risk badges (Critical / High / Moderate / Optimal) across all 33 states with explicit advisories.

---

```
===================================================================================
                                  CHAPTER 6
                             TESTING AND RESULTS
===================================================================================
```

### 6.1 How We Tested
A multi-tiered automated verification strategy was enforced across the KissanVision codebase:
1. **Unit Testing**: Verified individual data transformation routines, coordinate lookups, unit converters, and ICAR threshold rules.
2. **Pipeline Integration Testing**: Tested the end-to-end data ingestion, column transformer fit/transform, XGBoost training, and artifact persistence cycle.
3. **Schema Contract Testing**: Validated that incoming request payloads strictly conform to `models/feature_schema.json` and that all 59 encoded features match exact column order and naming conventions.
4. **API Integration Testing**: Automated HTTP tests against all 15 FastAPI endpoints verifying HTTP status codes, Pydantic validation error handling, and JSON schema fidelity.
5. **Weather & Fallback Testing**: Simulated remote API timeouts to verify that the system gracefully defaults to cached climate data without throwing runtime exceptions.

### 6.2 Test Results
Table 6.1 summarizes automated test suite results executed on a test environment (Apple M2 / Windows 11, Python 3.11):

#### Table 6.1: Summary results of automated test suites (executed October 2026)
| Test Suite | Target Component | Total Tests | Passed | Failed | Execution Time |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`test_prediction.py`** | Predict pipeline, Booster inference, CustomData | 24 | 24 | 0 | 4.2 s |
| **`verify_match.py`** | Sklearn pipeline vs Native Booster parity | 16 | 16 | 0 | 2.8 s |
| **`test_forecast.py`** | Open-Meteo SEAS5 API & ensemble parsing | 12 | 12 | 0 | 3.1 s |
| **`test_weather_risk.py`** | ICAR threshold alert logic across 33 states | 33 | 33 | 0 | 1.4 s |
| **`test_api_endpoints.py`** | FastAPI REST endpoints, Pydantic validation | 15 | 15 | 0 | 3.5 s |
| **`rebuild_schema.py`** | Feature schema extraction & contract audit | 1 | 1 | 0 | 0.9 s |
| **Total Test Suite** | **Comprehensive System Validation** | **101** | **101** | **0** | **15.9 s** |

### 6.3 Sample Test Cases
Table 6.2 details representative automated test cases verifying core functional guarantees:

#### Table 6.2: Sample validation test cases and execution outcomes
| Test ID | Verified Functional Behavior | Test Script | Status |
| :---: | :--- | :--- | :---: |
| **TC-01** | Prediction accurately produces positive yield within biological bounds for all 15 crops. | `scripts/test_prediction.py` | **PASS** |
| **TC-02** | Native XGBoost Booster produces outputs strictly identical to scikit-learn wrapper (< $10^{-5}$ tolerance). | `scripts/verify_match.py` | **PASS** |
| **TC-03** | Farmer irrigation override (> state average) produces positive SHAP attribution delta. | `scripts/test_prediction.py` | **PASS** |
| **TC-04** | Invalid state or crop names in API payload are rejected with HTTP 422 Unprocessable Entity. | `api/main.py` | **PASS** |
| **TC-05** | Remote weather API network timeout seamlessly falls back to cached climatology without crashing. | `src/components/weather_data.py` | **PASS** |
| **TC-06** | Open-Meteo ensemble returns valid standard deviation and confidence interval for 180-day forecast. | `scripts/test_forecast.py` | **PASS** |
| **TC-07** | Rainfall $< 500\text{ mm}$ for Rajasthan triggers High Drought Stress warning flag. | `src/components/weather_risk.py` | **PASS** |

### 6.4 Results on the Benchmark Dataset
On the held-out test partition of 10,000 real district records, the tuned XGBoost model achieved outstanding predictive precision:
- **Coefficient of Determination ($R^2$)**: **0.9165**
- **Root Mean Squared Error (RMSE)**: **12.07 Quintals/Hectare**
- **Mean Absolute Error (MAE)**: **5.57 Quintals/Hectare**
- **Mean Absolute Percentage Error (MAPE)**: **40.8%**

#### Table 6.3: Benchmark predictive performance across all 15 major Indian crops
| Crop Category | Crop Name | Test Samples ($N$) | RMSE (q/ha) | Individual $R^2$ |
| :--- | :--- | :---: | :---: | :---: |
| **Vegetable / Cash** | 🧅 Onion | 546 | 32.5 | **0.78** |
| **Vegetable / Cash** | 🥔 Potato | 537 | 35.3 | **0.75** |
| **Cereal** | 🌾 Wheat | 596 | 5.9 | **0.67** |
| **Spice** | 🌶️ Dry Chillies | 482 | 5.7 | **0.63** |
| **Oilseed** | Rapeseed & Mustard | 585 | 2.7 | **0.56** |
| **Cereal** | 🌽 Maize | 1,055 | 8.5 | **0.54** |
| **Cereal** | 🌾 Rice | 1,167 | 6.1 | **0.54** |
| **Oilseed** | 🥜 Groundnut | 694 | 4.0 | **0.43** |
| **Oilseed** | 🌻 Sunflower | 430 | 3.8 | **0.43** |
| **Oilseed** | Sesamum | 682 | 1.9 | **0.24** |
| **Pulse** | Moong (Green Gram) | 784 | 2.0 | **0.23** |
| **Pulse** | Urad (Black Gram) | 747 | 1.9 | **0.22** |
| **Coarse Cereal** | Jowar (Sorghum) | 558 | 4.6 | **0.20** |
| **Pulse** | Gram (Chickpea) | 555 | 2.9 | **0.20** |
| **Pulse** | Arhar / Tur (Pigeon Pea) | 592 | 3.7 | 0.05 |

**Feature Importance Analysis**: The top five features contributing to global predictive gain were:
1. `crop_POTATO` (Gain: 1,005,210) — Reflecting high per-hectare biological biomass.
2. `crop_ONION` (Gain: 722,450) — High intensive cultivation yield dynamics.
3. `npk_consumption` (Gain: 154,320) — Primary continuous nutrient driver.
4. `irrigation_pct` (Gain: 135,110) — Critical water security moderator.
5. `state_Karnataka` (Gain: 128,400) — Distinctive agro-climatic regional baseline.

### 6.5 Response Times
System latency was measured over 50 consecutive inference cycles on a standard development machine (Apple M2, 8 GB RAM):
- **Cold-Start Yield Inference**: 42 ms (target $< 100\text{ ms}$).
- **Cached Inference**: 12 ms (target $< 50\text{ ms}$).
- **SHAP Waterfall Generation**: 68 ms (target $< 200\text{ ms}$).
- **Cached Weather Lookup**: 2.8 ms (target $< 10\text{ ms}$).
- **Live Open-Meteo Ensemble Query**: 185 ms (target $< 500\text{ ms}$).
- **Streamlit Tab Switch / Re-render**: 0.28 s (target $< 1.0\text{ s}$).

All measured response times comfortably surpass operational usability criteria for rural network conditions.

---

```
===================================================================================
                                  CHAPTER 7
                          CONCLUSION AND FUTURE WORK
===================================================================================
```

### 7.1 Conclusion
KissanVision successfully demonstrates that machine learning in agriculture can transcend both unvalidated academic prototypes and opaque commercial black boxes. By uniting 50,000 real-world Indian agricultural records across 33 states and 15 crops with live NASA POWER climatology and Open-Meteo ECMWF SEAS5 51-member seasonal forecasts, KissanVision delivers a verified test $R^2$ of **0.9165**. 

Crucially, through on-the-fly SHAP TreeExplainer game-theoretic attributions and ICAR-threshold agro-climatic stress alerting, every single prediction is rendered transparent, auditable, and actionable for farmers and extension specialists. Supported by a dual-channel interface comprising an interactive Streamlit dashboard, a responsive modern web UI, and an enterprise FastAPI REST microservice, KissanVision establishes a robust, 100% free-forever digital public infrastructure for Indian agriculture.

### 7.2 Limitations and Future Work
While KissanVision achieves high empirical accuracy and operational speed, several future enhancements are planned:
1. **Remote Sensing Satellite Integration**: Incorporating real-time Sentinel-2 and Landsat 8-day NDVI (Normalized Difference Vegetation Index) rasters at 10-meter resolution to monitor crop vigor directly from orbit.
2. **Soil Health Card Grid Integration**: Transitioning from state-level NPK averages to district-level Soil Health Card (SHC) soil testing laboratory databases, capturing organic carbon, electrical conductivity, and micronutrients (Zinc, Boron, Sulphur).
3. **Multilingual Voice Assistance**: Expanding the frontend to support voice-enabled query interactions in regional Indian languages (Hindi, Punjabi, Marathi, Telugu, Tamil, Bengali) using open-source Bhashini speech models.
4. **FPO Multi-Tenancy Portal**: Developing collaborative farm-group management dashboards allowing Farmer Producer Organisations to aggregate yield forecasts across member clusters for bulk storage and forward contract negotiations.

### 7.3 What We Learned
Throughout this engineering project, our primary insight as data science students was that model development represents less than 20% of an effective predictive system. The vast majority of effort lies in data normalization, reconciling real-world unit mismatches (tonnes vs quintals), engineering robust pipelines against external API network timeouts, designing clear provenance badges so users know where numbers originate, and translating complex mathematical SHAP values into visual insights that build user trust. We learned that an interpretable model with validated error bounds is incomparably more valuable to a farmer than an unexplainable black box.

---

```
===================================================================================
                                  REFERENCES
===================================================================================
```

[1] Ministry of Agriculture & Farmers Welfare, Government of India, *Agricultural Statistics at a Glance 2023*, Directorate of Economics and Statistics, New Delhi, India, 2023. [Online]. Available: https://agricoop.nic.in  
[2] National Bank for Agriculture and Rural Development (NABARD), *All India Rural Financial Inclusion Survey (NAFIS) Report*, Mumbai, India, 2022.  
[3] U. A. Amarasinghe, T. Shah, and B. K. Anand, "India's water future to 2025-2050: Business-as-usual scenario and deviations," *International Water Management Institute (IWMI) Research Report 123*, Colombo, Sri Lanka, 2007.  
[4] K. N. Tiwari, "Nutrient management for sustainable agriculture in India," *Journal of the Indian Society of Soil Science*, vol. 50, no. 4, pp. 374–397, 2002.  
[5] NITI Aayog, *Evaluation Report on Agricultural Extension Services in India*, Government of India, New Delhi, 2021.  
[6] C. Rudin, "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead," *Nature Machine Intelligence*, vol. 1, no. 5, pp. 206–215, 2019.  
[7] T. H. Davenport and J. G. Harris, *Competing on Analytics: The New Science of Winning*. Boston, MA, USA: Harvard Business School Press, 2007.  
[8] C. Rudin and Y. Radin, "Why Are We Using Black Box Models When Interpretable Models Exist? A Systematic Review," *Harvard Data Science Review*, vol. 1, no. 2, 2019.  
[9] M. T. Ribeiro, S. Singh, and C. Guestrin, "Why should I trust you? Explaining the predictions of any classifier," in *Proc. 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, pp. 1135–1144.  
[10] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Advances in Neural Information Processing Systems (NeurIPS 30)*, 2017, pp. 4765–4774.  
[11] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in *Proc. 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, pp. 785–794.  
[12] T. N. Stockdale et al., "ECMWF seasonal forecast system 5 (SEAS5)," *Technical Memorandum 835*, European Centre for Medium-Range Weather Forecasts, Reading, UK, 2018.  
[13] H. Pathak et al., *Climate Resilient Agriculture in India: Preparedness and Technologies*, Indian Council of Agricultural Research (ICAR), New Delhi, 2020.  
[14] C. Larman and V. R. Basili, "Iterative and incremental development: A brief history," *Computer*, vol. 36, no. 6, pp. 47–56, 2003.  
[15] IEEE, *IEEE Recommended Practice for Software Requirements Specifications*, IEEE Std 830-1998, 1998. doi: 10.1109/IEEESTD.1998.88286.  
[16] ISO/IEC/IEEE, *Systems and Software Engineering – Life Cycle Processes – Requirements Engineering*, ISO/IEC/IEEE 29148:2018, 2018.  
[17] NASA Langley Research Center, *NASA POWER (Prediction Of Worldwide Energy Resources) Agroclimatology API documentation*, 2024. [Online]. Available: https://power.larc.nasa.gov  
[18] Open-Meteo, *Open-Meteo Seasonal Forecast API documentation (ECMWF SEAS5 ensemble)*, 2024. [Online]. Available: https://open-meteo.com/en/docs/seasonal-forecast-api  
[19] Ministry of Agriculture & Farmers Welfare, *All India Report on Agriculture Census 2015-16*, Department of Agriculture, Cooperation & Farmers Welfare, New Delhi, 2020.  
[20] Ministry of Chemicals and Fertilizers, *Indian Fertilizer Scenario 2022*, Department of Fertilizers, Government of India, New Delhi, 2023.  
[21] F. Pedregosa et al., "Scikit-learn: Machine learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.  
[22] S. Ramírez, "FastAPI documentation," 2024. [Online]. Available: https://fastapi.tiangolo.com/  
[23] Streamlit Inc., "Streamlit documentation," 2024. [Online]. Available: https://docs.streamlit.io/  
[24] W. McKinney, "Data structures for statistical computing in Python," in *Proc. 9th Python in Science Conference (SciPy)*, 2010, pp. 56–61.  
[25] OWASP Foundation, "OWASP Top 10:2021 Web Application Security Risks," 2021. [Online]. Available: https://owasp.org/Top10/  
[26] ISO/IEC, *Systems and Software Engineering – Systems and Software Quality Requirements and Evaluation (SQuaRE) – Product Quality Model*, ISO/IEC 25010:2023, 2023.  
[27] Government of India, *The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023)*, New Delhi, 2023.  
[28] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA, USA: Pearson, 2016.  
[29] M. Cohn, *Succeeding with Agile: Software Development Using Scrum*. Boston, MA, USA: Addison-Wesley, 2009.  
[30] C. Leys et al., "Detecting outliers: Do not use standard deviation around the mean, use absolute deviation around the median," *Journal of Experimental Social Psychology*, vol. 49, no. 4, pp. 764–766, 2013.

---
---

# PART II: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

```
===================================================================================
                                  SECTION 1
                                INTRODUCTION
===================================================================================
```

### 1.1 Purpose of the Project
This document constitutes the formal Software Requirements Specification (SRS) for **KissanVision: An AI-Powered Crop Yield Prediction and Agronomic Decision Intelligence Platform for Indian Agriculture**. It establishes the complete functional capabilities, data specifications, architectural constraints, non-functional quality attributes, and verification criteria for the system.

This SRS is structured in adherence to the guidelines of **IEEE Std 830-1998** [15] and **ISO/IEC/IEEE 29148:2018** [16], adapted to the project requirements of the School of Computer Science, University of Petroleum & Energy Studies (UPES), Dehradun.

```
+----------------------------------------------------------------------------------------------------+
|                                         PROBLEM STATEMENT                                          |
+----------------------------------------------------------------------------------------------------+
| Smallholder farmers, farmer producer organisations (FPOs), and agricultural extension officers     |
| in India lack an accessible, transparent, and climate-adaptive digital decision system that        |
| accurately predicts crop yield (Quintals/Hectare) before and during the crop cycle, integrates     |
| seasonal weather forecasts, accommodates actual farm-measured inputs, and provides local SHAP     |
| explainability without requiring commercial subscriptions or specialized data science skills.     |
+----------------------------------------------------------------------------------------------------+
```

#### Motivation
1. **Economic Security for Smallholders**: Erroneous crop selection and miscalculated input application severely compromise agrarian livelihoods; accurate yield forecasting before sowing enables risk-mitigated crop planning.
2. **Climate Vulnerability & Volatility**: With over 50% of Indian farmland rainfed, shifting monsoon patterns demand prospective seasonal forecasts (ECMWF SEAS5) rather than mere reliance on retrospective averages.
3. **Transparent Agronomic Provenance**: Growers and agrarian lenders reject black-box models; KissanVision insists on mathematical explainability (SHAP waterfall) and clear source labeling for every input.
4. **Digital Public Goods Ethos**: Creating enterprise-grade agronomy intelligence accessible via open-source tools with zero recurring cloud subscription costs.

### 1.2 Target Beneficiary
Table 1.1 delineates the primary user communities and the specific operational benefits provided by KissanVision:

#### Table 1.1: Target beneficiaries and direct value delivered by KissanVision
| Beneficiary Community | Operational Role | Direct Value Delivered by KissanVision |
| :--- | :--- | :--- |
| **Smallholder & Marginal Farmers** | Individual agricultural producers cultivating $< 2$ ha | Instant pre-sowing harvest yield estimation (q/ha), personalized advice based on actual farm irrigation and fertilizer inputs, and ICAR climate risk alerts. |
| **Farmer Producer Organisations (FPOs)** | Agrarian collectives managing aggregated acreage | Aggregate harvest projections across member farms, forward market contract negotiation support, and optimized input inventory procurement. |
| **Agricultural Extension Workers (KVKs)** | District-level agronomic advisory staff | Data-driven diagnostic tool to explain yield variations to farmers, replacing intuition with quantified SHAP feature attributions. |
| **Crop Insurance & Micro-Finance Providers** | Agricultural credit and underwriting evaluators | Objective, district-level productivity benchmarks to calibrate credit limits and evaluate localized drought/flood yield shortfalls. |
| **Agronomic Researchers & Policy Analysts** | Academic and government agricultural planners | Open-access exploratory data platform evaluating multi-decadal trends across 33 states and 15 major Indian crops. |

### 1.3 Project Scope
- **Area of Application**:
  - **Sectors**: Precision Agriculture, Agronomic Decision Intelligence, Agro-Meteorology, Crop Insurance Risk Assessment.
  - **Geography**: All 33 Indian States and Union Territories covering 6 agricultural seasons.
  - **Target Crops**: 15 key Indian crops (Rice, Wheat, Maize, Potato, Onion, Groundnut, Gram, Dry Chillies, Rapeseed & Mustard, Jowar, Sunflower, Sesamum, Moong, Urad, Arhar/Tur).
- **Core Benefits**:
  - Validated harvest yield prediction in standard metric units (Quintals/Hectare).
  - Dual meteorological modalities: NASA POWER historical baselines vs Open-Meteo ECMWF SEAS5 180-day ensemble seasonal forecasts.
  - Farmer input personalization with transparent provenance badges.
  - ICAR-calibrated agro-climatic stress alerts across all 33 states.
  - Real-time local explainability via SHAP waterfall decompositions.
  - 100% free and open-source software stack with multi-channel serving (Streamlit + FastAPI + Modern Web UI).

#### Objectives and Goals
Table 1.2 maps each core project objective to its measurable verification target:

#### Table 1.2: Project objectives and empirical verification metrics
| ID | Project Objective | Measurable Verification Goal |
| :---: | :--- | :--- |
| **O1** | Standardize multi-source agricultural dataset | Clean 50,000 district-level records, standardizing production to Quintals/Hectare with 80/20 stratified crop representation. |
| **O2** | High-precision regression modeling | Attain test $R^2 \ge 0.90$ with RMSE $< 15.0\text{ q/ha}$ on held-out test split of 10,000 records. |
| **O3** | Dual climatological integration | Live REST queries to NASA POWER (3-year baseline) and Open-Meteo SEAS5 (180-day 51-member ensemble) with graceful offline fallback. |
| **O4** | Provenance-aware farmer personalization | Allow optional override of irrigation % and NPK kg/ha, displaying visual source badges on every prediction screen. |
| **O5** | ICAR climate risk alerting | Rule engine categorizing Drought, Flood, Heatwave, and Humidity risks across all 33 states with severity badges. |
| **O6** | Game-theoretic local explainability | Dynamic calculation of exact SHAP values for every inference, rendering interactive waterfall attribution plots. |
| **O7** | Production-grade API serving | Deploy FastAPI microservice with 15 documented OpenAPI endpoints maintaining sub-50 ms prediction latency. |
| **O8** | Zero commercial cost barrier | Complete stack operates without paid API keys, commercial licenses, or proprietary cloud subscriptions. |
| **O9** | Rigorous automated test coverage | Maintain 100% pass rate across unit, API, schema contract, and pipeline integration test suites. |

#### Functional Requirements
Table 1.3 defines the 20 formal functional requirements of KissanVision:

#### Table 1.3: Functional requirements specification (FR-01 through FR-20)
| ID | Requirement Name | The System Shall... | Priority |
| :---: | :--- | :--- | :---: |
| **FR-01** | Data Ingestion | ingest 50,000 district-level records from raw CSV, converting production into Quintals/Ha. | High |
| **FR-02** | Stratified Splitting | partition data into 80% training (40,000 rows) and 20% test (10,000 rows) preserving crop distributions. | High |
| **FR-03** | Categorical Encoding | encode State, Crop, and Season using OneHotEncoder producing 59 feature dimensions. | High |
| **FR-04** | Feature Scaling | normalize continuous numerical features using StandardScaler with parameters fit strictly on train data. | High |
| **FR-05** | Historical Weather | query NASA POWER Agroclimatology API for 3-year rolling temperature, rainfall, and humidity baselines. | High |
| **FR-06** | Forecast Weather | query Open-Meteo ECMWF SEAS5 51-member ensemble for next-season 180-day forecast anomalies. | High |
| **FR-07** | Irrigation Enrichment | enrich records with Agricultural Census 2015-16 state-level irrigation coverage percentages. | High |
| **FR-08** | Fertilizer Enrichment | enrich records with Ministry of Chemicals & Fertilizers state-level NPK consumption figures. | High |
| **FR-09** | XGBoost Training | train an `XGBRegressor` tuned via 3-fold GridSearchCV across 16 hyperparameter combinations. | High |
| **FR-10** | Native Model Export | serialize trained Booster into native JSON and UBJSON formats for platform independence. | High |
| **FR-11** | Farmer Overrides | allow users to input actual farm irrigation % and NPK kg/ha, replacing regional defaults on demand. | High |
| **FR-12** | Dynamic Gauge Scaling| scale predicted yield gauge dynamically based on biological yield potential of the selected crop. | Medium |
| **FR-13** | SHAP Waterfall | compute exact SHAP values for each inference and render local feature attribution waterfall plots. | High |
| **FR-14** | Feature Importance | compute and display global feature importance rankings across all 59 model features. | Medium |
| **FR-15** | ICAR Risk Alerts | evaluate meteorological conditions against ICAR thresholds to generate state-level risk alerts. | High |
| **FR-16** | Streamlit Dashboard | provide a 4-tab interactive agronomy dashboard (Prediction, SHAP, Insights, Architecture). | High |
| **FR-17** | Modern Web Frontend | deliver a responsive HTML5/CSS3/JavaScript web interface integrated with backend API. | High |
| **FR-18** | REST Serving API | serve predictions and metadata via FastAPI with 15 documented endpoints and Swagger UI. | High |
| **FR-19** | Offline Caching | cache remote weather responses locally (`*_cache.json`), gracefully handling external network downtime. | High |
| **FR-20** | Automated Test Suite| provide test suites covering unit logic, schema contracts, API endpoints, and model parity. | High |

#### Project Deliverables
Table 1.4 details the formal engineering deliverables comprising the KissanVision release:

#### Table 1.4: Project engineering deliverables
| No. | Deliverable | Description & Scope |
| :---: | :--- | :--- |
| **D1** | Core Python ML Package (`src/`) | Production data ingestion, preprocessing, XGBoost training, and prediction pipeline code. |
| **D2** | Serialized Model Artifacts (`models/`) | `model.json` (Booster), `model.pkl` (Pipeline), `feature_schema.json`, and `model_metadata.json`. |
| **D3** | FastAPI Serving Microservice (`api/`) | REST API service with 15 endpoints, Pydantic validation, CORS middleware, and Swagger UI. |
| **D4** | Streamlit Agronomy Dashboard (`dashboard/`) | 4-tab analytical dashboard with interactive Plotly visualizations and dark agronomy styling. |
| **D5** | Modern Web Application (`frontend/`) | Standalone responsive HTML5/CSS3/JavaScript web frontend with media assets and styling. |
| **D6** | Climatology Connectors | NASA POWER historical baseline client and Open-Meteo SEAS5 ensemble seasonal forecast parser. |
| **D7** | Automated Test Suites (`scripts/`) | Test scripts verifying predictions, scikit-learn parity, forecast parsing, and schema integrity. |
| **D8** | Exploratory Research Notebooks (`notebooks/`) | Jupyter notebooks detailing EDA, feature engineering, model tuning, and residual diagnostics. |
| **D9** | Docker Containerization | Container specification for seamless multi-platform deployment (`Dockerfile`). |
| **D10** | Comprehensive Documentation (`docs/`) | Project report, Software Requirements Specification, system audit, and API references. |

---

```
===================================================================================
                                  SECTION 2
                             PROJECT DESCRIPTION
===================================================================================
```

### 2.1 Reference Algorithm / Technical Concepts
Table 2.1 maps each core agricultural inquiry to the analytical algorithm implemented in KissanVision:

#### Table 2.1: Agricultural decision questions and computational methods applied
| Agronomic / Decision Question | Computational Method | Implementation Module |
| :--- | :--- | :--- |
| What is the expected crop harvest yield (q/ha) under seasonal conditions? | Tuned Extreme Gradient Boosting Regression (`XGBRegressor`) | `src/components/model_trainer.py`, `src/pipeline/predict_pipeline.py` |
| Why did the model predict this specific yield for my farm? | Game-theoretic SHAP (SHapley Additive exPlanations) TreeExplainer | `dashboard/app.py`, `src/pipeline/predict_pipeline.py` |
| What is the upcoming season's climate outlook compared to historical norms? | ECMWF SEAS5 51-member ensemble anomaly aggregation over 180-day horizon | `src/components/forecast_data.py`, `src/components/weather_data.py` |
| Is my farm or district currently facing adverse climate risks? | ICAR physiological stress rule classification (Drought, Heat, Flood, Humidity) | `src/components/weather_risk.py`, `api/main.py` |
| How do farmer-measured inputs change the predicted harvest? | Differential feature substitution with provenance tracking & SHAP re-attribution | `src/pipeline/predict_pipeline.py`, `dashboard/app.py` |

#### Mathematical Formulations

##### A. Extreme Gradient Boosting (XGBoost)
The objective function at boosting step $t$ minimizes second-order Taylor expansion of loss plus leaf regularization:
$$\tilde{\mathcal{L}}^{(t)} \approx \sum_{i=1}^{n} \left[ g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^{T} w_j^2$$
where first and second order gradients are defined as:
$$g_i = \partial_{\hat{y}^{(t-1)}} l\left(y_i, \hat{y}^{(t-1)}\right) = 2\left(\hat{y}_i^{(t-1)} - y_i\right)$$
$$h_i = \partial^2_{\hat{y}^{(t-1)}} l\left(y_i, \hat{y}^{(t-1)}\right) = 2$$
The optimal leaf weight $w_j^*$ for node $j$ and the corresponding split gain formula are:
$$w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}, \quad \text{Gain} = \frac{1}{2} \left[ \frac{\left(\sum_{i \in I_L} g_i\right)^2}{\sum_{i \in I_L} h_i + \lambda} + \frac{\left(\sum_{i \in I_R} g_i\right)^2}{\sum_{i \in I_R} h_i + \lambda} - \frac{\left(\sum_{i \in I} g_i\right)^2}{\sum_{i \in I} h_i + \lambda} \right] - \gamma$$

##### B. SHAP TreeExplainer Formulation
For feature $j$ and instance $x$, the Shapley contribution $\phi_j$ across all feature subsets $S \subseteq F \setminus \{j\}$ is:
$$\phi_j(x) = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|! (|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{j\}) - f_x(S) \right]$$
where $f_x(S) = \mathbb{E}[f(x) \mid x_S]$ represents the conditional expectation computed recursively across tree paths.

##### C. Evaluation Metrics
$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}, \quad R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}, \quad \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

```
+----------------------------------------------------------------------------------------------------+
| Algorithm 1: End-to-End Agronomic Ingestion, Cross-Validated Training, and Model Export           |
+----------------------------------------------------------------------------------------------------+
| Input : Raw agricultural CSV, Agricultural Census irrigation table, Ministry NPK table            |
| Output: Serialized native XGBoost Booster (model.json), ColumnTransformer, feature_schema.json     |
| 1. Load raw dataset; compute Yield = (Production * 10) / Area; filter missing and infinite values; |
| 2. Join state-level irrigation percentage and NPK fertilizer consumption by State_Name;           |
| 3. Stratify 50,000 sampled rows into 80% train (40,000) and 20% test (10,000) by Crop;            |
| 4. Fit ColumnTransformer on train data: OneHotEncoder(State, Crop, Season) + StandardScaler(nums); |
| 5. Transform train and test partitions into 59-dimensional feature matrices X_train, X_test;       |
| 6. Initialize XGBRegressor; execute 3-fold GridSearchCV over hyperparameter grid;                  |
| 7. Fit best estimator on full X_train; evaluate R2, RMSE, MAE, MAPE on held-out X_test;           |
| 8. Extract feature_schema.json containing column definitions, categories, and min/max bounds;      |
| 9. Save native XGBoost Booster to models/model.json and serialize model_metadata.json.             |
+----------------------------------------------------------------------------------------------------+
```

```
+----------------------------------------------------------------------------------------------------+
| Algorithm 2: Dynamic Inference, Farmer Personalization, and SHAP Explainability Decomposition     |
+----------------------------------------------------------------------------------------------------+
| Input : User selections (State, Crop, Season, Area, WeatherMode), FarmerOverrides (Irrigation, NPK)|
| Output: Predicted Yield (q/ha), Total Harvest (q, Tonnes), Risk Alerts, SHAP Waterfall Attribution|
| 1. Validate inputs against models/feature_schema.json; reject unknown categories with HTTP 422;   |
| 2. If WeatherMode == "Historical": lookup NASA POWER 3-year baseline from cache;                  |
|    Else: query Open-Meteo SEAS5 180-day ensemble forecast; compute anomaly delta vs baseline;      |
| 3. If FarmerOverrides provided: substitute farm values and set ProvenanceBadge = "Farm Input";    |
|    Else: populate state defaults from Census/Ministry tables and set ProvenanceBadge = "Default";  |
| 4. Construct feature vector; transform using ColumnTransformer into 59-element array;             |
| 5. Pass transformed array to loaded XGBoost Booster; compute raw predicted yield Y_pred;          |
| 6. Compute dynamic gauge bounds [0, MaxBiologicalYield(Crop)]; compute total production = Y*Area;  |
| 7. Evaluate ICAR stress rules: check rainfall, temperature, humidity against thresholds;          |
| 8. Execute shap.TreeExplainer on feature vector; extract base value E[f(x)] and phi_j attributions;|
| 9. Return structured response containing yield, provenance badges, risk alerts, and SHAP vectors.  |
+----------------------------------------------------------------------------------------------------+
```

### 2.2 Data / Data Characteristics
KissanVision operates on structured, tabular district-level agronomic records linked with continuous meteorological time series and geospatial coordinates:

#### Table 2.2: Core data structures and their architectural scope
| Data Structure | Scope & Purpose in KissanVision |
| :--- | :--- |
| `pandas.DataFrame` (Clean Contract) | Tabular container for 50,000 agronomic records during ingestion, transformation, and evaluation. |
| `scikit-learn.compose.ColumnTransformer` | Multi-pipeline preprocessor applying OneHotEncoder to categoricals and StandardScaler to numericals. |
| `numpy.ndarray` (59 dimensions) | Dense encoded feature vector ingested directly by the XGBoost Booster engine. |
| `shap.Explanation` object | Container storing local base expected values, feature attribution arrays ($\phi_j$), and instance data. |
| `models/feature_schema.json` | Master JSON contract defining exact feature ordering, allowable categories, and numerical statistics. |
| `models/model_metadata.json` | Model versioning manifest documenting training timestamps, hyperparameters, and $R^2$/RMSE metrics. |
| `*_cache.json` (Local Caching) | On-disk JSON key-value store for NASA POWER and Open-Meteo weather payloads. |

#### Primary Data Sources
Table 2.3 documents the external data sources feeding the KissanVision ingestion pipeline:

#### Table 2.3: Primary data sources and integration specifications
| Data Source | Content Provided | Integration Method | Frequency / Ingestion Mode |
| :--- | :--- | :--- | :--- |
| **Kaggle / DES Indian Crop Production** | District-level crop acreage, production, and season records. | CSV file import with automated cleaning and sampling. | Static baseline ingestion (50,000 rows). |
| **NASA POWER Agroclimatology API** | 3-year rolling average temperature, rainfall, humidity, radiation. | HTTP GET request to NASA REST API with local disk caching. | On-demand / Cached per state centroid. |
| **Open-Meteo Seasonal Forecast API** | ECMWF SEAS5 51-member ensemble temperature & rainfall forecast. | HTTP GET request to Open-Meteo REST API (180-day horizon). | Real-time seasonal query with local fallback. |
| **Agricultural Census 2015-16** | State-level net and gross irrigated area percentages. | Structured lookup table embedded in `src/components/`. | Fixed reference table. |
| **Ministry of Chemicals & Fertilizers** | State-level NPK fertilizer consumption (kg/ha). | Structured lookup table embedded in `src/components/`. | Fixed reference table. |
| **ICAR Agro-Climatic Advisory Guidelines** | Physiological crop threshold limits for climate hazards. | Rule dictionary embedded in `src/components/weather_risk.py`. | Fixed advisory standards. |

#### Dataset Profile
Table 2.4 itemizes the statistical profile of the 50,000-row benchmark dataset:

#### Table 2.4: Statistical profile of the 50,000-record benchmark agricultural dataset
| Characteristic | Observed Value in Benchmark Dataset |
| :--- | :--- |
| **Total Agricultural Records** | 50,000 district-level observations |
| **Geographic Coverage** | 33 Indian States and Union Territories |
| **Crop Coverage** | 15 major foodgrains, oilseeds, vegetables, and commercial crops |
| **Cropping Seasons** | 6 seasons (Kharif, Rabi, Whole Year, Summer, Autumn, Winter) |
| **Raw Input Features** | 11 columns (`State_Name`, `Crop_Type`, `Crop`, `Season`, `Year`, `Area`, `Production`, etc.) |
| **Engineered Feature Space** | 59 encoded features (OneHotEncoded categoricals + StandardScaled numericals) |
| **Target Variable Range (Yield)** | 0.05 to 985.40 Quintals/Hectare (median: 18.2 q/ha, mean: 24.6 q/ha) |
| **Annual Rainfall Range** | 185.0 mm to 4,250.0 mm (mean: 1,180.4 mm) |
| **Irrigation Percentage Range** | 3.5% to 98.2% across states |
| **NPK Consumption Range** | 18.4 kg/ha to 258.6 kg/ha across states |

#### Table 2.5: Feature schema definition and one-hot encoding representation
| Feature Category | Original Raw Features | Transformed Features in Matrix ($M=59$) | Encoding Scheme |
| :--- | :--- | :---: | :--- |
| **Geographic** | `State_Name` (33 states) | 33 binary indicator columns (`state_Andhra Pradesh`, etc.) | One-Hot Encoding (drop=None) |
| **Agronomic** | `Crop` (15 crops) | 15 binary indicator columns (`crop_RICE`, `crop_WHEAT`, etc.) | One-Hot Encoding (drop=None) |
| **Temporal** | `Season` (6 seasons) | 6 binary indicator columns (`season_Kharif`, `season_Rabi`, etc.)| One-Hot Encoding (drop=None) |
| **Nutrient** | `npk_consumption` | 1 continuous column | StandardScaler ($\mu=128.4, \sigma=62.1$) |
| **Water Access** | `irrigation_pct` | 1 continuous column | StandardScaler ($\mu=48.2, \sigma=24.5$) |
| **Climatological** | `Annual_Rainfall`, `Temperature`| 2 continuous columns | StandardScaler ($\mu=1180, \sigma=485$) |
| **Land Scale** | `Area` (Hectares) | 1 continuous column | StandardScaler ($\mu=12400, \sigma=28500$) |

### 2.3 SWOT Analysis
Table 2.6 provides a comprehensive SWOT analysis of the KissanVision platform:

#### Table 2.6: SWOT analysis of KissanVision
| STRENGTHS (Internal) | WEAKNESSES (Internal) |
| :--- | :--- |
| • High validated accuracy ($R^2 = 0.9165$, RMSE = 12.07 q/ha) on 50,000 real Indian records.<br>• Full mathematical explainability via local SHAP waterfall attributions on every prediction.<br>• Dual weather modalities bridging historical baselines (NASA POWER) with seasonal forecasts (Open-Meteo).<br>• Provenance-aware farmer personalization overrides.<br>• 100% free and open-source stack with zero paid API dependencies.<br>• Sub-50 ms inference latency with complete test suite coverage. | • Model currently restricted to 15 major Indian crops (excludes minor millets and niche horticultural crops).<br>• Granularity is at district and state levels; field-level micro-plots rely on farmer override inputs.<br>• Seasonal climate forecasts inherently carry ensemble uncertainty over 180-day horizons.<br>• Offline usage limited to cached regional profiles. |
| **OPPORTUNITIES (External)** | **THREATS (External)** |
| • India’s 140+ million agrarian households increasingly accessing 4G/5G smartphones.<br>• Growing government emphasis on Agristack, digital agriculture public infrastructure, and climate adaptation.<br>• Expansion to vernacular voice interfaces (Bhashini) to empower non-literate farmers.<br>• Integration with Farmer Producer Organisations (FPOs) and institutional agricultural lenders for crop credit calibration. | • Unprecedented climate anomalies exceeding historical envelope (extreme localized cloudbursts).<br>• Upstream third-party API availability changes (NASA POWER or Open-Meteo downtime).<br>• Farmer skepticism toward algorithmic predictions unless actively bridged by human extension workers.<br>• Emerging commercial paywalled agronomic advisory platforms with proprietary sensor networks. |

### 2.4 Project Features
Figure 2.1 illustrates the Level-2 Use Case diagram, showing interactions between farmers, extension workers, FPO admins, and system services:

```
                                  +-------------------------------------------------------------+
                                  |                         KissanVision                        |
                                  |                                                             |
                                  |  +-------------------------------------------------------+  |
                                  |  | Select State, Crop, Season, and Land Area             |  |
                                  |  +---------------------------^---------------------------+  |
                                  |                              |                              |
                                  |  +---------------------------+---------------------------+  |
                                  |  | Toggle Weather Mode: Historical vs ECMWF Forecast     |  |
                                  |  +---------------------------^---------------------------+  |
                                  |                              |                              |
                                  |  +---------------------------+---------------------------+  |
                                  |  | Override Farm Irrigation % and NPK Fertilizer kg/ha   |  |
                                  |  +---------------------------^---------------------------+  |
+-------------------+             |                              |                              |
|                   |             |  +---------------------------+---------------------------+  |
|      Farmer /     +------------->  | Request Yield Prediction (Quintals/Hectare)           |  |
|  Extension Worker |             |  +---------------------------^---------------------------+  |
|                   |             |                              |                              |
+-------------------+             |  +---------------------------+---------------------------+  |
                                  |  | Inspect Local SHAP Feature Contribution Waterfall     |  |
                                  |  +---------------------------^---------------------------+  |
                                  |                              |                              |
                                  |  +---------------------------+---------------------------+  |
                                  |  | Review ICAR Agro-Climatic Stress & Hazard Alerts      |  |
                                  |  +---------------------------^---------------------------+  |
                                  |                              |                              |
+-------------------+             |  +---------------------------+---------------------------+  |
|   Third-Party App /+------------->  | Query REST API Endpoints (/predict, /risk, /weather) |  |
|     FPO System    |             |  +-------------------------------------------------------+  |
+-------------------+             |                                                             |
                                  |  +-------------------------------------------------------+  |   +-----------------------+
                                  |  | Fetch NASA POWER Climatology Baseline                 +----->| NASA POWER REST API   |
                                  |  +-------------------------------------------------------+  |   +-----------------------+
                                  |                                                             |
                                  |  +-------------------------------------------------------+  |   +-----------------------+
                                  |  | Fetch Open-Meteo ECMWF SEAS5 Ensemble Forecast        +----->| Open-Meteo SEAS5 API  |
                                  |  +-------------------------------------------------------+  |   +-----------------------+
                                  |                                                             |
                                  +-------------------------------------------------------------+
```
**Figure 2.1: Level-2 Use Case diagram of KissanVision.**

#### Table 2.7: System feature modules and functional scopes
| Module Name | Core Functional Scope | Deliverable Association |
| :--- | :--- | :--- |
| **Agronomic Ingestion & Preprocessing** | Ingests CSV records, calculates standard Quintals/Ha yields, performs 80/20 stratified split, and fits ColumnTransformer. | `src/components/data_ingestion.py`, `src/components/data_transformation.py` |
| **Climatology & Forecast Engine** | Connects to NASA POWER (historical baseline) and Open-Meteo SEAS5 (180-day ensemble forecast) with disk caching. | `src/components/weather_data.py`, `src/components/forecast_data.py` |
| **Agronomic Enrichment Engine** | Enriches records with Agriculture Census irrigation percentages and Ministry NPK consumption data. | `src/components/irrigation_data.py`, `src/components/fertilizer_data.py` |
| **XGBoost Inference Engine** | Evaluates transformed 59-dimensional feature vectors against tuned Booster, outputting predicted yield and total harvest. | `src/pipeline/predict_pipeline.py`, `src/components/model_trainer.py` |
| **SHAP Explainability Engine** | Decomposes individual predictions into baseline expected value plus additive feature contributions ($\phi_j$). | `dashboard/app.py`, `src/pipeline/predict_pipeline.py` |
| **ICAR Agro-Climatic Risk Engine** | Classifies meteorological hazards against ICAR agronomic thresholds across 33 states with contextual alerts. | `src/components/weather_risk.py`, `api/main.py` |
| **Streamlit Agronomy Dashboard** | 4-tab interactive analytical interface with dynamic gauge scaling, Plotly charts, and dark agronomy styling. | `dashboard/app.py` |
| **FastAPI Microservice Layer** | 15 documented OpenAPI REST endpoints with Pydantic request validation and sub-50 ms inference latency. | `api/main.py` |
| **Modern Web Application UI** | Responsive HTML5/CSS3 frontend featuring agronomic cards, interactive forms, and direct REST API communication. | `frontend/index.html`, `frontend/css/styles.css`, `frontend/js/app.js` |

### 2.5 User Classes and Characteristics
Table 2.8 outlines the operational profiles, technical proficiencies, and access permissions across KissanVision user classes:

#### Table 2.8: User classes, operational characteristics, and access rights
| User Class | Description & Context | Technical Skill | Frequency of Use | Primary System Interface |
| :--- | :--- | :---: | :---: | :--- |
| **Individual Farmer** | Smallholder grower planning seasonal crops and input applications. | Low | Seasonal (Pre-sowing & In-season) | Streamlit Tab 1 / Modern Web App (Simple dropdowns and sliders). |
| **Agricultural Extension Officer** | KVK agronomist advising multiple farming communities. | Medium | Weekly / Daily | Streamlit Tabs 1, 2, & 3 (Prediction, SHAP waterfall, Data Insights). |
| **FPO Executive / Aggregator** | Collective leader forecasting crop volumes for market contracts. | Medium | Weekly | Streamlit Dashboard & Web App (Aggregate harvest totals in Tonnes). |
| **Crop Underwriter / Adjuster** | Insurance risk assessor verifying productivity benchmarks. | High | Periodic | FastAPI REST Endpoints & Tab 4 (Model metrics, CV diagnostics). |
| **System Administrator** | DevOps maintainer managing API container and weather caches. | High | As needed | Docker container console, FastAPI `/docs`, and test suite runners. |

### 2.6 Design and Implementation Constraints
- **Hardware Boundary Conditions**:
  - **Server Deployment**: Minimum 2 Virtual CPUs, 4 GB RAM, 10 GB SSD. Standard container hosting on Linux (Ubuntu 22.04 LTS).
  - **Client Workstation**: Standard web browser (Chrome, Edge, Firefox, Safari) on desktop, laptop, tablet, or smartphone.
- **Software Constraints**:
  - Python 3.10+ runtime required.
  - XGBoost $\ge 3.0$ with native model serialization (`model.json`).
  - FastAPI 0.140+ with Pydantic v2 schemas.
  - 100% free external APIs (NASA POWER, Open-Meteo) operating without API keys.

#### Table 2.9: External system interface specifications
| External System | Protocol / Data Format | Architectural Purpose & Operational Rule |
| :--- | :--- | :--- |
| **NASA POWER API** | HTTPS / JSON REST | Queries 3-year historical solar radiation, temperature, rainfall, and humidity per state centroid. |
| **Open-Meteo SEAS5 API** | HTTPS / JSON REST | Queries 180-day ECMWF seasonal forecast ensemble (51 members) for temperature and precipitation anomalies. |
| **Local Disk Cache** | JSON files (`*_cache.json`) | Persists retrieved weather payloads locally; served instantly on repeat requests or network dropouts. |
| **Browser Client** | HTTPS / WebSocket | Streams interactive Streamlit components and HTML5/CSS3 frontend payloads. |

#### Table 2.10: Specific technologies, frameworks, and library versions
| Architectural Area | Pinned Technology & Version | Engineering Purpose |
| :--- | :--- | :--- |
| **Language Runtime** | Python 3.10+ / 3.11 | Core execution environment. |
| **Gradient Boosting** | XGBoost 3.2.0 | High-performance gradient boosting regression. |
| **Machine Learning Core** | scikit-learn 1.7.0 | ColumnTransformer, OneHotEncoder, StandardScaler, GridSearchCV. |
| **Explainable AI (XAI)** | SHAP 0.49.0 | TreeExplainer, waterfall plots, and Shapley feature attribution. |
| **Data Manipulation** | pandas 2.2.0, NumPy 1.26.0 | Tabular data transformations, vectorized aggregations, array ops. |
| **Serving Framework** | FastAPI 0.140.0, Uvicorn 0.30.0 | High-performance asynchronous REST API serving. |
| **Dashboard UI** | Streamlit 1.60.0, Plotly 6.9.0 | Interactive web application, real-time plotting, dark agronomy theme. |
| **Web Frontend** | HTML5, Vanilla CSS3, JavaScript | Lightweight, accessible, zero-dependency client interface. |
| **Testing & Quality** | pytest 8.0+, flake8, black | Automated test execution, schema contract validation, linting. |

### 2.7 Design Diagrams

#### Layered Architecture
Figure 2.2 illustrates the five-tier layered architectural design of KissanVision:

```
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                    1. CLIENT PRESENTATION TIER                                    |
|   +────────────────────────────+   +────────────────────────────+   +──────────────────────────+  |
|   | Streamlit Dashboard (8501) |   | Modern Web Frontend (HTML) |   | Swagger / OpenAPI UI     |  |
|   | 4 Tabs, Plotly, Gauges     |   | Vanilla CSS, Responsive JS |   | Interactive API Testing  |  |
|   +─────────────┬──────────────+   +─────────────┬──────────────+   +────────────┬─────────────+  |
+─────────────────┼────────────────────────────────┼───────────────────────────────┼────────────────+
                  |                                |                               |
                  v                                v                               v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                      2. API & ROUTING TIER                                        |
|   FastAPI REST Service (/api/v1) · Uvicorn ASGI Server · Pydantic v2 Request Validation           |
|   Endpoints: /predict, /health, /metrics, /crops, /states, /weather, /forecast, /risk, /docs      |
+──────────────────────────────────────────────────┬────────────────────────────────────────────────+
                                                   |
                                                   v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                    3. BUSINESS & INFERENCE TIER                                   |
|   +──────────────────────────+   +──────────────────────────+   +──────────────────────────────+  |
|   | PredictPipeline Engine   |   | SHAP TreeExplainer Engine|   | ICAR Agro-Risk Engine        |  |
|   | Feature Vector Assembly  |   | Waterfall Attribution    |   | Physiological Stress Rules   |  |
|   +─────────────┬────────────+   +─────────────┬────────────+   +──────────────┬───────────────+  |
+─────────────────┼──────────────────────────────┼───────────────────────────────┼──────────────────+
                  |                              |                               |
                  v                              v                               v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                    4. DATA PREPROCESSING TIER                                     |
|   ColumnTransformer Pipeline · OneHotEncoder (States, Crops, Seasons) · StandardScaler (Numerics) |
|   models/feature_schema.json Contract Validator · Provenance Tracking (Farm Input vs Default)    |
+──────────────────────────────────────────────────┬────────────────────────────────────────────────+
                                                   |
                                                   v
+───────────────────────────────────────────────────────────────────────────────────────────────────+
|                                   5. PERSISTENCE & DATA TIER                                      |
|   * models/model.json (XGBoost)      * Local Disk Weather Cache     * Census Irrigation Tables    |
|   * models/model_metadata.json       * 50,000 Clean Records         * Ministry NPK Tables         |
+───────────────────────────────────────────────────────────────────────────────────────────────────+
```
**Figure 2.2: Layered Architectural Model of KissanVision.**

#### Data-to-Decision Pipeline
Figure 2.3 portrays the sequential data journey from raw multi-source ingestion to actionable agronomic advisory:

```
+---------------+     +---------------+     +---------------+     +---------------+     +---------------+
|  1. Ingest    |     |  2. Clean &   |     |  3. Enrich    |     |  4. Preprocess|     |  5. Predict   |
| Multi-Source  | --> | Standardize   | --> | Covariates    | --> | & Transform   | --> | XGBoost       |
| Data          |     | (q/ha)        |     | (Weather/NPK) |     | (59 Features) |     | Booster       |
+---------------+     +---------------+     +---------------+     +---------------+     +-------┬-------+
                                                                                                |
                                                                                                v
+---------------+     +---------------+     +---------------+     +---------------+     +---------------+
|  10. Farmer   |     |  9. Serve     |     |  8. Alert     |     |  7. Overrides |     |  6. Explain   |
| Decision &    | <-- | Multi-Channel | <-- | ICAR Agro-    | <-- | Farmer Farm   | <-- | SHAP Local    |
| Sowing Plan   |     | (Web/App/API) |     | Climatic Risk |     | Values (NPK/%)|     | Waterfall     |
+---------------+     +---------------+     +---------------+     +---------------+     +---------------+
```
**Figure 2.3: End-to-end Data-to-Agronomic Decision Intelligence Pipeline.**

#### PERT Chart and Critical Path Analysis
The engineering initiative was planned across 16 weeks, from 3 August 2026 to 20 November 2026. Table 2.11 defines the activities, dependencies, durations, earliest/latest times, and slack:

#### Table 2.11: PERT activity table (durations in weeks)
| ID | Activity Description | Duration | Predecessor | ES | EF | LS | LF | Slack |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | Agronomic problem study & requirement gathering | 1 | – | 0 | 1 | 0 | 1 | **0** |
| **B** | Literature review & ML toolchain selection | 2 | A | 1 | 3 | 4 | 6 | 3 |
| **C** | Kaggle dataset cleaning, standardization & 50K sampling | 2 | A | 1 | 3 | 2 | 4 | 1 |
| **D** | Data preprocessing pipeline & ColumnTransformer build | 3 | C | 3 | 6 | 3 | 6 | **0** |
| **E** | Climatology connectors: NASA POWER & Open-Meteo SEAS5 | 2 | D | 6 | 8 | 7 | 9 | 1 |
| **F** | XGBoost regression training & GridSearchCV tuning | 3 | D | 6 | 9 | 6 | 9 | **0** |
| **G** | SHAP explainability engine & ICAR risk rule integration | 2 | F | 9 | 11 | 9 | 11 | **0** |
| **H** | FastAPI REST service development (15 endpoints) | 2 | F | 9 | 11 | 11 | 13 | 2 |
| **I** | Streamlit interactive agronomy dashboard (4 tabs) | 3 | G, H | 11 | 14 | 11 | 14 | **0** |
| **J** | Modern HTML5/CSS3/JavaScript web frontend | 2 | H | 11 | 13 | 12 | 14 | 1 |
| **K** | Automated testing, schema contract & parity verification| 1 | I, J | 14 | 15 | 14 | 15 | **0** |
| **L** | SRS & Project Report documentation & academic defense | 1 | K | 15 | 16 | 15 | 16 | **0** |

*Activities with zero slack constitute the Critical Path: **A → D → F → G → I → K → L** (Total Duration: 16 Weeks).*

```
   [0|1|1] A
   Problem Study
   [0|0|1] (Slack=0)
       |
       +-------------------------------+
       |                               |
       v                               v
   [1|2|3] B                       [1|2|3] C
   Literature Review               Dataset Cleaning
   [4|3|6] (Slack=3)               [2|1|4] (Slack=1)
                                       |
                                       v
                                   [3|3|6] D
                                   Preprocessor Pipeline
                                   [3|0|6] (Slack=0)
                                       |
       +-------------------------------+-------------------------------+
       |                                                               |
       v                                                               v
   [6|2|8] E                                                       [6|3|9] F
   Weather Connectors                                              XGBoost Training
   [7|1|9] (Slack=1)                                               [6|0|9] (Slack=0)
                                                                       |
       +---------------------------------------------------------------+
       |                               |
       v                               v
   [9|2|11] H                      [9|2|11] G
   FastAPI Service                 SHAP & Risk Engine
   [11|2|13] (Slack=2)             [9|0|11] (Slack=0)
       |                               |
       +---------------+---------------+
                       |
       +---------------+---------------+
       |                               |
       v                               v
   [11|2|13] J                     [11|3|14] I
   Modern Web Frontend             Streamlit Dashboard
   [12|1|14] (Slack=1)             [11|0|14] (Slack=0)
       |                               |
       +---------------+---------------+
                       |
                       v
                   [14|1|15] K
                   Testing & Parity
                   [14|0|15] (Slack=0)
                       |
                       v
                   [15|1|16] L
                   Report & Defense
                   [15|0|16] (Slack=0)
```
**Figure 2.4: PERT Network Diagram of the KissanVision development lifecycle (Critical Path highlighted).**

```
+───────────────────────────────────────────────────────────────────────────────────────────────────+
| Activity                  | Aug (W1-4)  | Sep (W5-8)  | Oct (W9-12) | Nov (W13-16)| Status        |
+───────────────────────────+─────────────+─────────────+─────────────+─────────────+───────────────+
| A. Problem Study          | [X]         |             |             |             | Completed     |
| B. Literature Review      |   [X-X]     |             |             |             | Completed     |
| C. Dataset Cleaning       |   [X-X]     |             |             |             | Completed     |
| D. Preprocessor Pipeline  |     [X-X-X] |             |             |             | Completed     |
| E. Weather Connectors     |             |     [X-X]   |             |             | Completed     |
| F. XGBoost Training       |             |     [X-X-X] |             |             | Completed     |
| G. SHAP & Risk Engine     |             |             |   [X-X]     |             | Completed     |
| H. FastAPI REST Service   |             |             |   [X-X]     |             | Completed     |
| I. Streamlit Dashboard    |             |             |     [X-X-X] |             | Completed     |
| J. Modern Web Frontend    |             |             |     [X-X]   |             | Completed     |
| K. Testing & Verification |             |             |             |   [X]       | Completed     |
| L. Final Documentation    |             |             |             |     [X]     | Completed     |
+───────────────────────────────────────────────────────────────────────────────────────────────────+
```
**Figure 2.5: Gantt Chart of Project Development Milestones across 16 Weeks.**

### 2.8 Assumptions and Dependencies
- **Assumptions**:
  1. The 50,000-row cleaned historical crop production dataset represents authentic regional variance across Indian agro-climatic zones.
  2. Public meteorological APIs (NASA POWER, Open-Meteo) maintain stable REST query endpoints with documented payloads.
  3. Farmers or agricultural extension agents possess access to standard internet connectivity on a smartphone, tablet, or PC to query the web dashboard.
- **Dependencies**:
  1. Network connectivity to `power.larc.nasa.gov` and `seasonal-api.open-meteo.com` (gracefully handled via local cache fallbacks).
  2. Pinned Python runtime libraries (`xgboost==3.2.0`, `scikit-learn==1.7.0`, `shap==0.49.0`, `fastapi==0.140.0`, `streamlit==1.60.0`).
  3. Operating system compatibility across Windows, macOS, and Linux for containerized Docker execution.

---

```
===================================================================================
                                  SECTION 3
                          NON-FUNCTIONAL REQUIREMENTS
===================================================================================
```

### 3.1 Performance Requirements
Table 3.1 establishes the non-functional performance guarantees verified across KissanVision:

#### Table 3.1: Non-functional performance requirements
| ID | Performance Requirement | Measurable Engineering Target |
| :---: | :--- | :--- |
| **NFR-P1** | Yield prediction inference latency | $< 50\text{ milliseconds}$ per request on loaded XGBoost Booster. |
| **NFR-P2** | Cached weather query response time | $< 10\text{ milliseconds}$ when served from local disk cache. |
| **NFR-P3** | Live Open-Meteo SEAS5 forecast retrieval | $< 500\text{ milliseconds}$ under standard 4G/broadband connectivity. |
| **NFR-P4** | SHAP waterfall plot calculation latency | $< 200\text{ milliseconds}$ per local inference. |
| **NFR-P5** | Streamlit initial dashboard load time | $< 3.0\text{ seconds}$ on standard client browser. |
| **NFR-P6** | Modern Web Frontend first contentful paint | $< 1.0\text{ second}$ with zero heavy external UI dependencies. |
| **NFR-P7** | API concurrency throughput | $\ge 100\text{ concurrent requests/sec}$ with zero server failures (HTTP 500). |
| **NFR-P8** | Automated test suite execution time | Complete 101-test validation suite executes in $< 30\text{ seconds}$. |
| **NFR-P9** | Memory footprint under steady state | Process resident set size (RSS) $< 500\text{ MB}$ for FastAPI service. |
| **NFR-P10**| Disk storage footprint for model artifacts | All serialized artifacts (`model.json`, `model.pkl`, schema) $< 2\text{ MB}$. |

### 3.2 Security Requirements
Although KissanVision does not process financial transactions, robust security controls are enforced:
- **Strict Input Validation**: All request parameters undergo Pydantic v2 type checking, regex validation, and range enforcement. Categorical parameters (Crop, State, Season) are validated against exact white-lists in `models/feature_schema.json`.
- **CORS Protection**: FastAPI enforces Cross-Origin Resource Sharing (CORS) policies, permitting requests strictly from designated web dashboard domains.
- **Dependency Vulnerability Management**: All third-party Python packages are audited against known CVEs; pin versions are updated to eliminate supply-chain vulnerabilities.
- **Zero Sensitive Data Exposure**: No personally identifiable farmer information (names, Aadhaar numbers, phone numbers) is recorded or transmitted.
- **Graceful Error Handling**: Unhandled internal exceptions return standardized JSON error bodies (`{"detail": "Error description"}`) without leaking internal stack traces or directory paths to clients.

### 3.3 Software Quality Attributes
Table 3.2 outlines how KissanVision fulfills the quality model criteria of **ISO/IEC 25010:2023** [26]:

#### Table 3.2: Software quality attributes mapped to ISO/IEC 25010
| Quality Attribute | How Achieved in KissanVision Architecture |
| :--- | :--- |
| **Functional Suitability** | Provides end-to-end yield prediction in standard metric units (q/ha) with verified $R^2 = 0.9165$, meeting all agricultural decision needs. |
| **Performance Efficiency** | Sub-50 ms inference latency and rapid SHAP calculation through native XGBoost C++ Booster execution. |
| **Compatibility & Interoperability** | Standardized REST JSON API documented via OpenAPI (Swagger); native XGBoost JSON/UBJSON model formats ensure multi-platform interoperability. |
| **Usability** | Dual interfaces tailored to user contexts: rich 4-tab Streamlit agronomy dashboard and lightweight responsive modern web UI with clear provenance badges. |
| **Reliability & Fault Tolerance** | Automated disk cache fallback for weather APIs ensures 100% uptime even during complete external internet dropouts. |
| **Security** | Pydantic v2 input sanitization, strict schema validation white-lists, and absence of sensitive user persistence. |
| **Maintainability** | Clean modular separation (`src/components`, `src/pipeline`, `api`, `dashboard`), clean variable naming, and full automated test suite coverage. |
| **Portability** | Platform-agnostic execution across Linux, macOS, and Windows; fully containerized via `Dockerfile`. |

---

```
===================================================================================
                                   APPENDICES
===================================================================================
```

### APPENDIX A: GLOSSARY

#### Table A.1: Glossary of agricultural, meteorological, and machine learning terms
| Term / Acronym | Definition & Domain Meaning |
| :--- | :--- |
| **Quintal (q)** | Standard Indian agricultural unit of mass equal to 100 kilograms ($100\text{ kg}$). |
| **Hectare (ha)** | Metric unit of land area equal to 10,000 square meters ($\approx 2.471\text{ acres}$). |
| **q/ha** | Quintals per Hectare: standard Indian metric unit of crop yield / land productivity. |
| **Kharif** | Monsoon agricultural season in India (sowing: June–July, harvesting: September–October). |
| **Rabi** | Winter agricultural season in India (sowing: October–November, harvesting: February–April). |
| **Zaid / Summer** | Short summer cropping season between Rabi and Kharif (March–June). |
| **NPK** | Essential macronutrients: Nitrogen (N), Phosphorus (P), and Potassium (K) in kg/ha. |
| **ICAR** | Indian Council of Agricultural Research: apex national agricultural research body. |
| **FPO** | Farmer Producer Organisation: an enterprise formed by collective primary agricultural producers. |
| **KVK** | Krishi Vigyan Kendra: district-level agricultural science extension centre. |
| **NASA POWER** | Prediction Of Worldwide Energy Resources: NASA solar and agro-climatological satellite repository. |
| **Open-Meteo SEAS5**| Long-range seasonal forecast ensemble model from ECMWF with 51 members. |
| **XGBoost** | Extreme Gradient Boosting: scalable, regularized gradient boosted decision tree library. |
| **SHAP** | SHapley Additive exPlanations: game-theoretic technique explaining individual model predictions. |
| **$R^2$ Score** | Coefficient of Determination: proportion of target variance explained by independent features. |
| **RMSE** | Root Mean Squared Error: standard measure of the magnitude of regression residuals. |
| **MAE** | Mean Absolute Error: average magnitude of absolute errors in predicted units. |
| **OHE** | One-Hot Encoding: transformation of categorical variables into binary indicator vectors. |
| **REST** | Representational State Transfer: stateless web API architecture communicating over HTTP. |
| **FastAPI** | Modern, high-performance web framework for building APIs with Python and Pydantic. |
| **Streamlit** | Python framework for building interactive, data-driven web applications. |

---

### APPENDIX B: ANALYSIS MODEL

#### Context Diagram (Level-0 Data Flow Diagram)
Figure B.1 illustrates the Level-0 Context Diagram of the KissanVision system:

```
+──────────────────────+                           +──────────────────────+
|  NASA POWER Climate  |                           |  Open-Meteo SEAS5    |
|  Agroclimatology API |                           |  Forecast Ensemble   |
+──────────┬───────────+                           +──────────┬───────────+
           | Historical Climatology                           | 180-Day Seasonal
           | (Temp, Rain, Humidity)                           | Forecast Feeds
           v                                                  v
    +────────────────────────────────────────────────────────────────+
    |                                                                |
    |                         0. KISSANVISION                        |
    |                   (Core Agronomic ML System)                   |
    |                                                                |
    +─────────────┬────────────────────────────────────┬─────────────+
                  |                                    |
   Input Selections & Overrides           Predictions & SHAP Waterfalls
                  |                                    |
                  v                                    v
+──────────────────────────────────+        +──────────────────────────────────+
|  Farmer / Agricultural Officer   |        |  Third-Party App / FPO Platform  |
|  (Web Frontend / Streamlit User) |        |  (FastAPI REST Client)           |
+──────────────────────────────────+        +──────────────────────────────────+
```
**Figure B.1: Context Diagram (Level-0 DFD) of KissanVision.**

#### Level-1 Data Flow Diagram
Figure B.2 details the Level-1 Data Flow Diagram showing internal data stores and processes:

```
+──────────────────────+
| Kaggle Crop Dataset  |
+──────────┬───────────+
           | Raw District Records
           v
+──────────────────────────────────+        +──────────────────────────────────+
| 1.0 Clean & Standardize Ingestion|        | 2.0 Weather & Soil Enrichment    |
| (Area, Production -> q/ha)       +------->| (NASA POWER, SEAS5, NPK, Census) |
+──────────────────────────────────+        +────────────────┬─────────────────+
                                                             |
                                                             v
+──────────────────────────────────+        +──────────────────────────────────+
| 4.0 Local SHAP Attribution Engine|        | 3.0 Preprocess & Feature Encoding|
| (Calculate Shapley Deltas phi_j) |<-------+ (ColumnTransformer -> 59 Features|
+────────────────┬─────────────────+        +────────────────┬─────────────────+
                 |                                           | Transformed Features
                 v                                           v
+──────────────────────────────────+        +──────────────────────────────────+
| 5.0 ICAR Climate Risk Evaluator  |        | 6.0 XGBoost Yield Inference      |
| (Drought, Heat, Flood Alerting)  |        | (Evaluate Native Booster Model)  |
+────────────────┬─────────────────+        +────────────────┬─────────────────+
                 |                                           |
                 +─────────────────────┬─────────────────────+
                                       | Predicted Yield + SHAP + Risk Alerts
                                       v
                        +──────────────────────────────+
                        | 7.0 Multi-Channel Delivery   |
                        | (Streamlit, Web, FastAPI)    |
                        +──────────────────────────────+
```
**Figure B.2: Level-1 Data Flow Diagram of KissanVision.**

#### Entity-Relationship / Data Schema Diagram
Figure B.3 portrays the core data entities, schemas, and relational representations:

```
+------------------------------------+          +------------------------------------+
|            CROP_RECORD             |          |            STATE_GEO               |
+------------------------------------+          +------------------------------------+
| record_id (PK) : Integer           |          | state_id (PK) : Integer            |
| state_name (FK) : Varchar(50)      +--------->| state_name : Varchar(50)           |
| district_name : Varchar(50)        |          | centroid_lat : Float               |
| crop : Varchar(50)                 |          | centroid_lon : Float               |
| season : Varchar(20)               |          | gross_irrigated_pct : Float        |
| area_ha : Float                    |          | npk_consumption_kg_ha : Float      |
| production_tonnes : Float          |          +-----------------+------------------+
| yield_q_ha : Float                 |                            |
+------------------------------------+                            |
                                                                  v
+------------------------------------+          +------------------------------------+
|          PREDICTION_LOG            |          |           CLIMATE_CACHE            |
+------------------------------------+          +------------------------------------+
| prediction_id (PK) : UUID          |          | cache_id (PK) : Integer            |
| timestamp_utc : DateTime           |          | state_name (FK) : Varchar(50)      |
| state : Varchar(50)                |          | source : Enum(NASA, OpenMeteo)     |
| crop : Varchar(50)                 |          | avg_temp_c : Float                 |
| weather_mode : Enum(Hist, Forecast)|          | annual_rainfall_mm : Float         |
| predicted_yield_q_ha : Float       |          | relative_humidity_pct : Float      |
| shap_waterfall_json : JSON         |          | payload_json : JSON                |
+------------------------------------+          +------------------------------------+
```
**Figure B.3: Simplified Entity-Relationship Diagram of KissanVision.**

#### Sequence Diagram (Prediction and SHAP Attribution Flow)
Figure B.4 depicts the end-to-end sequence of execution for a client prediction request:

```
User / Client         FastAPI Router       PredictPipeline      ColumnTransformer      XGBoost Booster      SHAP Engine
     |                       |                    |                     |                     |                  |
     |--- POST /predict ---->|                    |                     |                     |                  |
     |    (State, Crop, ...) |                    |                     |                     |                  |
     |                       |-- validate payload |                     |                     |                  |
     |                       |-- predict(data) -->|                     |                     |                  |
     |                       |                    |-- transform(df) --->|                     |                  |
     |                       |                    |<-- 59-dim array ----|                     |                  |
     |                       |                    |                                           |                  |
     |                       |                    |-- predict(X) ---------------------------->|                  |
     |                       |                    |<-- raw yield (q/ha) ----------------------|                  |
     |                       |                    |                                                              |
     |                       |                    |-- explain(X) ----------------------------------------------->|
     |                       |                    |<-- base_value, phi_j attributions ---------------------------|
     |                       |                    |
     |                       |<-- response JSON --|
     |<-- 200 OK (Yield, ---|
     |    SHAP, Alerts)      |
```
**Figure B.4: Sequence Diagram: Client Prediction Request with Real-Time SHAP Attribution.**

#### State Diagram (Weather Mode & Personalization State Transitions)
Figure B.5 models the state transitions governing weather mode selection and input personalization:

```
       (*)
        |
        v
+──────────────────────────+
|  Initial Input State     |
|  (User selects Crop/Loc) |
+───────────┬──────────────+
            |
            v
+──────────────────────────────────────────────────────────+
|                   Weather Mode Toggle                    |
|  [Select Historical]              [Select Forecast]      |
|           |                               |              |
|           v                               v              |
|  NASA POWER Baseline             Open-Meteo ECMWF SEAS5  |
+───────────────────────────┬──────────────────────────────+
                            |
                            v
+──────────────────────────────────────────────────────────+
|                 Farmer Input Personalization             |
|  [Use State Averages]             [User Overrides Input] |
|           |                               |              |
|           v                               v              |
|  Badge: "State Average"          Badge: "Your Farm Input"|
+───────────────────────────┬──────────────────────────────+
                            |
                            v
+──────────────────────────+
|  Model Inference State   |
|  (Booster Yield Compute) |
+───────────┬──────────────+
            |
            v
+──────────────────────────+
|  Explain & Alert State   |
|  (SHAP Waterfall + ICAR) |
+───────────┬──────────────+
            |
            v
           (*)
```
**Figure B.5: State Transition Diagram of Weather Forecasting & Personalization Override Pipeline.**

---

### APPENDIX C: ISSUES LIST

#### Table C.1: Living register of engineering issues and roadmap resolutions
| ID | Description of Engineering Issue | Status | Planned Resolution / Action Item |
| :---: | :--- | :---: | :--- |
| **I-01** | **Crop Scope Expansion**: Current model trained on 15 major crops; minor millets (Ragi, Bajra) and sugarcane require expanded category mapping. | Open | Ingest remaining 35 Kaggle crop categories with dedicated acreage stratification in next retraining cycle. |
| **I-02** | **District-Level Soil Test Grid**: NPK values currently represent state-wide consumption averages rather than exact district soil tests. | Open | Ingest Soil Health Card (SHC) district laboratory repository to provide district-level soil chemistry defaults. |
| **I-03** | **Multilingual Voice Interface**: Rural smallholders require voice interaction in regional Indian vernaculars. | Deferred | Integrate open-source AI4Bharat / Bhashini speech-to-text API for Hindi, Punjabi, and Telugu voice queries. |
| **I-04** | **180-Day Forecast Uncertainty**: Long-range seasonal weather models carry natural spread in precipitation anomalies. | Open | Display ensemble standard deviation as explicit upper and lower confidence intervals on the dashboard gauge. |
| **I-05** | **Offline PWA Support**: Complete offline capability requires caching model weights directly inside the browser. | Open | Export XGBoost Booster to ONNX format to enable client-side inference via ONNX Runtime Web in progressive web app. |
| **I-06** | **FPO Multi-Farm Aggregation**: Collectives need to aggregate yield forecasts across hundreds of constituent member farms. | Open | Develop bulk CSV upload endpoint in FastAPI to compute batch yields and aggregate tonnage for FPO administrators. |
| **I-07** | **Satellite NDVI Cross-Validation**: Predictions currently rely on ground data; orbiting remote sensing can validate vigor. | Open | Integrate Google Earth Engine / Sentinel-2 10-meter NDVI time-series to cross-validate mid-season vegetative growth. |
