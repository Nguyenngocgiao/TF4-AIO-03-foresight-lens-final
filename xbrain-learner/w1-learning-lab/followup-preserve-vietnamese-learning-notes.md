# Follow-up prompt for Open Design

```text
Revise the current AIOps W1 website direction.

Important changes:
1. Do NOT define or override colors manually.
2. Follow the currently selected Open Design design system/style. Use its existing typography, spacing, colors, components, and visual language.
3. The website content must be in Vietnamese. Keep English technical terms only where they are standard, and explain them in Vietnamese.
4. Preserve the substance of the original W1 learning notes. Do not reduce them into a shallow overview.
5. This must be a real learning website where students can study W1 directly, not a marketing page, poster, or summary dashboard.

Use these local learning notes as the primary source of truth:
- /home/dinh/Downloads/W1-D1_ Metric Anomaly Detection _ My Learning Notes.html
- /home/dinh/Downloads/W1-D2_ Log Mining + Parsing + Anomaly từ Log _ My Learning Notes.html
- /home/dinh/Downloads/W1-D3_ Data Layer Architecture + Observability Pipeline _ My Learning Notes.html
- /home/dinh/Downloads/W1-offline-thursday-slides.html

Content preservation requirements:
- Keep the original learning-note ideas, explanations, examples, warnings, trade-offs, mental models, and teaching flow.
- Do not only extract headings or bullet points.
- Turn the notes into a structured interactive course page, but retain enough depth that a student can actually learn from it.
- If a concept appears in the notes, include it in the website unless it is clearly duplicate or irrelevant.
- Use Vietnamese explanations throughout.
- Use English technical terms with Vietnamese explanation, for example:
  - Rolling Z-score — điểm z theo cửa sổ trượt
  - EWMA — trung bình động có trọng số mũ
  - STL decomposition — tách chuỗi thời gian thành trend, seasonality, residual
  - Drain3 — thuật toán parse log thành template
  - OpenTelemetry Collector — thành phần thu thập và định tuyến telemetry

Learning website requirements:
- Create one complete long-form interactive web page for studying AIOps W1.
- Include sticky navigation and learning progress markers.
- Each major concept must have four parts:
  1. Giải thích bằng tiếng Việt
  2. Visualization hoặc animation minh họa
  3. Liên hệ với lab/file tương ứng
  4. Câu hỏi tự kiểm tra hoặc checkpoint

Required course sections:
1. Bắt đầu: W1 học gì và vì sao quan trọng
2. D1 — Metric Anomaly Detection
3. D1 Lab Walkthrough
4. D2 — Log Mining + Parsing + Log-based Anomaly Detection
5. D2 Lab Walkthrough
6. D3 — Data Layer Architecture + Observability Pipeline
7. D3 Lab Walkthrough
8. Offline Thursday Lab — Broken System Triage
9. Final Review / Knowledge Check

D1 must teach deeply:
- Vì sao threshold cứng thường báo muộn hoặc báo sai
- Distribution, skewness, stationarity
- Rolling Z-score / 3σ với moving window animation
- EWMA với giải thích alpha phản ứng nhanh/chậm
- STL decomposition: trend + seasonality + residual
- Isolation Forest: anomaly bị cô lập nhanh hơn
- Autoencoder: reconstruction error
- Feature engineering cho time series
- Precision, recall, F1, TTD, false alarm rate
- Vì sao accuracy không đủ trong AIOps

D2 must teach deeply:
- Vì sao log quan trọng: metric nói “cái gì sai”, log giúp hiểu “vì sao”
- Structured vs unstructured logs
- Vì sao không thể phân tích log line-by-line bằng exact match
- Raw logs → log templates
- Drain3 parse tree intuition
- Parser comparison: Drain3 vs Spell vs Lenma vs LLM-based parsing
- Template count time series
- TF-IDF / embedding similarity
- New template detection
- Production concerns: volume, sampling, storage cost

D3 must teach deeply:
- Vì sao data architecture quyết định chất lượng AIOps/RCA
- Observability pipeline: collect → transport → process → store → query → alert
- OpenTelemetry: metrics, logs, traces, SDK, Collector
- Kafka vs direct push, kèm trade-off và “khi nào chọn cái nào”
- Feature pipeline và liên hệ với anomaly detection D1
- Feature store online/offline
- Storage tradeoffs: TSDB, log store/Loki, traces/Jaeger, S3/Parquet/data lake
- Schema registry và data contracts
- Cost model cho observability data
- ADR: cách ra quyết định kiến trúc

Lab connection requirements:
Show file/artifact cards and explain why each matters:
- w1/d1/assignment.ipynb
- w1/d1/data/realKnownCause/ambient_temperature_system_failure.csv
- w1/d1/data/realKnownCause/nyc_taxi.csv
- w1/d1/detector_comparison.png
- w1/d1/isolation_forest_model.joblib
- w1/d1/SUBMIT.md
- w1/d2/HDFS_2k.log
- w1/d2/BGL_2k.log
- w1/d2/nginx_structured.log
- w1/d2/nginx_unstructured.log
- w1/d2/assignment.ipynb
- w1/d2/assignment.py
- w1/d2/log_analyzer.py
- w1/d2/results/top_templates.csv
- w1/d2/results/anomaly_plot.png
- w1/d2/SUBMIT.md
- w1/d3/architecture.drawio
- w1/d3/architecture.png
- w1/d3/architecture.md
- w1/d3/pipeline.py
- w1/d3/features.json
- w1/d3/cost_estimate.md
- w1/d3/cost_model.py
- w1/d3/ADR-001.md
- w1/d3/test_d3.py
- w1/d3/SUBMIT.md

Animation/visualization requirements:
- Use meaningful animations only when they teach the concept.
- Animate moving rolling window for Rolling Z-score.
- Animate EWMA smoothing compared to raw noisy signal.
- Animate STL decomposition into trend/seasonality/residual.
- Animate Isolation Forest split/isolation intuition.
- Animate Autoencoder reconstruction error.
- Animate raw log lines becoming templates.
- Animate Drain3 token routing / parse tree intuition.
- Animate template count spike and new template detection.
- Animate telemetry flowing through OTel → Kafka/direct push → processors → storage → dashboard/ML detector.
- Respect reduced-motion preferences.

Design guidance:
- Do not specify a custom color palette.
- Do not hardcode a new visual identity.
- Use the selected Open Design system as the source of truth for visual style.
- Focus design effort on readability, learning flow, interaction clarity, and visual explanation quality.
- Make the website feel like an interactive course module, not a marketing landing page.

Final result:
A Vietnamese interactive AIOps W1 learning website that preserves the depth of the original learning notes and teaches the student through explanations, animations, lab walkthroughs, and checkpoints.
```
