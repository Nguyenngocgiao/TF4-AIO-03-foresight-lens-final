---
name: capstone-docs-operator
description: Automates the execution of documentation and diagram scripts (fix_docs.py, generate_diagrams.py) when relevant code changes occur in the TF4 Capstone.
---

# Capstone Docs Operator

This skill ensures that whenever there is a structural change to the project or updates to the contracts/specs, the accompanying diagrams and docs are rebuilt and updated.

## Trigger Conditions
Use this skill whenever:
1. The user asks to "update docs", "sync docs", or "run docs pipeline".
2. You modify architectural contracts (`telemetry-contract.md`, `ai-api-contract.md`, `deployment-contract.md`) or specs (`docs/02_solution_design.md`, `docs/03_ai_engine_spec.md`).
3. You modify the `engine-skeleton` source code in a way that affects the API schema.

## Workflow
1. Execute the documentation scripts located in `scripts/`:
   - `python scripts/fix_docs.py` (or `update_docs.py` if present)
   - `python scripts/generate_diagrams.py`
2. Wait for the scripts to complete and verify the outputs (e.g., check that `.drawio` or `.png` files are updated).
3. Optionally run `git status` to see what files were modified by the scripts, and offer to commit them.

## Notes
- This ensures the CDO teams and Mentors always see the latest architectural diagrams and perfectly formatted markdown files in the Evidence Pack.
