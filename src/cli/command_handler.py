import sys
from pathlib import Path

# Add the src directory to the path so imports work correctly
src_dir = Path(__file__).parent.parent
sys.path.insert(0, str(src_dir))

from services.todo_service import TodoService
from typing import List, Tuple
import re


class CommandHandler:
    """
    Handles parsing and execution of user commands for the todo application.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the command handler with a todo service instance.

        Args:
            todo_service (TodoService): The service to handle task operations
        """
        self.todo_service = todo_service

    def parse_command(self, user_input: str) -> Tuple[str, List[str]]:
        """
        Parse user input into command and arguments.
        Handles quoted strings as single arguments.

        Args:
            user_input (str): Raw user input

        Returns:
            Tuple[str, List[str]]: Command and list of arguments
        """
        # Use regex to handle quoted strings properly
        # This pattern matches either quoted strings or unquoted words
        pattern = r'"([^"]*)"|(\S+)'
        matches = re.findall(pattern, user_input.strip())

        # Each match is a tuple where either the quoted part or unquoted part is present
        tokens = [match[0] if match[0] else match[1] for match in matches]

        if not tokens:
            return "", []

        command = tokens[0].lower()
        args = tokens[1:]

        return command, args

    def handle_command(self, user_input: str) -> str:
        """
        Process a user command and return the appropriate response.

        Args:
            user_input (str): The raw user input command

        Returns:
            str: The response to display to the user
        """
        command, args = self.parse_command(user_input)

        if command == "add":
            return self._handle_add(args)
        elif command == "list":
            return self._handle_list(args)
        elif command == "update":
            return self._handle_update(args)
        elif command == "delete":
            return self._handle_delete(args)
        elif command == "complete":
            return self._handle_complete(args)
        elif command == "incomplete":
            return self._handle_incomplete(args)
        elif command == "help":
            return self._handle_help()
        elif command == "exit":
            return self._handle_exit()
        else:
            return f"Unknown command: {command}. Type 'help' for available commands."

    def _handle_add(self, args: List[str]) -> str:
        """
        Handle the 'add' command to create a new task.

        Args:
            args (List[str]): Arguments for the command [title, optional description]

        Returns:
            str: Response message
        """
        if len(args) < 1:
            return "Error: Title is required. Usage: add \"title\" [\"optional description\"]"

        title = args[0]
        description = args[1] if len(args) > 1 else ""

        try:
            task = self.todo_service.add_task(title, description)
            return f"Task added with ID: {task.id}"
        except ValueError as e:
            return f"Error: {str(e)}"

    def _handle_list(self, args: List[str]) -> str:
        """
        Handle the 'list' command to display all tasks.

        Args:
            args (List[str]): Arguments for the command (should be empty)

        Returns:
            str: Response message with task list
        """
        if args:
            return "Usage: list (no arguments required)"

        tasks = self.todo_service.list_tasks()

        if not tasks:
            return "No tasks found"

        # Format each task with its string representation
        task_list = [str(task) for task in tasks]
        return "\n".join(task_list)

    def _handle_update(self, args: List[str]) -> str:
        """
        Handle the 'update' command to modify a task.

        Args:
            args (List[str]): Arguments for the command [id, new_title, optional new_description]

        Returns:
            str: Response message
        """
        if len(args) < 2:
            return "Error: Task ID and new title are required. Usage: update <id> \"new title\" [\"optional new description\"]"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be an integer"

        new_title = args[1]
        new_description = args[2] if len(args) > 2 else None

        try:
            updated = self.todo_service.update_task(task_id, new_title, new_description)
            if updated:
                return f"Task {task_id} updated successfully"
            else:
                return f"Task with ID {task_id} not found"
        except ValueError as e:
            return f"Error: {str(e)}"

    def _handle_delete(self, args: List[str]) -> str:
        """
        Handle the 'delete' command to remove a task.

        Args:
            args (List[str]): Arguments for the command [id]

        Returns:
            str: Response message
        """
        if len(args) != 1:
            return "Error: Task ID is required. Usage: delete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be an integer"

        deleted = self.todo_service.delete_task(task_id)
        if deleted:
            return f"Task {task_id} deleted successfully"
        else:
            return f"Task with ID {task_id} not found"

    def _handle_complete(self, args: List[str]) -> str:
        """
        Handle the 'complete' command to mark a task as complete.

        Args:
            args (List[str]): Arguments for the command [id]

        Returns:
            str: Response message
        """
        if len(args) != 1:
            return "Error: Task ID is required. Usage: complete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be an integer"

        toggled = self.todo_service.toggle_complete(task_id)
        if toggled:
            task = self.todo_service.get_task_by_id(task_id)
            status = "complete" if task.completed else "incomplete"
            return f"Task {task_id} marked as {status}"
        else:
            return f"Task with ID {task_id} not found"

    def _handle_incomplete(self, args: List[str]) -> str:
        """
        Handle the 'incomplete' command to mark a task as incomplete.

        Args:
            args (List[str]): Arguments for the command [id]

        Returns:
            str: Response message
        """
        if len(args) != 1:
            return "Error: Task ID is required. Usage: incomplete <id>"

        try:
            task_id = int(args[0])
        except ValueError:
            return "Error: Task ID must be an integer"

        toggled = self.todo_service.toggle_complete(task_id)
        if toggled:
            # Toggle again to ensure it's incomplete
            self.todo_service.toggle_complete(task_id)
            return f"Task {task_id} marked as incomplete"
        else:
            return f"Task with ID {task_id} not found"

    def _handle_help(self) -> str:
        """
        Handle the 'help' command to display available commands.

        Returns:
            str: Help message with available commands
        """
        help_text = """
Available commands:
  add "title" ["optional description"]    - Add a new task
  list                                  - View all tasks with status indicators
  update <id> "new title" ["new desc"]  - Update a task
  delete <id>                           - Delete a task by ID
  complete <id>                         - Mark a task as complete
  incomplete <id>                       - Mark a task as incomplete
  help                                  - Show this help message
  exit                                  - Exit the application
        """.strip()
        return help_text

    def _handle_exit(self) -> str:
        """
        Handle the 'exit' command.

        Returns:
            str: Special exit signal
        """
        return "EXIT"