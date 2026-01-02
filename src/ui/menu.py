from typing import Optional
from services.todo_service import TodoService


class Menu:
    """
    Menu class handling the display and user interaction for the todo application.
    Provides a menu-driven interface with numbered options.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the Menu with a TodoService instance.

        Args:
            todo_service (TodoService): The service to handle task operations
        """
        self.todo_service = todo_service

    def display_menu(self) -> None:
        """Display the main menu options to the user."""
        print("\n" + "="*40)
        print("TODO APPLICATION - MENU")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's menu choice
        """
        return input("Enter your choice (1-6): ").strip()

    def handle_add_task(self) -> None:
        """Handle the add task menu option."""
        print("\n--- Add New Task ---")
        title = input("Enter task title (required): ").strip()

        if not title:
            print("Error: Title is required")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()

        try:
            task = self.todo_service.add_task(title, description)
            print(f"Success: Task added with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_tasks(self) -> None:
        """Handle the view tasks menu option."""
        print("\n--- Task List ---")
        tasks = self.todo_service.list_tasks()

        if not tasks:
            print("No tasks found")
            return

        for task in tasks:
            print(task)

    def handle_update_task(self) -> None:
        """Handle the update task menu option."""
        print("\n--- Update Task ---")
        task_id_str = input("Enter task ID to update: ").strip()

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Task ID must be a number")
            return

        task = self.todo_service.get_task_by_id(task_id)
        if task is None:
            print(f"Task with ID {task_id} not found")
            return

        print(f"Current task: {task}")
        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()

        # Prepare update parameters
        title_update = new_title if new_title else None
        description_update = new_description if new_description else None

        # If user entered empty string, treat as wanting to clear the description
        if new_description == "":
            description_update = ""

        try:
            if self.todo_service.update_task(task_id, title_update, description_update):
                print("Success: Task updated")
            else:
                print(f"Task with ID {task_id} not found")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_toggle_complete(self) -> None:
        """Handle the mark task as complete menu option."""
        print("\n--- Mark Task as Complete ---")
        task_id_str = input("Enter task ID to toggle completion: ").strip()

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Task ID must be a number")
            return

        if self.todo_service.toggle_complete(task_id):
            task = self.todo_service.get_task_by_id(task_id)
            status = "completed" if task.completed else "incomplete"
            print(f"Success: Task {task_id} marked as {status}")
        else:
            print(f"Task with ID {task_id} not found")

    def handle_delete_task(self) -> None:
        """Handle the delete task menu option."""
        print("\n--- Delete Task ---")
        task_id_str = input("Enter task ID to delete: ").strip()

        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Task ID must be a number")
            return

        if self.todo_service.delete_task(task_id):
            print(f"Success: Task {task_id} deleted")
        else:
            print(f"Task with ID {task_id} not found")

    def handle_choice(self, choice: str) -> bool:
        """
        Handle the user's menu choice.

        Args:
            choice (str): The user's menu choice

        Returns:
            bool: True if the application should continue, False to exit
        """
        if choice == "1":
            self.handle_add_task()
        elif choice == "2":
            self.handle_view_tasks()
        elif choice == "3":
            self.handle_update_task()
        elif choice == "4":
            self.handle_toggle_complete()
        elif choice == "5":
            self.handle_delete_task()
        elif choice == "6":
            print("Thank you for using the Todo Application. Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        return True