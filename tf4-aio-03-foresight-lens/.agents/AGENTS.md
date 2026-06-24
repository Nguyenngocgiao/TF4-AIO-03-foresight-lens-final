# Workspace Rules for TF4 (AIO-03 Foresight Lens)

This repository is part of the XBrain AWS DevOps/CloudOps Foundation Program (Capstone Phase 2).
All AI agents (Gemini/Claude) operating in this workspace MUST STRICTLY follow these rules when assisting team members.

## 1. Jira & GitHub Smart Commits (CRITICAL)
- **Project Key:** TF4
- **Rule:** "No trace = no work". Every code change, documentation update, or lab experiment MUST be tied to a Jira ticket.
- **Commit Formatting:** When writing commit messages or creating Pull Requests, the agent MUST prefix the message with the relevant Jira ticket ID.
  - **Example:** `git commit -m "TF4-5: Implement multi-tenant routing for AI engine"`
  - **Failure to do this will result in the member not getting credit for their work.**
- If the user asks you to commit or push code, ALWAYS ask them for the Jira Ticket ID first if they haven't provided one.

## 2. Capstone Working Workflow
- Do not implement arbitrary features. Only work on Tasks defined in the Jira board for W11 and W12.
- Before modifying the AI engine logic (`engine.py`), ensure that the AI API Contract (`contracts/ai-api-contract.md`) is respected. The output must strictly match the JSON schema defined.
- Always include "Evidence" (screenshots, logs, metric outputs, or commit links) when completing a task, as required by the `Jira_Working_Rules.md`.

## 3. Communication
- If a CDO group member asks a question regarding the API, point them to the `contracts/` directory.
- For architectural decisions, always draft an ADR in `docs/05_adrs.md` before writing implementation code.
