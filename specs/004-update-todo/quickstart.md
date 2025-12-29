# Quickstart: Update Todo Feature

**Feature**: 004-update-todo
**Created**: 2025-12-29

## Overview
The Update Todo feature allows users to modify the title and/or description of existing todo items in memory via console commands.

## Prerequisites
- Python 3.14+ installed
- Project repository cloned and set up
- Current working directory: project root

## Command Usage

### Update Todo Command
```bash
python -m src.todo.main update [ID] [TITLE] [DESCRIPTION?]
```

### Examples
1. **Update title only**:
   ```bash
   python -m src.todo.main update a27fc20c-d676-44a5-9636-d6ccd99c4192 "New Title"
   ```

2. **Update title and description**:
   ```bash
   python -m src.todo.main update a27fc20c-d676-44a5-9636-d6ccd99c4192 "New Title" "New Description"
   ```

3. **View updated todo**:
   ```bash
   python -m src.todo.main list
   ```

## Test Scenarios

### Scenario 1: Successful Update
1. Add a todo:
   ```bash
   python -m src.todo.main add "Original Title" "Original Description"
   ```
2. Note the ID from the output
3. Update the todo:
   ```bash
   python -m src.todo.main update [ID] "Updated Title" "Updated Description"
   ```
4. Verify the update:
   ```bash
   python -m src.todo.main list
   ```

### Scenario 2: Update with Invalid ID
1. Try to update with non-existent ID:
   ```bash
   python -m src.todo.main update invalid-id "New Title"
   ```
2. Verify error message appears

### Scenario 3: Update with Empty Title
1. Try to update with empty title:
   ```bash
   python -m src.todo.main update [ID] ""
   ```
2. Verify error message appears

## Expected Output

### Success
```
Todo updated successfully!
ID: [UUID]
Title: [Updated Title]
Description: [Updated Description or "None" if empty]
Status: [Current Status]
```

### Error Cases
- Invalid ID: "Error: Todo item with ID [ID] not found"
- Empty title: "Error: Title cannot be empty or contain only whitespace"

## Integration Testing
1. Update a todo
2. Verify changes appear in list view
3. Verify other todos remain unchanged
4. Verify todo status remains unchanged after update