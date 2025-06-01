import pathlib

def test_prd_has_architecture_section():
    prd_path = pathlib.Path('PRD.md')
    content = prd_path.read_text(encoding='utf-8')
    assert '## Architecture' in content
