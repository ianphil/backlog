import pytest
from backlog.core.models import Task, TaskCollection
from backlog.core.task_ops import add_task

def create_sample_task_collection():
    return TaskCollection(meta=TaskCollection.default_meta(), tasks=[])

@pytest.fixture
def task_data():
    tc = create_sample_task_collection()
    task = add_task("Sample Task", "Sample description", "medium", tc)
    return tc, task
