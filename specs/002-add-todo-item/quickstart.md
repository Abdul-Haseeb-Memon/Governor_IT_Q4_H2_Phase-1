# Quickstart Guide: Add Todo Item

## Feature Overview

The Add Todo Item feature allows users to create new todo items with a title and optional description. Each todo is assigned a unique ID and default status of "incomplete", stored in memory for the current session.

## Getting Started

### Prerequisites

- Python 3.13+ installed and configured
- Project dependencies installed via UV
- Environment properly set up (completed in Phase 1)

### Basic Usage

To add a new todo with title and description:
```bash
python -m todo.main add "My Todo Title" "Optional description here"
```

To add a new todo with title only:
```bash
python -m todo.main add "My Todo Title"
```

### Example Commands

1. Add a simple todo:
   ```bash
   python -m todo.main add "Complete project documentation"
   ```

2. Add a todo with description:
   ```bash
   python -m todo.main add "Buy groceries" "Milk, bread, eggs, cheese"
   ```

3. Add a work-related todo:
   ```bash
   python -m todo.main add "Prepare presentation" "For the team meeting on Friday"
   ```

## Expected Output

On successful addition:
```
Todo added successfully!
ID: 550e8400-e29b-41d4-a716-446655440000
Title: Complete project documentation
Description: None
Status: incomplete
```

On validation error:
```
Error: Title cannot be empty or contain only whitespace
```

## Integration Points

- The add functionality integrates with the existing CLI framework in `src/todo/main.py`
- Todo items are stored in memory using the data model defined in `src/todo/model.py`
- The functionality supports the list/view functionality (to be implemented in Spec 3)

## Development Workflow

1. Run the application with the add command
2. Verify the todo is added successfully
3. Use the list command to confirm the todo appears in the collection
4. Test error conditions with empty titles