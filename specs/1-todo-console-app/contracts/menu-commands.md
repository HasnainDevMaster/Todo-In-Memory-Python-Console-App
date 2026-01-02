# Menu Command Contracts: Todo Menu-Driven Python Console App

## Menu Interface Specification

### Main Menu Options
1. **Add Task** - Add a new task with title and optional description
   - Input: Title (required), Description (optional)
   - Output: Success message with assigned task ID
   - Errors:
     - Missing title → "Error: Title is required"
     - File save error → "Warning: Could not save task to file"

2. **View Tasks** - Display all tasks with status indicators
   - Input: None
   - Output: Formatted list of all tasks with status indicators
   - Errors:
     - Empty list → "No tasks found"
     - File load error → "Warning: Could not load tasks from file"

3. **Update Task** - Modify an existing task's details
   - Input: Task ID (required integer), new title (required), new description (optional)
   - Output: Success confirmation
   - Errors:
     - Invalid ID → "Task with ID [X] not found"
     - Missing ID → "Error: Task ID is required"
     - File save error → "Warning: Could not save task to file"

4. **Delete Task** - Remove a task by its ID
   - Input: Task ID (required integer)
   - Output: Success confirmation
   - Errors:
     - Invalid ID → "Task with ID [X] not found"
     - File save error → "Warning: Could not save task list to file"

5. **Mark Task as Complete** - Toggle completion status of a task
   - Input: Task ID (required integer)
   - Output: Success confirmation
   - Errors:
     - Invalid ID → "Task with ID [X] not found"
     - File save error → "Warning: Could not save task to file"

6. **Exit** - Close the application
   - Input: None
   - Output: Application termination
   - Errors: None