### 📁 `backlog/` (project root)
```
backlog/
├── backlog/                     # 📦 Python package root
│   ├── cli.py                   # 🚀 CLI entry point using `click`
│
│   ├── core/                    # 🧱 Core task logic (no AI dependencies)
│   │   ├── __init__.py
│   │   ├── models.py            # Task + Subtask dataclasses
│   │   ├── storage.py           # Load/save tasks.json
│   │   ├── task_ops.py          # Add/remove/update task logic
│   │   ├── markdown.py          # (Planned) Markdown file generator/parser
│   │   └── utils.py             # (Planned) Dependency resolution, formatting, etc.
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
├── tasks.json                   # 🧠 Source of truth for all task data
├── .env                         # 🔐 Local API keys / config
├── .env.example                 # 🧪 Shared example env file
├── .gitignore                   # 🚫 Ignore .venv, __pycache__, tasks/*.md, etc.
├── README.md                    # 📘 Setup + usage documentation
├── pyproject.toml               # 📦 Package + dependency config (PEP 621)
```

---

### 📌 Notes

- **`scripts/cli.py`** is the main entry point. You can symlink this for easier usage (`backlog` command).
- **`core/`** = all logic that doesn’t require AI. This is your foundation and runs even if OpenAI goes down.
- **`ai/`** = all model-specific logic. Easy to mock or switch to other LLMs later.
- **`tasks/`** = markdown export for human-readable editing and doc gen.
- **`.env`** for dev/test, pulled in with `python-dotenv` or `os.environ`.