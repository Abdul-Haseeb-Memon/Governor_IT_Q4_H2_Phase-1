# Quickstart: Delete Todo Feature

**Feature**: 005-delete-todo
**Created**: 2025-12-29

## Overview
The Delete Todo feature allows users to remove existing todo items from memory via console commands using the todo's ID.

## Prerequisites
- Python 3.14+ installed
- Project repository cloned and set up
- Current working directory: project root

## Command Usage

### Delete Todo Command
```bash
python -m src.todo.main delete [ID]
```

### Examples
1. **Delete a todo**:
   ```bash
   python -m src.todo.main delete a27fc20c-d676-44a5-9636-d6ccd99c4192
   ```

2. **View todos after deletion**:
   ```bash
   python -m src.todo.main list
   ```

3. **List todos to get an ID first**:
   ```bash
   python -m src.todo.main list
   ```

## Test Scenarios

### Scenario 1: Successful Deletion
1. Add a todo:
   ```bash
   python -m src.todo.main add "Test Todo" "Test Description"
   ```
2. Note the ID from the output
3. Delete the todo:
   ```bash
   python -m src.todo.main delete [ID]
   ```
4. Verify the deletion:
   ```bash
   python -m src.todo.main list
   ```

### Scenario 2: Delete with Invalid ID
1. Try to delete with non-existent ID:
   ```bash
   python -m src.todo.main delete invalid-id
   ```
2. Verify error message appears

## Expected Output

### Success
```
Todo deleted successfully!
ID: [UUID]
Title: [Title]
Description: [Description or "None" if empty]
Status: [Status]
```

### Error Cases
- Invalid ID: "Error: Todo item with ID [ID] not found"

## Integration Testing
1. Delete a todo
2. Verify it no longer appears in list view
3. Verify other todos remain unchanged
4. Verify the ID cannot be used for other operations after deletion