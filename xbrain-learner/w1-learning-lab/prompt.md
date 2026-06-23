# Open Design Prompt — Build a Full Interactive Learning Website for AIOps W1

Use this prompt in Open Design / Antigravity.

## Local source files to reference

Learning notes downloaded locally:

```text
/home/dinh/Downloads/W1-D1_ Metric Anomaly Detection _ My Learning Notes.html
/home/dinh/Downloads/W1-D2_ Log Mining + Parsing + Anomaly từ Log _ My Learning Notes.html
/home/dinh/Downloads/W1-D3_ Data Layer Architecture + Observability Pipeline _ My Learning Notes.html
/home/dinh/Downloads/W1-offline-thursday-slides.html
```

Existing repo/lab context:

```text
/home/dinh/workspace/aiops-NguyenHuuDinh/w1/d1/
/home/dinh/workspace/aiops-NguyenHuuDinh/w1/d2/
/home/dinh/workspace/aiops-NguyenHuuDinh/w1/d3/
/home/dinh/workspace/aiops-NguyenHuuDinh/slides/aiops_w1_detection_triage_deep_dive_slides.html
/home/dinh/workspace/aiops-NguyenHuuDinh/slides/20260528-aiops-plan-3-weeks-detailed-en.html
```

---

## Prompt to paste into Open Design

