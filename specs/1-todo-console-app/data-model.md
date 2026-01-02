# Data Model: Todo Menu-Driven Python Console App with File Persistence

## Task Entity

### Attributes
- **id**: Integer (required, unique, auto-incremented starting from 1)
- **title**: String (required, max 200 characters)
- **description**: String (optional, max 1000 characters)
- **completed**: Boolean (required, default False)

### Validation Rules
- Title must not be empty or whitespace only
- ID must be unique within the application session
- ID must be a positive integer
- Completed field must be a boolean value

### State Transitions
- New task: completed=False (default)
- Mark complete: completed=False → completed=True
- Mark incomplete: completed=True → completed=False

### Relationships
- No relationships with other entities (standalone entity)

## File Storage Structure
- **tasks.json**: JSON file containing an array of Task objects
- Format: `[{"id": 1, "title": "Task 1", "description": "Description", "completed": false}, ...]`
- Auto-incremented ID tracking: separate counter stored in the application state to ensure sequential IDs across sessions