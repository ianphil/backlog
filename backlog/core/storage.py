import json
from pathlib import Path
from backlog.core.models import TaskCollection, Task
from dataclasses import asdict

TASK_FILE = Path("tasks.json")

def load_tasks() -> TaskCollection:
    if TASK_FILE.exists():
        with open(TASK_FILE) as f:
            data = json.load(f)
        tasks = [Task(**t) for t in data["tasks"]]
        return TaskCollection(meta=data["meta"], tasks=tasks)
    else:
        return TaskCollection(meta=TaskCollection.default_meta())

def save_tasks(task_collection: TaskCollection):
    with open(TASK_FILE, "w") as f:
        data = {
            "meta": task_collection.meta,
            "tasks": [asdict(t) for t in task_collection.tasks]
        }
        json.dump(data, f, indent=2)
