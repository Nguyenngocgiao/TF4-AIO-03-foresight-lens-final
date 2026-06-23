# Requirements - Foresight Lens

<!-- Doc owner: AIO-03 Lead
     Status: Final (W11 T6 Pack #1)
     Word target: 800-1500 từ
     BA methodology: dùng 5W2H làm khung khi interview Client T2 W11 -->

## 1. Khách hàng nói

> "Hệ thống của chúng tôi thường xuyên gặp tình trạng cạn kiệt tài nguyên (Capacity Exhaustion) một cách đột ngột. Khi monitor báo đỏ thì hệ thống đã sập rồi. Chúng tôi cần một giải pháp có khả năng dự đoán sớm sự cố trước khi nó xảy ra để SRE kịp thời can thiệp. Tuy nhiên, chúng tôi không muốn hệ thống tự động can thiệp (auto-remediation) vì sợ rủi ro, và ngân sách duy trì hàng tháng phải cực kỳ tối ưu, không được vượt quá $200."

## 2. Outcomes mong muốn

- **Outcome 1**: Dự đoán sớm sự cố cạn kiệt tài nguyên (Memory/CPU) với độ trễ tối thiểu 15 phút trước khi hệ thống thực sự sập.
- **Outcome 2**: Đảm bảo phân lập dữ liệu rõ ràng (Multi-tenant) cho ít nhất 3 dịch vụ Tier-1 cốt lõi.
- **Outcome 3**: Tối ưu hóa chi phí vận hành ở mức thấp nhất (gần như $0), loại bỏ hoàn toàn các rủi ro phát sinh từ việc sử dụng các mô hình ngôn ngữ lớn (LLM).
- **Outcome 4**: Đóng vai trò là một "Cố vấn" (Predict + Recommend), cung cấp cảnh báo kèm hành động đề xuất, không tự ý thay đổi hạ tầng.

## 3. Success criteria (measurable)

| Metric | Target | How to measure |
|---|---|---|
| **Lead Time** | ≥ 15 phút trước SLO breach | So sánh thời điểm phát ra Alert với thời điểm hệ thống OOM trong test case. |
| **Precision** | ≥ 0.90 | Tỉ lệ True Positive / (True Positive + False Positive) qua bộ 10 test scenarios. |
| **False Positive Rate** | < 5% | Đếm số lượng alert bị kích hoạt sai trong điều kiện Traffic bình thường. |
| **Cost** | < $200/tháng | AWS Cost Explorer (chỉ tính chi phí cho AI Engine, không tính CDO infra). |

## 4. Constraints

- **Budget**: Tuyệt đối không vượt quá $200/tháng cho toàn bộ giải pháp AI.
- **Timeline**: W11-W12, code freeze T4 W12 18h.
- **Tooling**: AWS only, Python (FastAPI, NumPy).
- **Architecture**: Phải có cơ chế Fallback (Fail-open) khi Engine down.

## 5. Out of scope

- ❌ **Tự động phục hồi (Auto-remediation)**: Engine chỉ suggest `SCALE_UP` hoặc `INVESTIGATE`, việc gọi API thay đổi hạ tầng thuộc scope của team CDO.
- ❌ **LLM Root Cause Analysis**: Không sử dụng GenAI để phân tích log ngôn ngữ tự nhiên (để đảm bảo budget và tránh Hallucination).
- ❌ **Cross-region failover**: Thiết kế dừng ở mức Single-region, DR là design-only.

## 6. Non-functional requirements

- **SLO platform**: p99 latency < 500ms · availability ≥ 99.5%.
- **Multi-tenant scale**: Hỗ trợ độc lập dữ liệu cho ít nhất 3 tenant/service (Payment, Fraud, Ledger).
- **Security baseline**: Cách ly context 100% bằng `X-Tenant-Id`. Audit log mọi request. Không lưu raw PII.
- **Cost target**: < $5/tenant/month.

## 7. Open questions

- [x] Q1: Có được phép lưu trữ raw data của tín hiệu đo lường vào log không? - *Resolved: Không. Bắt buộc dùng Hashing (SHA-256) cho input data để tránh lộ PII qua log.*
