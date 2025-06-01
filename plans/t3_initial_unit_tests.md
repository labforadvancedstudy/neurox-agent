# Plan T3: Initial unit tests

## Goal
Create basic unit tests covering the Assistant reset functionality and one built-in tool (FileCreatorTool).

## Steps
1. Create `tests/test_assistant_reset.py`:
   - Mock `anthropic` client to avoid dependency.
   - Patch `Config.ANTHROPIC_API_KEY` and `Assistant._load_tools`.
   - Verify `reset()` clears conversation history and token count.
2. Create `tests/test_file_creator_tool.py`:
   - Use pytest `tmp_path` fixture to create a temporary file.
   - Call `FileCreatorTool.execute` with a single file specification.
   - Assert file contents and JSON result show success.
3. Run `ruff .` and `pytest -q` to ensure tests and lint pass.
4. Update `TODO.md` to mark **T3** as completed.

## Impact
Adds first unit tests to the project, improving reliability and enabling future CI checks.
