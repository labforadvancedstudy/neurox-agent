# Plan T1: Finalize PRD and Diagram

## Goal
Improve existing documentation so that PRD.md and Diagram.md fully describe the project architecture and goals. After completion, mark T1 as complete in TODO.md.

## Steps
1. Expand `PRD.md` with an Architecture section referencing the diagram and explaining major components (CLI, Web UI, Assistant, Tool Loader, Token Manager, History Store, external APIs).
2. Update `Diagram.md` mermaid diagram to include Token Manager and History Store nodes connected to the Assistant.
3. Review `readme.md` references to ensure they still point to updated docs (already okay).
4. Run `ruff check .` and `pytest -q` to confirm linting and tests (may fail due to missing dependencies but run and capture output).
5. Update `TODO.md` to mark **T1** as completed.
