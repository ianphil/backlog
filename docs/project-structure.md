### 📁 `backlog/` (project root)
```
backlog/
├── backlog/                     # 📦 Python package root
│   ├── cli.py                   # 🚀 CLI entry point using `click`
│
│   ├── core/                    # 🧱 Core task logic (no AI dependencies)
│   │   ├── __init__.py
│   │   ├── models.py            # Task + Subtask dataclasses
│   │   ├── storage.py           # Load/save tasks.json + meta updates
│   │   ├── task_ops.py          # Add/remove/update task logic
│   │   ├── markdown.py          # Markdown file generator for tasks
│   │   └── utils.py             # (Planned) Validation, dependency graph helpers
│
│   ├── ai/                      # 🤖 OpenAI integration (planned)
│   │   ├── __init__.py
│   │   ├── client.py            # OpenAI config + API wrapper
│   │   ├── prd_parser.py        # PRD → task breakdown
│   │   ├── task_expander.py     # Generate subtasks with LLM
│   │   └── drift_handler.py     # Handle rewrites, dependency drift, etc.
│
├── tasks/                       # 📄 Generated task markdown files
│   ├── task_001.md
│   └── ...
│
├── tests/                       # 🧪 Test suite
│   ├── __init__.py              # Optional
│   ├── test_cli.py              # Full CLI integration tests
│   ├── test_task_add.py         # Add task slice test (CLI + JSON + .md)
│   └── conftest.py              # Shared fixtures (e.g. task_data factory)
│
├── tasks.json                   # 🧠 Source of truth for all task data
├── .env                         # 🔐 Local API keys / config
├── .env.example                 # 🧪 Shared example env file
├── .gitignore                   # 🚫 Ignore .venv, __pycache__, task_*.md, etc.
├── README.md                    # 📘 Setup + usage documentation
├── pyproject.toml               # 📦 Package + dependency config (PEP 621)
```

---

### 📌 Notes

- **`backlog/cli.py`** is the main entry point. You can symlink this for easier usage (`backlog` command).
- **`core/`** = all logic that doesn’t require AI. This is your foundation and runs even if OpenAI goes down.
- **`ai/`** = all model-specific logic. Easy to mock or switch to other LLMs later.
- **`tasks/`** = markdown export for human-readable editing and doc gen.
- **`tests/`** = contains unit and integration tests to ensure the reliability of core and AI features.
- **`.env`** for dev/test, pulled in with `python-dotenv` or `os.environ`.