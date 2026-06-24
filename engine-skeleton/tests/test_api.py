from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ============================================================
# Scenario 1: Happy Path — Không có anomaly
# ============================================================
def test_detect_happy_path():
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 51},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 49},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 50}
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is False
    assert data["recommendation"] is None

# ============================================================
# Scenario 2: Sudden Spike — CPU nhảy vọt đột ngột
# ============================================================
def test_detect_sudden_spike():
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 98}
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is True
    assert data["recommendation"]["action_verb"] == "SCALE_UP"
    assert "audit_id" in data

# ============================================================
# Scenario 3: Gradual Drift — CPU tăng dần từ từ
# ============================================================
def test_detect_gradual_drift():
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 52},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 54},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 56},
            {"ts": "2026-06-25T10:04:00Z", "signal_name": "cpu_pct", "value": 58},
            {"ts": "2026-06-25T10:05:00Z", "signal_name": "cpu_pct", "value": 60},
            {"ts": "2026-06-25T10:06:00Z", "signal_name": "cpu_pct", "value": 62},
            {"ts": "2026-06-25T10:07:00Z", "signal_name": "cpu_pct", "value": 64},
            {"ts": "2026-06-25T10:08:00Z", "signal_name": "cpu_pct", "value": 66},
            {"ts": "2026-06-25T10:09:00Z", "signal_name": "cpu_pct", "value": 95}  # breach
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:09:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is True

# ============================================================
# Scenario 4: Slow Leak — Memory tăng rỉ rả rồi bùng phát
# ============================================================
def test_detect_slow_leak():
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "mem_pct", "value": 40},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "mem_pct", "value": 41},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "mem_pct", "value": 42},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "mem_pct", "value": 42},
            {"ts": "2026-06-25T10:04:00Z", "signal_name": "mem_pct", "value": 43},
            {"ts": "2026-06-25T10:05:00Z", "signal_name": "mem_pct", "value": 43},
            {"ts": "2026-06-25T10:06:00Z", "signal_name": "mem_pct", "value": 44},
            {"ts": "2026-06-25T10:07:00Z", "signal_name": "mem_pct", "value": 44},
            {"ts": "2026-06-25T10:08:00Z", "signal_name": "mem_pct", "value": 45},
            {"ts": "2026-06-25T10:09:00Z", "signal_name": "mem_pct", "value": 92}  # OOM burst
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:09:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is True
    assert data["recommendation"]["action_verb"] == "ROLLBACK"

# ============================================================
# Scenario 5: Noisy Baseline — Nhiễu cao nhưng KHÔNG có drift thật
# ============================================================
def test_detect_noisy_baseline_no_false_positive():
    # Noisy data nhưng không vượt 3-sigma
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 55},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 45},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 58},
            {"ts": "2026-06-25T10:04:00Z", "signal_name": "cpu_pct", "value": 42},
            {"ts": "2026-06-25T10:05:00Z", "signal_name": "cpu_pct", "value": 53}
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:05:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is False

# ============================================================
# Scenario 6: Sudden Drop — Throughput sụp đổ (two-tailed)
# ============================================================
def test_detect_sudden_drop():
    payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "throughput_rps", "value": 1000},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "throughput_rps", "value": 1000},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "throughput_rps", "value": 1000},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "throughput_rps", "value": 50}  # Drop 95%
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    headers = {"X-Tenant-Id": "tnt-1", "Authorization": "SigV4"}
    response = client.post("/v1/predict", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["anomaly"] is True
    assert data["recommendation"]["action_verb"] == "INVESTIGATE"

# ============================================================
# Scenario 7: Multi-tenant isolation — Tenant A anomaly, Tenant B clean
# ============================================================
def test_multi_tenant_isolation():
    anomaly_payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 98}
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    normal_payload = {
        "signal_window": [
            {"ts": "2026-06-25T10:00:00Z", "signal_name": "cpu_pct", "value": 50},
            {"ts": "2026-06-25T10:01:00Z", "signal_name": "cpu_pct", "value": 51},
            {"ts": "2026-06-25T10:02:00Z", "signal_name": "cpu_pct", "value": 49},
            {"ts": "2026-06-25T10:03:00Z", "signal_name": "cpu_pct", "value": 50}
        ],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    # Tenant A has anomaly
    r1 = client.post("/v1/predict", json=anomaly_payload, headers={"X-Tenant-Id": "tnt-A", "Authorization": "SigV4"})
    assert r1.status_code == 200
    assert r1.json()["anomaly"] is True
    
    # Tenant B is clean — should NOT be affected by Tenant A
    r2 = client.post("/v1/predict", json=normal_payload, headers={"X-Tenant-Id": "tnt-B", "Authorization": "SigV4"})
    assert r2.status_code == 200
    assert r2.json()["anomaly"] is False

# ============================================================
# Scenario 8: Validation Error — Thiếu X-Tenant-Id
# ============================================================
def test_missing_tenant_id():
    payload = {
        "signal_window": [],
        "context": {
            "deployment_version": "v1",
            "time_range": {"start_ts": "2026-06-25T10:00:00Z", "end_ts": "2026-06-25T10:03:00Z"}
        }
    }
    response = client.post("/v1/predict", json=payload, headers={"Authorization": "SigV4"})
    assert response.status_code == 422
