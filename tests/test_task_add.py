import json
import os
import subprocess
from pathlib import Path

def test_task_add_creates_json_and_md(tmp_path):
    os.chdir(tmp_path)

    # Run the CLI add command
    result = subprocess.run(
        [
            "backlog", "task", "add",
            "--title", "Test Task",
            "--description", "Task description",
            "--priority", "high"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "✅ Task [1] added: Test Task" in result.stdout

    # Validate tasks.json was created
    task_file = Path("tasks.json")
    assert task_file.exists()
    with open(task_file) as f:
        data = json.load(f)
        assert len(data["tasks"]) == 1
        assert data["tasks"][0]["title"] == "Test Task"

    # Validate Markdown file was generated
    md_file = Path("tasks/task_001.md")
    assert md_file.exists()
    content = md_file.read_text()
    assert "# Task 1: Test Task" in content
    assert "## Description\nTask description" in content
