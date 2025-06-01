# Plan: Add project documentation

## Goal
Create missing project documentation files and diagrams based on the current repository. Implement PRD with milestones and create TODO lists. Update README and add architecture diagram. No code changes to application logic.

## Steps
1. Create `PRD.md` describing project vision, features and milestones (short-, mid-, long-term).
2. Create `Diagram.md` with a mermaid diagram representing high level architecture (web UI, CLI, tools, core assistant, external APIs).
3. Update `readme.md` with a brief note linking to PRD and diagram.
4. Generate `TODO.md` with short term tasks derived from PRD. Generate `TODO.next.md` for mid/long tasks.
5. Ensure plan and docs follow repository instructions in `AGENTS.md`.
6. Run `ruff .` and `pytest -q` to verify no lint or test regressions.

## Impact
- Adds documentation only; no changes to runtime code.
- Should not affect tests.
