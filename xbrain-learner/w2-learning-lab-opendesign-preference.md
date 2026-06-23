# Open Design Preference — AIOps W2 Interactive Learning Website

Use this as the project preference / custom instruction for Open Design.

```text
Build a real Vietnamese interactive learning website for AIOps W2.

This is not a landing page, not an overview, not a poster, and not a static infographic.
The student must be able to learn W2 directly from the interface through explanations, interactive diagrams, animations, lab walkthroughs, and checkpoints.

Project type preference:
- Prototype
- Responsive web
- High fidelity
- Use the currently selected Open Design design system
- Do not manually define or override colors
- Do not create a separate custom visual identity
- Prefer Local CLI · Antigravity if an agent option is available

Source materials:
- /home/dinh/Downloads/W2-D1_ Alert Correlation — Từ Noise Sang Signal _ My Learning Notes.html
- /home/dinh/Downloads/W2-D2_ RCA — Graph, Causal & LLM-augmented _ My Learning Notes.html
- /home/dinh/Downloads/W2-D3_ Model Serving — Đưa Pipeline Lên Production _ My Learning Notes.html
- /home/dinh/Downloads/W2-offline-slides.html
- /home/dinh/Downloads/W2-offline-slides(1).html

Source image/asset folders:
- /home/dinh/Downloads/W2-D1_ Alert Correlation — Từ Noise Sang Signal _ My Learning Notes_files
- /home/dinh/Downloads/W2-D2_ RCA — Graph, Causal & LLM-augmented _ My Learning Notes_files
- /home/dinh/Downloads/W2-D3_ Model Serving — Đưa Pipeline Lên Production _ My Learning Notes_files

Use these image folders as visual references and source diagrams. Rebuild them into interactive HTML/CSS/JS learning visualizations when possible; do not simply paste static screenshots unless a static reference is more appropriate.

Repo/lab source paths:
- /home/dinh/workspace/aiops-NguyenHuuDinh/w2/d1
- /home/dinh/workspace/aiops-NguyenHuuDinh/w2/d2
- /home/dinh/workspace/aiops-NguyenHuuDinh/w2/d3

Language/content requirements:
- All learning content must be in Vietnamese.
- Keep important English technical terms when standard: alert correlation, RCA, graph traversal, PageRank, temporal causality, lag, Jaccard similarity, kNN, FastAPI, health check, readiness, Prometheus, LLM kill switch.
- Preserve the depth of the W2 learning notes: explanations, examples, trade-offs, warnings, mental models, and lab flow.
- Do not reduce the notes into shallow overview cards.
- Do not invent fake results. If a file/result is referenced, label it as lab artifact or expected output.

Overall learning story:
W2 continues from W1 detection/triage into root-cause analysis and production serving:
1. D1 turns alert noise into correlated alert clusters.
2. D2 turns clusters into root-cause hypotheses using graph, temporal evidence, incident retrieval, and classifier/LLM-augmented decision logic.
3. D3 turns the RCA pipeline into a production-style FastAPI service with health/readiness, metrics, logging, tests, and operational safeguards.

Required page structure:
1. Sticky course navigation and progress sidebar
2. W2 big-picture learning map
3. D1 — Alert Correlation: từ noise sang signal
4. D1 lab walkthrough
5. D2 — RCA: graph, causal, retrieval, kNN/LLM-augmented
6. D2 lab walkthrough
7. D3 — Model Serving: đưa pipeline lên production
8. D3 lab walkthrough
9. Offline W2 incident exercise / broken-system triage
10. Final review and checkpoint section

Every major concept must include:
1. Vietnamese explanation
2. Interactive visualization or animation
3. Connection to lab files
4. Checkpoint question with expandable answer
5. Common mistake or production warning

Required interactive visualizations:

1. Alert storm → correlation cluster
- Show many raw alerts arriving over time.
- Let the learner group alerts by time window, service, metric, severity, and fingerprint.
- Animate reduction from noisy alerts to fewer clusters.
- Display reduction ratio and cluster summary.
- Explain why alert correlation reduces cognitive load but can hide edge cases.

2. Service topology graph
- Show services and stores as nodes: edge-lb, auth-svc, checkout-svc, payment-svc, payments-db, catalog-svc, catalog-db, recommender-svc, cart-redis, notification-svc.
- Show dependency edges.
- Let learner click alerting services and see upstream/downstream impact.
- Explain blast radius and dependency-aware RCA.

3. Graph traversal RCA scoring
- Animate reverse traversal from alerting services toward upstream candidates.
- Show candidate scores based on depth, overlap, PageRank, and severity weight.
- Display the formula: score = (weighted_overlap * pagerank) / (depth + 1).
- Explain why upstream candidates can be more likely root causes.

4. Temporal causality / lag
- Show alert timelines for several services.
- Animate which service fires first.
- Visualize lag calculation and median time difference.
- Explain that the root cause often leads symptoms, but correlation is not proof.

5. Incident retrieval similarity
- Show a historical incident catalog.
- Let the learner compare current cluster to past incidents.
- Visualize weighted similarity:
  - services overlap 0.6
  - keyword overlap 0.3
  - severity match 0.1
- Explain Jaccard similarity and why similar past incidents speed up triage.

6. kNN / decision gate
- Show decision flow:
  if top incident similarity >= 0.3 → use graph + retrieval
  else → use graph-only heuristic
- Show confidence calculation.
- Show top-3 similar incidents.
- Explain why fallback logic matters in production.

7. LLM-augmented RCA safety layer
- Show LLM as an optional advisor, not the source of truth.
- Include feature flag / kill switch: AIOPS_USE_LLM.
- Show fallback when LLM fails or is disabled.
- Explain hallucination risk, grounding, and why deterministic evidence stays primary.

8. D3 FastAPI production pipeline
- Animate request flow:
  POST /incident → D1 alert correlation → D2 RCA pipeline → IncidentResponse.
- Show endpoints:
  GET /healthz
  GET /readyz
  GET /version
  POST /incident
  GET /metrics
- Explain health vs readiness separation.
- Show graph/history loading during lifespan startup.
- Show Prometheus metrics and structured JSON logs.

9. Observability of the RCA service
- Visualize request count, latency histogram, LLM failures, clusters per request.
- Explain why the AIOps system itself must be observable.

10. Testing and production readiness
- Show unit tests vs integration tests.
- Explain why FastAPI lifespan needs real uvicorn for full integration tests.
- Show test flow: start server → wait for readyz → call endpoints → assert response.

Lab file cards:

D1 files:
- w2/d1/assignment.ipynb — student notebook for alert correlation
- w2/d1/correlate.py — runnable CLI correlation pipeline
- w2/d1/dataset/alerts_sample.jsonl — raw alert stream
- w2/d1/dataset/services.json — topology/services metadata
- w2/d1/results/cluster_summary.json — correlated cluster output
- w2/d1/SUBMIT.md — submission checklist

D2 files:
- w2/d2/assignment.ipynb — RCA notebook
- w2/d2/correlate.py — 4-layer RCA CLI pipeline
- w2/d2/run_rca.py — quick runner if present
- w2/d2/dataset/cluster_summary.json — D1 output used as D2 input
- w2/d2/dataset/alerts_sample.jsonl — full alerts used for temporal evidence
- w2/d2/dataset/services.json — topology graph source
- w2/d2/dataset/incidents_history.json — retrieval/history catalog
- w2/d2/results/rca_output.json — RCA result output

D3 files:
- w2/d3/serve.py — FastAPI serving layer
- w2/d3/DESIGN.md — architecture and production design explanation
- w2/d3/SUBMIT.md — submission checklist
- w2/d3/requirements.txt — dependencies
- w2/d3/tests/test_serve.py — unit/integration tests
- w2/d3/dataset/alerts_sample.jsonl — request/sample alerts
- w2/d3/dataset/cluster_summary.json — cluster input/reference
- w2/d3/dataset/incidents_history.json — historical incident catalog
- w2/d3/dataset/services.json — topology graph source

Interaction requirements:
- Sticky progress sidebar
- Clickable W2 pipeline map
- Expand/collapse explanation cards
- Animated graph traversal
- Timeline/lag visualization
- Similarity scoring widget
- Decision-gate widget
- Endpoint explorer for D3
- Quiz/checkpoint reveal cards
- Lab file cards
- Scroll progress indicator
- “I understand this” checkmarks for major concepts

Quality bar before finalizing:
- Is this deep enough to learn from, not just look at?
- Are D1, D2, and D3 clearly separated?
- Does the site explain how W2 builds on W1?
- Are animations educational, not decorative?
- Are lab files connected to actual concepts?
- Is Vietnamese explanation substantial?
- Do all interactions work in preview?
- Is the selected Open Design design system preserved?

If any answer is no, fix the artifact before finishing.
```
