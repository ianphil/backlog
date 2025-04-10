from dataclasses import dataclass, field
from typing import List, Optional
import datetime

@dataclass
class Subtask:
    id: str
    title: str
    description: str
    status: str = "pending"
    dependencies: List[str] = field(default_factory=list)
    acceptanceCriteria: Optional[str] = None

@dataclass
class Task:
    id: str
    title: str
    description: str
    status: str = "pending"
    priority: str = "medium"
    dependencies: List[str] = field(default_factory=list)
    details: Optional[str] = ""
    testStrategy: Optional[str] = ""
    subtasks: List[Subtask] = field(default_factory=list)

@dataclass
class TaskCollection:
    meta: dict
    tasks: List[Task] = field(default_factory=list)

    @staticmethod
    def default_meta():
        now = datetime.datetime.now().isoformat()
        return {
            "projectName": "Backlog Project",
            "version": "0.1.0",
            "createdAt": now,
            "updatedAt": now,
        }
