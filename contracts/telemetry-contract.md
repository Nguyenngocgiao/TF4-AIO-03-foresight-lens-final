# Telemetry Contract - Task force 4

<!-- Owner: AIO-03
     Signed by: AI Lead + CDO Leads × 2-3 + Reviewer panel
     Date signed: 2026-06-25 (W11 T5)
     🔒 FREEZE - no change without formal change request -->

## Mục đích

Định nghĩa **signals nào CDO emit từ infra** → AI engine consume để dự đoán Capacity Exhaustion. Là handshake giữa platform layer (CDO) và intelligence layer (AI).

## Versioning

- **Current version**: `v1.0`
- **Evolution**: backward-compatible additions only. Breaking change → new contract version + migration window
- **Change request process**: raise trong nhóm task force → họp bàn → bump version + notify all

---

## Signals required

> List signals AI engine cần để analyze. Hệ thống Foresight Lens sử dụng mảng dữ liệu (Rolling Window) để phát hiện bất thường dựa trên 3-Sigma.

### Signal 1: `cpu_usage_percent`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, region, tenant_id (mandatory) |
| **Unit** | percentage (0-100) |
| **Frequency** | 1 phút |
| **Emit point** | CloudWatch Metrics / Prometheus → CDO Ingestion → AI API |
| **Retention** | 7 ngày hot + 83 ngày cold (tổng 90 ngày minimum) |
| **Used for** | Phát hiện xu hướng tăng đột biến CPU |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

**Schema example** (concrete JSON payload AI nhận được):

```json
{
  "ts": "2026-06-25T10:30:00Z",
  "tenant_id": "tnt-abc123",
  "service_id": "payment-gateway",
  "signal_name": "cpu_usage_percent",
  "value": 85.5,
  "labels": {"region": "ap-southeast-1"}
}
```

### Signal 2: `memory_usage_percent`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, region, tenant_id (mandatory) |
| **Unit** | percentage (0-100) |
| **Frequency** | 1 phút |
| **Emit point** | CloudWatch Metrics / Prometheus → CDO Ingestion → AI API |
| **Retention** | 7 ngày hot + 83 ngày cold (tổng 90 ngày minimum) |
| **Used for** | Dự đoán Memory Leak dẫn tới OOM (Out Of Memory) |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

### Signal 3: `active_connections`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, region, tenant_id (mandatory) |
| **Unit** | count |
| **Frequency** | 1 phút |
| **Emit point** | ALB / Nginx metrics |
| **Used for** | Correlate giữa traffic spike và resource exhaustion |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

### Signal 4: `db_connection_pool_pct`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, db_type (e.g. postgres, mysql), region, tenant_id |
| **Unit** | percentage (0-100) |
| **Frequency** | 1 phút |
| **Emit point** | RDS CloudWatch Metrics → CDO Ingestion → AI API |
| **Retention** | 7 ngày hot + 83 ngày cold (tổng 90 ngày minimum) |
| **Used for** | Phát hiện cạn kiệt Connection Pool của Database do slow queries hoặc Cache Stampede |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

### Signal 5: `queue_depth`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, queue_name, region, tenant_id |
| **Unit** | count |
| **Frequency** | 1 phút |
| **Emit point** | SQS CloudWatch Metrics → CDO Ingestion → AI API |
| **Retention** | 7 ngày hot + 83 ngày cold (tổng 90 ngày minimum) |
| **Used for** | Đo lường mức độ nghẽn cổ chai (backlog) của worker consuming message (ví dụ Ledger worker) |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

### Signal 6: `cache_hit_rate_pct`

| Attribute | Value |
|---|---|
| **Type** | gauge |
| **Labels** | service_id, cache_type (e.g. redis), region, tenant_id |
| **Unit** | percentage (0-100) |
| **Frequency** | 1 phút |
| **Emit point** | ElastiCache CloudWatch Metrics → CDO Ingestion → AI API |
| **Retention** | 7 ngày hot + 83 ngày cold (tổng 90 ngày minimum) |
| **Used for** | Phát hiện Cache Miss Spike dẫn đến quá tải trực tiếp xuống RDS |
| **Emit SLA** | p99 latency < 60s từ lúc phát sinh metric |
| **Volume SLA** | Peak 50k events/sec (tổng toàn hệ thống) |
| **Cost estimate** | Tối ưu thông qua Time-series DB |

---

## Cross-cutting requirements

Mọi signal phải comply:
- **Tenant scoping**: mọi signal payload **bắt buộc** có `tenant_id` field - AI engine không accept signal thiếu tenant_id.
- **Time precision**: timestamp RFC3339 UTC, millisecond precision.
- **Schema validation**: AI ingestion layer (Pydantic) validate schema; reject malformed.
- **PII**: KHÔNG được chứa PII (email / phone / name) trong signal value hoặc labels.
