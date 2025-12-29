# Quickstart: Mark Todo Complete/Incomplete Feature

**Feature**: 006-mark-todo
**Created**: 2025-12-29

## Overview
The Mark Todo Complete/Incomplete feature allows users to update the status of existing todo items from memory via console commands using the todo's ID.

## Prerequisites
- Python 3.14+ installed
- Project repository cloned and set up
- Current working directory: project root

## Command Usage

### Complete Todo Command
```bash
python -m src.todo.main complete [ID]
```

### Incomplete Todo Command
```bash
python -m src.todo.main incomplete [ID]
```

### Examples
1. **Mark a todo as complete**:
   ```bash
   python -m src.todo.main complete a27fc20c-d676-44a5-9636-d6ccd99c4192
   ```

2. **Mark a todo as incomplete**:
   ```bash
   python -m src.todo.main incomplete a27fc20c-d676-44a5-9636-d6ccd99c4192
   ```

3. **View todos after status change**:
   ```bash
   python -m src.todo.main list
   ```

4. **List todos to get an ID first**:
   ```bash
   python -m src.todo.main list
   ```

## Test Scenarios

### Scenario 1: Mark Todo as Complete
1. Add a todo:
   ```bash
   python -m src.todo.main add "Test Todo" "Test Description"
   ```
2. Note the ID from the output
3. Mark the todo as complete:
   ```bash
   python -m src.todo.main complete [ID]
   ```
4. Verify the status change:
   ```bash
   python -m src.todo.main list
   ```

### Scenario 2: Mark Todo as Incomplete
1. Add and complete a todo:
   ```bash
   python -m src.todo.main add "Test Todo" "Test Description"
   python -m src.todo.main complete [ID]
   ```
2. Mark the todo as incomplete:
   ```bash
   python -m src.todo.main incomplete [ID]
   ```
3. Verify the status change:
   ```bash
   python -m src.todo.main list
   ```

### Scenario 3: Status Update with Invalid ID
1. Try to update status with non-existent ID:
   ```bash
   python -m src.todo.main complete invalid-id
   ```
2. Verify error message appears

## Expected Output

### Success
```
Todo status updated successfully!
ID: [UUID]
Title: [Title]
Description: [Description or "None" if empty]
Status: [New Status]
```

### Error Cases
- Invalid ID: "Error: Todo item with ID [ID] not found"

## Integration Testing
1. Update a todo status
2. Verify it appears with correct status in list view
3. Verify other todos remain unchanged
4. Verify the ID can be used for other operations after status change