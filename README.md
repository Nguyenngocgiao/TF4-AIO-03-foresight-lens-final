# XBrain Capstone - Task Force 4 (AIO-03)
## Foresight Lens - Capacity Exhaustion Prediction Engine

This repository contains the AI Engine and Documentation for the Capstone Project of **AIO-03** in the XBrain AWS DevOps/CloudOps Foundation Program.

### 🌟 Project Overview

**Foresight Lens** is a predictive alerting engine designed to detect and warn about impending Capacity Exhaustion (OOM/CPU starvation) events with a minimum lead time of 15 minutes before actual SLO breach.

To optimize the strict $200 budget constraint and ensure extreme low latency, our team adopted a **Statistical 3-Sigma Rolling Window** algorithm in favor of traditional LLM solutions. This decision guarantees mathematically accurate detection, zero hallucination risk, and virtually $0 execution cost.

### 🗂 Repository Structure

- `engine-skeleton/`: Contains the FastAPI implementation of the AI Engine.
  - `app/engine.py`: The core 3-Sigma detection logic.
  - `app/audit.py`: The secure PII-hashed audit logger.
  - `app/main.py`: The `/v1/detect` and `/v1/verify` API endpoints.
  - `tests/test_api.py`: 10 comprehensive pytest scenarios (Multi-tenant, Happy path, False positive checks).
- `xbrain-learner/tf4-evidence/`: Contains the evaluation scripts (`tf4_evidence.py`) generating Brier Score, Precision, and Recall metrics.
- `docs/`: The complete Capstone specification and design documents.
- `contracts/`: API and deployment contracts between the AI and CDO groups.
- `tf4-foresight-lens.html`: The interactive final presentation slide deck.

### 🚀 Getting Started

#### 1. Setup Environment
```bash
cd engine-skeleton
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Run Tests
Ensure all 10 scenarios pass with strict X-Tenant-Id isolation:
```bash
pytest tests/ -v
```

#### 3. Start the Engine locally
```bash
uvicorn app.main:app --reload --port 8000
```

### 📊 Performance & Evidence
Our architecture was validated against 6 months of historical synthetic data:
- **Lead time**: ~ 106 minutes prior to crash.
- **Precision**: 1.0 (100%)
- **False Positive Rate (FPR)**: 1.9%
- **Cost**: < $3 / month (Local compute execution).

See `docs/04_eval_report.md` for full evaluation details.

### 👥 Team
- **Group**: AIO-03
- **Role**: AI Group
- **Task Force**: 4
