from backlog.core.models import Task
from uuid import uuid4

def generate_task_id(existing_tasks):
    return str(len(existing_tasks) + 1)

def add_task(title: str, description: str, priority: str, task_collection):
    task_id = generate_task_id(task_collection.tasks)
    task = Task(
        id=task_id,
        title=title,
        description=description,
        priority=priority
    )
    task_collection.tasks.append(task)
    return task
