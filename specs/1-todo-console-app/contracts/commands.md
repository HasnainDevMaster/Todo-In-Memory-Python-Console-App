# Command Contracts: Todo In-Memory Python Console App

## Command Interface Specification

### Add Task Command
- **Command**: `add`
- **Syntax**: `add "title" ["optional description"]`
- **Input**: Title (required string), Description (optional string)
- **Output**: Success message with assigned task ID
- **Errors**:
  - Missing title → "Error: Title is required"
  - Invalid format → "Error: Invalid command format"

### List Tasks Command
- **Command**: `list`
- **Syntax**: `list`
- **Input**: None
- **Output**: Formatted list of all tasks with status indicators
- **Errors**:
  - Empty list → "No tasks found"

### Update Task Command
- **Command**: `update`
- **Syntax**: `update <id> "new title" ["optional new description"]`
- **Input**: Task ID (required integer), new title (required string), new description (optional string)
- **Output**: Success confirmation
- **Errors**:
  - Invalid ID → "Task with ID [X] not found"
  - Missing ID → "Error: Task ID is required"

### Delete Task Command
- **Command**: `delete`
- **Syntax**: `delete <id>`
- **Input**: Task ID (required integer)
- **Output**: Success confirmation
- **Errors**:
  - Invalid ID → "Task with ID [X] not found"

### Complete Task Command
- **Command**: `complete`
- **Syntax**: `complete <id>`
- **Input**: Task ID (required integer)
- **Output**: Success confirmation
- **Errors**:
  - Invalid ID → "Task with ID [X] not found"

### Incomplete Task Command
- **Command**: `incomplete`
- **Syntax**: `incomplete <id>`
- **Input**: Task ID (required integer)
- **Output**: Success confirmation
- **Errors**:
  - Invalid ID → "Task with ID [X] not found"

### Exit Command
- **Command**: `exit`
- **Syntax**: `exit`
- **Input**: None
- **Output**: Application termination
- **Errors**: None