import json
import os
import subprocess
from pathlib import Path


def test_task_list(tmp_path):
    """Test that task list command shows tasks and filters correctly"""
    os.chdir(tmp_path)

    # Add a couple of tasks first
    subprocess.run(
        [
            "backlog", "task", "add",
            "--title", "High priority task",
            "--description", "This is important",
            "--priority", "high"
        ],
        capture_output=True,
        text=True
    )

    subprocess.run(
        [
            "backlog", "task", "add",
            "--title", "Low priority task",
            "--description", "This can wait",
            "--priority", "low"
        ],
        capture_output=True,
        text=True
    )

    # Test listing all tasks
    result = subprocess.run(
        ["backlog", "task", "list"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "📋 Task List:" in result.stdout
    assert "High priority task" in result.stdout
    assert "Low priority task" in result.stdout

    # Test filtering by priority
    result = subprocess.run(
        ["backlog", "task", "list", "--priority", "high"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "filtered by: priority=high" in result.stdout
    assert "High priority task" in result.stdout
    assert "Low priority task" not in result.stdout