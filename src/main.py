#!/usr/bin/env python3
"""
Main entry point for the Todo Console Application.

This application provides a menu-driven interface for managing tasks with file-based persistence.
"""

import sys
from pathlib import Path

# Add the project root directory to the path so imports work correctly
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from services.todo_service import TodoService
from ui.menu import Menu


def main():
    """
    Main function to run the Todo Console Application.
    Initializes services, loads existing tasks, and runs the menu-driven loop.
    """
    print("Welcome to the Todo Application!")
    print("Loading tasks from file...")

    # Initialize the TodoService
    todo_service = TodoService()

    # Load existing tasks from file
    todo_service.load_tasks()

    # Initialize the Menu
    menu = Menu(todo_service)

    # Display welcome message
    print("Tasks loaded successfully!")
    print("Starting menu-driven interface...")

    # Main application loop
    running = True
    while running:
        menu.display_menu()
        choice = menu.get_user_choice()
        running = menu.handle_choice(choice)

    print("Application closed.")


if __name__ == "__main__":
    main()