# Quickstart Guide: View Todo Items

## Feature Overview

The View Todo Items feature allows users to display all Todo items currently stored in memory. Each todo is displayed with its ID, title, description, and status.

## Getting Started

### Prerequisites

- Python 3.13+ installed and configured
- Project dependencies installed via UV
- Environment properly set up (completed in Phase 1)
- At least one todo item added (using the add command)

### Basic Usage

To view all todos in memory:
```bash
python -m todo.main list
```

### Example Commands

1. View all todos:
   ```bash
   python -m todo.main list
   ```

2. Add a todo and then view all todos:
   ```bash
   python -m todo.main add "Complete documentation" "Write user guides"
   python -m todo.main list
   ```

## Expected Output

On successful view with todos present:
```
[550e8400-e29b-41d4-a716-446655440000] Buy groceries - incomplete
    Description: Milk, bread, eggs
[550e8400-e29b-41d4-a716-446655440001] Complete project - complete
    Description: Finish the todo app implementation
```

On successful view with no todos:
```
No tasks found.
```

## Integration Points

- The view functionality integrates with the existing CLI framework in `src/todo/main.py`
- Todo items are accessed from the existing data model in `src/todo/model.py`
- The functionality works with the add functionality (from Spec 2)

## Development Workflow

1. Run the application with the list command
2. Verify all todos are displayed correctly
3. Test with empty list to ensure proper message
4. Verify all required fields are shown (ID, title, description, status)