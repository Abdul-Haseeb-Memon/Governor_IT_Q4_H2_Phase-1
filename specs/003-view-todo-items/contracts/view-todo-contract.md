# API Contract: View Todo Items

## Endpoint: `todo list` or `todo view`

**Purpose**: Display all Todo items currently stored in memory via console

### Request

**Command**: `todo list`

**Parameters**: None required

**CLI Format**:
```bash
python -m todo.main list
```

### Response

**Success (with todos)**:
- **Status**: 200 OK (conceptual, CLI returns exit code 0)
- **Output**:
  ```
  [550e8400-e29b-41d4-a716-446655440000] Buy groceries - incomplete
      Description: Milk, bread, eggs
  [550e8400-e29b-41d4-a716-446655440001] Complete project - complete
      Description: Finish the todo app implementation
  ```

**Success (no todos)**:
- **Status**: 200 OK (conceptual, CLI returns exit code 0)
- **Output**:
  ```
  No tasks found.
  ```

### Validation Rules

**Input Validation**:
- No input validation required (command takes no parameters)

**Business Rules**:
- All stored todos must be displayed
- Each todo must show ID, title, and status
- Description should be shown if it exists
- Format must be clear and readable in console
- Empty state must be handled gracefully

### Examples

**Command with todos present**:
```bash
python -m todo.main list
```

**Response with todos**:
```
[550e8400-e29b-41d4-a716-446655440000] Buy groceries - incomplete
    Description: Milk, bread, eggs
[550e8400-e29b-41d4-a716-446655440001] Complete project - complete
    Description: Finish the todo app implementation
```

**Command with no todos**:
```bash
python -m todo.main list
```

**Response when empty**:
```
No tasks found.
```

### State Changes

**Before**: None
**After**: Todos displayed in console (no state change)