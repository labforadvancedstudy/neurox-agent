# Plan T2: Add basic CI script

## Goal
Add a GitHub Actions workflow that runs `ruff` and `pytest` on each push.

## Steps
1. Create `.github/workflows/ci.yml` workflow.
   - Use `actions/setup-python` to install Python 3.11.
   - Install project with dev dependencies using `pip install .[dev]`.
   - Run `ruff .` and `pytest -q`.
2. Run `ruff .` and `pytest -q` locally to ensure the repository passes.
3. Update `TODO.md` to mark **T2** as completed.

## Impact
- Adds CI for linting and tests, improving code quality.
