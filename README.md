# 🧠 Backlog

**Backlog** is a CLI-driven task backlog manager designed for AI-first workflows. It organizes and expands development tasks using structured JSON + Markdown, with optional OpenAI integration for parsing PRDs and generating subtasks.

---

## 🚀 Features

- JSON + Markdown task management
- Command-line interface (CLI) built with `click`
- OpenAI integration for task parsing and subtask expansion (coming soon)
- Minimal file-based setup – no database required

---

## 🛠 Dev Environment Setup

### Prerequisites

- Python 3.8+
- [`uv`](https://github.com/astral-sh/uv) (fast Python dependency manager)

### Clone the repo

```bash
git clone https://github.com/your-username/backlog.git
cd backlog
```

### Run locally

```bash
uv pip install -e .
backlog task add --title "Fix import bug" --description "Adjust relative paths" --priority medium
```

### Tests
```bash
pytest tests/
```