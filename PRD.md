# Product Requirements Document (PRD)

## Overview
`neurox-agent` (Claude Engineer v3) is a Python based assistant that combines a CLI and web interface to interact with Anthropic's Claude model. It dynamically loads tools for file management, web scraping and code execution, and can even create new tools autonomously. The goal is to provide a self‑improving framework that developers can use to automate tasks and extend capabilities during conversation.

## Goals
- Offer both CLI and web UI for interacting with Claude
- Support dynamic tool loading and creation
- Track token usage and conversation history
- Provide rich debugging output and progress indicators
- Remain easy to extend and deploy

## Architecture

The project consists of several layers:

1. **Interfaces** – a command line client and a web UI for chatting with the assistant.
2. **Core Assistant** – controls conversation flow and communicates with external services.
3. **Tool Loader** – discovers built-in and generated tools at runtime.
4. **Token Manager** – tracks token usage and enforces limits.
5. **History Store** – stores recent messages for context during a session.
6. **External Services** – calls the Anthropic API for responses and the E2B sandbox to run generated code safely.

See `Diagram.md` for a high level view of these components.

## Milestones
### Short‑Term (within 1 week)
1. **Documentation completeness** – add architecture diagram and PRD (this document)
2. **Task tracking** – maintain TODO lists for upcoming work
3. **Basic CI** – ensure linting and tests run locally (ruff + pytest)

### Mid‑Term (within 1 month)
1. **Improve test coverage** across existing tools and assistant logic
2. **Package distribution** via PyPI including project metadata
3. **Docker support** for easy deployment of the web UI

### Long‑Term (within 3 months)
1. **Plugin ecosystem** allowing external developers to register new tools
2. **Advanced conversation analytics** with persistent storage
3. **Continuous integration** with automated deployment pipelines

## References
- `readme.md` – installation, usage and tool descriptions
- `tools/` – collection of builtin tools
- `templates/` & `static/` – web interface assets
