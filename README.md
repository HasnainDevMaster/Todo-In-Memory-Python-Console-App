# Todo Menu-Driven Python Console App with File Persistence

A simple menu-driven todo application with file-based persistence that allows users to add, view, update, delete, and mark tasks as complete.

## Features

- Menu-driven interface with numbered options
- Add tasks with title and optional description
- View all tasks with status indicators and full details
- Update task details
- Delete tasks by ID
- Mark tasks as complete/incomplete
- File-based persistence using tasks.json
- Sequential task IDs that persist across sessions
- User-friendly error handling

## Requirements

- Python 3.13 or higher
- uv package manager (for dependency management)

## Setup

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies: `uv sync`

## Usage

Run the application:

```bash
uv run python src/main.py
```

The menu-driven interface will start. Available options include:

1. **Add Task** - Add a new task with title and optional description
2. **View Tasks** - Display all tasks with status indicators
3. **Update Task** - Modify an existing task's details
4. **Mark Task as Complete** - Toggle completion status of a task
5. **Delete Task** - Remove a task by its ID
6. **Exit** - Close the application

## Example Usage

```
========================================
TODO APPLICATION - MENU
========================================
1. Add Task
2. View Tasks
3. Update Task
4. Mark Task as Complete
5. Delete Task
6. Exit
========================================
Enter your choice (1-6): 1

--- Add New Task ---
Enter task title (required): Buy groceries
Enter task description (optional, press Enter to skip): Milk, bread, eggs
Success: Task added with ID 1

Enter your choice (1-6): 2

--- Task List ---
[x] 1: Buy groceries - Milk, bread, eggs

Enter your choice (1-6): 6
Thank you for using the Todo Application. Goodbye!
```

## Persistence

Tasks are automatically saved to `tasks.json` in the project root after every operation.
On startup, the application loads existing tasks from `tasks.json` if it exists.

## Development

For development, you can run:

- Run the application: `uv run python src/main.py`
- Run tests: `uv run python test_app.py`
- Check syntax: `uv run python -m py_compile src/**/*.py`

## Architecture

The application follows a clean architecture with separation of concerns:

- `src/models/task.py` - Task model definition with serialization support
- `src/services/todo_service.py` - Business logic for task operations with persistence
- `src/ui/menu.py` - Menu display and user interaction handling
- `src/main.py` - Main application entry point with menu-driven loop