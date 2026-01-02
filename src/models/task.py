class Task:
    """
    Task model representing a single todo item.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task (required)
        description (str): Optional description of the task
        completed (bool): Completion status of the task (default False)
    """

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str): Optional description of the task
            completed (bool): Completion status of the task (default False)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")

        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed

    def __str__(self):
        """String representation of the task."""
        status = "[x]" if self.completed else "[ ]"
        desc_part = f" - {self.description}" if self.description else ""
        return f"{status} {self.id}: {self.title}{desc_part}"

    def __repr__(self):
        """Developer-friendly representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def to_dict(self):
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task instance from a dictionary representation."""
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )