import sys
import types
from pathlib import Path

sys.modules['dotenv'] = types.SimpleNamespace(load_dotenv=lambda: None)
rich_stub = types.SimpleNamespace(
    console=types.SimpleNamespace(
        Console=type(
            "DummyConsole",
            (),
            {
                "print": lambda self, *a, **k: None,
            },
        )
    ),
    markdown=types.SimpleNamespace(Markdown=lambda text: text),
    live=types.SimpleNamespace(Live=object),
    spinner=types.SimpleNamespace(Spinner=object),
    panel=types.SimpleNamespace(Panel=object),
)
sys.modules['rich'] = rich_stub
sys.modules['rich.console'] = rich_stub.console
sys.modules['rich.markdown'] = rich_stub.markdown
sys.modules['rich.live'] = rich_stub.live
sys.modules['rich.spinner'] = rich_stub.spinner
sys.modules['rich.panel'] = rich_stub.panel
prompt_toolkit_stub = types.SimpleNamespace(
    prompt=lambda *a, **k: "",
    styles=types.SimpleNamespace(Style=object),
)
sys.modules['prompt_toolkit'] = prompt_toolkit_stub
sys.modules['prompt_toolkit.styles'] = prompt_toolkit_stub.styles

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import Config  # noqa: E402


# Provide a minimal stub for the anthropic client
class DummyMessages:
    def create(self, *args, **kwargs):
        return types.SimpleNamespace(stop_reason="stop", content=[])

class DummyClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.messages = DummyMessages()

def test_reset_clears_history_and_tokens(monkeypatch):
    sys.modules['anthropic'] = types.SimpleNamespace(Anthropic=DummyClient)

    from ce3 import Assistant  # import after stubbing anthropic

    monkeypatch.setattr(Config, "ANTHROPIC_API_KEY", "test")
    monkeypatch.setattr(Assistant, "_load_tools", lambda self: [])

    assistant = Assistant()
    assistant.conversation_history = [{"role": "user", "content": "hi"}]
    assistant.total_tokens_used = 10

    assistant.reset()

    assert assistant.conversation_history == []
    assert assistant.total_tokens_used == 0