```text
Build a complete interactive learning website for AIOps Week 1.

Important:
This must NOT be an overview poster, landing page, or simple infographic.
This must be a full learning website where a student can actually study W1 from beginning to end.
The page should teach concepts, explain algorithms visually, animate the important ideas, include lab walkthroughs, quizzes/checkpoints, and connect each concept to the actual W1 lab files.

Title:
AIOps W1 Learning Studio — Detection & Triage

Subtitle:
Learn metric anomaly detection, log mining, and observability data architecture through visual explanations, animations, and lab-guided practice.

Primary output:
Create a single self-contained responsive HTML learning website.
It should work as a long-form interactive course page, not a slide deck only.
Use sections, sticky navigation, progress indicators, animated diagrams, visual demos, expandable explanations, code cards, lab checklists, and quiz cards.

Target learner:
Vietnamese university / bootcamp students learning AIOps for the first time.
Use English technical terms, but explanations should be simple and Vietnamese-friendly.
Prefer bilingual microcopy when helpful: English term + Vietnamese explanation.

Learning goal:
By the end of the page, the learner should understand and be able to explain:
1. What anomaly detection is in AIOps.
2. Why simple thresholds are not enough.
3. How rolling Z-score, EWMA, STL, Isolation Forest, and Autoencoder detect anomalies.
4. Why logs need parsing/mining before they become useful signals.
5. How Drain3 turns raw logs into templates.
6. How template counts and new templates can reveal incidents.
7. Why observability architecture matters for AIOps.
8. How OTel, Kafka/direct push, storage, feature pipelines, and ADR decisions affect detection and RCA quality.
9. How W1 labs build toward an incident triage hypothesis.

Core story:
W1 is a learning journey:
Raw telemetry → metric anomaly detection → log mining → observability data layer → evidence synthesis → incident triage hypothesis.
The website must teach this journey step by step.

Use these source topics and expand them into full teaching sections:

W1-D1 — Metric Anomaly Detection
- Normal distribution, skewness, stationarity
- Rolling Z-score / 3σ detection
- EWMA
- STL decomposition
- Isolation Forest
- Autoencoder / reconstruction error
- Feature engineering for time series
- Evaluation metrics: precision, recall, F1, TTD, false alarm rate
- Lab: load NAB-style time series, perform EDA, implement detectors, compare results, produce detector comparison and reflection

W1-D2 — Log Mining + Parsing + Log-based Anomaly Detection
- Why logs matter: metrics say what is wrong, logs explain why
- Structured vs unstructured logs
- Log parsing problem: many unique log lines need templates
- Drain3 parse tree and template extraction
- Parser comparison: Drain3 vs Spell vs Lenma vs LLM-based parsing
- Template count time series
- TF-IDF / embedding for log template similarity
- New template detection and semantic drift
- Production log concerns: volume, sampling, storage cost
- Lab: parse HDFS/BGL/nginx logs, extract templates, generate top templates, detect anomalies, inspect template spikes

W1-D3 — Data Layer Architecture + Observability Pipeline
- End-to-end observability pipeline: collect → transport → process → store → query → alert
- OpenTelemetry: metrics, logs, traces, SDK, Collector
- Kafka vs direct push
- Streaming feature pipeline
- Feature store: online vs offline
- Schema registry and data contracts
- Storage trade-offs: time-series DB, Loki/log store, S3/Parquet/data lake
- Cost model for observability data
- ADR writing: architecture decision for Kafka vs direct push
- Lab: draw architecture diagram, implement mock pipeline, compute cost estimate, write ADR

Required website structure:

1. Sticky course navigation
Create a left or top sticky navigation with progress states:
- Start here
- D1 Metric Anomaly Detection
- D1 Lab
- D2 Log Mining
- D2 Lab
- D3 Observability Architecture
- D3 Lab
- Offline Broken System Lab
- Final Review
Each section should feel like a real lesson, not just a summary.

2. Hero: Start Here
Create a hero section with:
- Course title
- One-sentence promise: “Learn how AIOps turns raw telemetry into an incident hypothesis.”
- Animated visual: metrics stream + log stream flowing into a detection/triage engine.
- “What you will learn” cards.
- “What you will build” cards.

3. Interactive W1 Learning Map
Create a clickable/expandable journey map:
Raw metrics → Detect anomaly → Raw logs → Parse templates → Build data pipeline → Combine evidence → Incident hypothesis.
When each node is selected/expanded, show what concept it teaches and which lab file uses it.

4. D1 Lesson — Metric Anomaly Detection
This must be a real teaching section with explanation blocks, not a list.
Include these subsections:

4.1 Why threshold alerts fail
- Explain fixed threshold vs adaptive baseline.
- Animated chart: normal signal slowly drifts until fixed threshold fires too late.

4.2 Distribution intuition
- Visualize normal distribution, skewness, and outliers.
- Add a small callout: “Before choosing detector, inspect distribution.”

4.3 Rolling Z-score / 3σ
- Animated line chart with moving window.
- Show mean line and ±3σ band.
- Highlight when a point becomes anomaly.
- Include formula card:
  z = (x - rolling_mean) / rolling_std
- Include “when it works” and “when it fails.”

4.4 EWMA
- Animated comparison: raw noisy series vs smoothed EWMA baseline.
- Explain alpha intuitively: higher alpha reacts faster, lower alpha smoother.
- Include a mini slider-style mockup for alpha, even if static.

4.5 STL decomposition
- Animated or stacked visual: original series splits into trend + seasonality + residual.
- Explain that anomalies often live in residual.

4.6 Isolation Forest
- Visual metaphor: normal points require many splits, anomalies isolate quickly.
- Use animated splitting boxes / tree nodes.
- Explain contamination and feature engineering.

4.7 Autoencoder
- Visual: input time window → encoder bottleneck → decoder reconstruction → reconstruction error.
- Show anomaly when reconstruction error spikes.
- Explain when DL is worth it and when it is overkill.

4.8 Detector comparison
- Visual comparison table: Z-score, EWMA, STL, Isolation Forest, Autoencoder.
- Columns: needs labels, handles seasonality, explainability, complexity, best use case.

5. D1 Lab Walkthrough
Create a practical lab module:
- Inputs: NAB-style CSV time series.
- Files/artifacts:
  - w1/d1/assignment.ipynb
  - w1/d1/data/realKnownCause/ambient_temperature_system_failure.csv
  - w1/d1/data/realKnownCause/nyc_taxi.csv
  - w1/d1/detector_comparison.png
  - w1/d1/isolation_forest_model.joblib
  - w1/d1/SUBMIT.md
- Step-by-step cards:
  1. Load time series
  2. Plot and inspect distribution
  3. Engineer rolling features
  4. Run statistical detector
  5. Run Isolation Forest
  6. Compare precision/recall/F1
  7. Write reflection
- Include a “Try to explain” checkpoint: Why recall matters more than accuracy in AIOps?

6. D2 Lesson — Log Mining + Parsing
This must teach log mining deeply with visual examples.

6.1 Why logs are hard
- Animate many raw log lines with variable tokens.
- Explain why exact string matching fails.

6.2 Raw logs → templates
- Show raw lines like:
  User 123 failed login from 10.0.0.5
  User 987 failed login from 10.0.0.9
- Animate them becoming:
  User <*> failed login from <*>

6.3 Drain3 parse tree intuition
- Visual tree with fixed-depth parsing.
- Animate tokens flowing through tree branches.
- Show where variables are replaced with wildcards.

6.4 Parser comparison
- Cards for Drain3, Spell, Lenma, LLM-based parsing.
- Explain tradeoffs: speed, accuracy, adaptability, cost.

6.5 Template count anomaly
- Animated time series of template counts.
- Show spike in error template count.

6.6 TF-IDF / embedding similarity
- Visualize templates as points in vector space.
- Similar templates cluster together.
- Outlier template appears far away.

6.7 New template detection
- Show known template catalog, then a never-seen-before template appears.
- Explain why new template can signal deploy issue or incident.

7. D2 Lab Walkthrough
Create a practical lab module:
- Inputs/artifacts:
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
- Step-by-step cards:
  1. Load raw logs
  2. Parse with Drain3
  3. Extract templates
  4. Count templates over time
  5. Find top templates
  6. Detect spikes/new templates
  7. Explain what logs add beyond metrics
- Include checkpoint question: “If metric latency spikes and a new error template appears, what evidence is stronger? Why?”

8. D3 Lesson — Observability Data Layer Architecture
This must teach architecture, not just draw boxes.

8.1 Why architecture matters for AIOps
- Explain: bad pipeline = missing evidence = bad RCA.
- Visual cause/effect: dropped logs → incomplete triage → wrong hypothesis.

8.2 End-to-end pipeline
Animated architecture diagram:
Services → OTel SDK → OTel Collector → Kafka or direct push → processors → storage → dashboard/ML detector.

8.3 OpenTelemetry
- Explain metrics/logs/traces.
- Show how OTel Collector normalizes and routes telemetry.

8.4 Kafka vs direct push
- Create an interactive tradeoff panel:
  Direct push = simple, low latency, less replay.
  Kafka = buffer, replay, decoupling, more complexity/cost.
- Show “choose this when…” cards.

8.5 Storage tradeoffs
- Compare TSDB, log store/Loki, traces/Jaeger, data lake/S3 Parquet.
- Explain what each stores and why.

8.6 Feature pipeline
- Show rolling features computed from telemetry.
- Connect to D1 anomaly detection.

8.7 Schema registry / data contracts
- Visualize a log schema change breaking a parser.
- Explain why contracts prevent silent pipeline failure.

8.8 Cost model
- Show cost drivers: logs/day, metrics/sec, retention days, storage tier.
- Include a small mock calculator card (static is okay): volume × retention × cost per GB.

9. D3 Lab Walkthrough
Create a practical lab module:
- Files/artifacts:
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
- Step-by-step cards:
  1. Draw architecture
  2. Decide Kafka vs direct push
  3. Build mock pipeline
  4. Extract rolling features
  5. Estimate cost
  6. Write ADR
  7. Run tests and submit
- Include checkpoint: “What breaks if logs are dropped during the incident window?”

10. Offline Thursday Lab — Broken System Triage
Create a full capstone section:
- Scenario: a broken microservice system with metrics + logs.
- Goal: find when failure started, where symptoms appear, and what root-cause hypothesis should be investigated.
- Animated evidence board:
  Metric spike + log template spike + architecture context → incident hypothesis.
- Show that W1 does not require perfect root cause automation. W1 teaches evidence gathering and narrowing.
- Output should be FINDINGS-style reasoning:
  - When did it start?
  - Which service is suspicious?
  - Which signals support the hypothesis?
  - What should be investigated next?

11. Knowledge Check / Quiz Section
Add short interactive-looking quiz cards after each day:
D1 quiz examples:
- Why can accuracy be misleading in anomaly detection?
- When does rolling Z-score fail?
- Why use Isolation Forest after simple statistical baselines?
D2 quiz examples:
- Why parse logs into templates?
- What does a new template indicate?
- Why are template count spikes useful?
D3 quiz examples:
- When should Kafka be used instead of direct push?
- Why are schema contracts important?
- How does observability cost affect architecture?
Use expandable answer cards or reveal-style UI.

12. Final Review Section
Create a final summary that helps students remember:
- Metrics tell when and what changed.
- Logs explain why it may have changed.
- Architecture decides whether evidence is complete and trustworthy.
- W1 output is an incident triage hypothesis.
- W2 will use this evidence for deeper RCA.

Interaction and animation requirements:
- Include meaningful animations, not decorative motion.
- Animate data flowing through pipelines.
- Animate chart concepts: moving rolling window, anomaly spike, EWMA smoothing, STL decomposition, template extraction, Kafka buffering.
- Use CSS/JS for lightweight interactions if possible.
- Add hover/click expandable cards for “why it matters,” “when it works,” and “when it fails.”
- Include progress indicators and section completion feel.
- Respect reduced motion: include prefers-reduced-motion CSS behavior.

Visual style:
- Premium technical education website.
- Dark navy/deep slate background.
- Neon AIOps accents: cyan, orange, red, green, purple.
- Use dashboard cards, animated SVG-like diagrams, charts, data streams, code snippets, file artifact cards, and architecture blocks.
- Use clean typography, strong hierarchy, generous spacing, and readable long-form lesson text.
- Make it feel like an XBrain/AIOps interactive course module, not a marketing landing page.

UX requirements:
- Student must be able to learn from the page without external explanation.
- Each concept needs: explanation, visual/animation, practical lab connection, and checkpoint question.
- Avoid shallow bullet lists. Turn bullets into teaching paragraphs, diagrams, and cards.
- Avoid generic placeholders and lorem ipsum.
- Do not invent unrelated tools or datasets.
- Keep examples aligned with the W1 notes and lab folders.
- Use accessible colors and readable body text.
- Responsive layout for desktop and tablet; mobile should still be readable.

Implementation requirements:
- Single self-contained HTML file preferred.
- If using CSS/JS, keep it inside the HTML unless the tool requires separate files.
- Use semantic HTML sections.
- Include a sticky table of contents.
- Use lightweight inline SVG/CSS for animations where possible.
- Do not require a backend.
- Do not require external paid APIs.

Final deliverable:
A complete interactive AIOps W1 learning website that teaches the student W1, not just summarizes it.
The student should be able to scroll through the website and actually learn metric anomaly detection, log mining, and observability architecture with animated visual explanations and lab-guided practice.
```
