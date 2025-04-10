from pathlib import Path
from backlog.core.models import Task

TASK_MD_DIR = Path("tasks")
TASK_MD_DIR.mkdir(exist_ok=True)

def generate_markdown(task: Task) -> str:
    md = f"""# Task {task.id}: {task.title}

- **Status**: `{task.status}`
- **Priority**: `{task.priority}`
- **Dependencies**: `{', '.join(task.dependencies) or 'None'}`

## Description
{task.description}

## Details
{task.details or 'N/A'}

## Test Strategy
{task.testStrategy or 'N/A'}

## Subtasks
"""
    for sub in task.subtasks:
        box = "[x]" if sub.status == "done" else "[ ]"
        md += f"- {box} **{sub.id}**: {sub.title} - {sub.description} (`{sub.status}`)\n"
        md += f"  - *Acceptance Criteria*: {sub.acceptanceCriteria or 'N/A'}\n"

    return md

def write_markdown_file(task: Task):
    filename = TASK_MD_DIR / f"task_{int(task.id):03}.md"
    content = generate_markdown(task)
    filename.write_text(content)
    return filename
