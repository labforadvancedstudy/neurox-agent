from pathlib import Path


def test_ci_workflow_exists_and_has_steps():
    ci_path = Path('.github/workflows/ci.yml')
    assert ci_path.exists(), "ci.yml workflow missing"
    content = ci_path.read_text(encoding='utf-8')
    assert 'ruff' in content and 'pytest' in content, 'workflow must run ruff and pytest'
