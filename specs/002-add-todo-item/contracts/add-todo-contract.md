# API Contract: Add Todo

## Endpoint: `todo add`

**Purpose**: Add a new todo item to the in-memory collection

### Request

**Command**: `todo add [title] [description?]`

**Parameters**:
- `title` (string, required): Title of the new todo item
- `description` (string, optional): Description of the new todo item

**CLI Format**:
```bash
python -m todo.main add "My Todo Title" "Optional description here"
# or
python -m todo.main add "My Todo Title"  # without description
```

### Response

**Success**:
- **Status**: 200 OK (conceptual, CLI returns exit code 0)
- **Output**:
  ```
  Todo added successfully!
  ID: [generated-uuid]
  Title: [title]
  Description: [description or "None"]
  Status: incomplete
  ```
- **Side Effect**: Todo item is stored in memory with unique ID

**Error**:
- **Status**: 400 Bad Request (conceptual, CLI returns exit code 1)
- **Output**:
  ```
  Error: Title cannot be empty or contain only whitespace
  ```
- **Side Effect**: No todo item is stored

### Validation Rules

**Input Validation**:
- `title` must not be empty after whitespace trimming
- `title` must not contain only whitespace characters
- `description` can be any string (including empty)

**Business Rules**:
- A unique ID must be generated for each new todo
- Status must default to "incomplete"
- Todo must be retrievable after addition

### Examples

**Valid Request**:
```bash
python -m todo.main add "Buy groceries" "Milk, bread, eggs"
```

**Valid Response**:
```
Todo added successfully!
ID: 550e8400-e29b-41d4-a716-446655440000
Title: Buy groceries
Description: Milk, bread, eggs
Status: incomplete
```

**Invalid Request**:
```bash
python -m todo.main add "" "Description only"
```

**Invalid Response**:
```
Error: Title cannot be empty or contain only whitespace
```

### State Changes

**Before**: Todo list contains N items
**After (success)**: Todo list contains N+1 items, with new item having unique ID and incomplete status
**After (error)**: Todo list remains unchanged