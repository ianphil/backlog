from backlog.core.models import Task
from uuid import uuid4
from typing import List, Optional

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

def filter_tasks(tasks: List[Task], status: Optional[str] = None, priority: Optional[str] = None) -> List[Task]:
    """Filter tasks based on status and/or priority criteria."""
    result = tasks
    
    if status:
        result = [task for task in result if task.status == status]
    
    if priority:
        result = [task for task in result if task.priority == priority]
    
    return result
