# Agent Workflow for Neurox-Agent

This repository hosts a Python application that provides a CLI and web interface for a self-improving assistant. The project uses `uv` for environment management, `pytest` for testing and `ruff` for linting.

The following guidelines help the AI contributor deliver clean pull requests and implement features effectively.

## 1. Preparation
- **Understand the code**: read `readme.md` and inspect recent commits with `git log` to learn ongoing work.
- **Discover tasks**: open `todo.md` if present. If not, analyze issues and user prompts to create a task entry before coding.
- **Plan deeply**: outline which files will change, write a plan under `plans/{task}.md`, and consider how changes impact existing tests and tools.

## 2. Coding Standards
- Target **Python 3.9+** with type hints and docstrings.
- Keep functions small and focused. Reuse utilities under `tools/` when possible.
- Avoid committing generated files, `__pycache__`, or anything ignored by `.gitignore`.

## 3. Workflow
1. Design failing tests first when adding new features.
2. Implement the feature following the plan.
3. Run quality checks:
   ```bash
   ruff .
   pytest -q
   ```
4. If commands fail due to missing dependencies or network restrictions, note it in the PR description.
5. Update documentation when behavior or APIs change.

## 4. Commit Messages
- Use the form `<type>: <summary>` with `feat`, `fix`, `docs`, `refactor`, or `chore`.
- Keep the summary under 72 characters and write in present tense.
- Example: `feat: add screenshot tool`.

## 5. Pull Requests
- Ensure `git status` shows a clean workspace before creating the PR.
- Summarize key changes by referencing line numbers in the PR body.
- Link the related task or plan file, marking it complete when merged.
- If builds or tests fail due to missing network access, mention this in the PR.

## 6. Self‑Reflection Checklist
Before finalizing a PR, verify:
1. **Accuracy** – Code runs and matches the plan.
2. **Clarity** – Names, comments, and commit message clearly express intent.
3. **Efficiency** – Implementation reuses existing utilities and stays lean.
4. **Documentation** – README or inline comments updated if needed.

Adhering to this workflow will help keep PRs focused, maintainable and easy to review.
