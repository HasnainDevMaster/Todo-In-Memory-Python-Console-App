from typing import List, Optional
import sys
import json
from pathlib import Path

# Add the src directory to the path so imports work correctly
src_dir = Path(__file__).parent.parent
sys.path.insert(0, str(src_dir))

from models.task import Task


class TodoService:
    """
    Service class handling all business logic for task operations.
    Manages in-memory storage of tasks with sequential ID generation.
    """

    def __init__(self):
        """
        Initialize the TodoService with empty task list and ID counter.
        """
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and optional description.

        Args:
            title (str): Title of the task (required)
            description (str): Optional description of the task

        Returns:
            Task: The newly created task with assigned ID

        Raises:
            ValueError: If title is empty or whitespace only
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")

        task = Task(task_id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        self.next_id += 1

        # Auto-save after adding task
        self._auto_save()

        return task

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List[Task]: List of all tasks in insertion order
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): ID of the task to find

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if task was updated, False if task not found

        Raises:
            ValueError: If title is provided but is empty or whitespace only
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # If title is provided, validate it
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Title must be a non-empty string")
            task.title = title.strip()

        # If description is provided, update it
        if description is not None:
            task.description = description.strip()

        # Auto-save after updating task
        self._auto_save()

        return True

    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed

        # Auto-save after toggling completion status
        self._auto_save()

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)

        # Auto-save after deleting task
        self._auto_save()

        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next ID that will be assigned
        """
        return self.next_id

    def load_tasks(self, filename: str = "tasks.json") -> None:
        """
        Load tasks from a JSON file on startup.

        Args:
            filename (str): Name of the file to load tasks from (default: tasks.json)
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Clear existing tasks
                self.tasks.clear()

                # Load tasks from the file
                for task_data in data:
                    task = Task.from_dict(task_data)
                    self.tasks.append(task)

                    # Update next_id to be one more than the highest ID found
                    if task.id >= self.next_id:
                        self.next_id = task.id + 1

        except FileNotFoundError:
            # If file doesn't exist, start with empty task list
            self.tasks = []
            self.next_id = 1
        except (json.JSONDecodeError, KeyError, ValueError):
            # If file is corrupt or has invalid data, start with empty task list
            print("Warning: Could not load tasks from file due to corruption. Starting with empty task list.")
            self.tasks = []
            self.next_id = 1

    def save_tasks(self, filename: str = "tasks.json") -> None:
        """
        Save current tasks to a JSON file (pretty-printed).

        Args:
            filename (str): Name of the file to save tasks to (default: tasks.json)
        """
        try:
            tasks_data = [task.to_dict() for task in self.tasks]
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(tasks_data, file, indent=2, ensure_ascii=False)
        except IOError:
            print(f"Warning: Could not save tasks to {filename}")

    def _auto_save(self, filename: str = "tasks.json") -> None:
        """
        Automatically save tasks after every mutating operation.

        Args:
            filename (str): Name of the file to save tasks to (default: tasks.json)
        """
        self.save_tasks(filename)