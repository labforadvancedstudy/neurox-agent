import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.filecreatortool import FileCreatorTool


def test_file_creator_creates_file(tmp_path):
    tool = FileCreatorTool()
    file_path = tmp_path / "hello.txt"
    result_json = tool.execute(files={"path": str(file_path), "content": "hello"})

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == "hello"

    result = json.loads(result_json)
    assert result["created_files"] == 1
    assert result["failed_files"] == 0
    assert result["results"][0]["success"] is True
    assert Path(result["results"][0]["path"]) == file_path
