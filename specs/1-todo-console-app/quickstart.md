# Quickstart Guide: Todo Menu-Driven Python Console App

## Getting Started

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application: `python src/main.py`
4. The menu-driven interface will start, showing numbered options

## Menu Options

- 1. Add Task - Add a new task with title and description
- 2. View Tasks - View all tasks with status indicators
- 3. Update Task - Update a task's details by ID
- 4. Delete Task - Delete a task by ID
- 5. Mark Task as Complete - Toggle completion status
- 6. Exit - Exit the application

## Example Usage

```
Todo Console App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Task added with ID: 1

Todo Console App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Choose an option: 2
[ ] 1: Buy groceries - Milk, bread, eggs

Todo Console App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Choose an option: 5
Enter task ID to mark as complete: 1
Task 1 marked as complete

Todo Console App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Choose an option: 2
[x] 1: Buy groceries - Milk, bread, eggs

Todo Console App
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Choose an option: 6
```

## Persistence

- Tasks are automatically saved to tasks.json file after each operation
- Tasks persist across application sessions
- On startup, the application loads existing tasks from tasks.json if it exists
- If tasks.json doesn't exist, the application starts with an empty task list