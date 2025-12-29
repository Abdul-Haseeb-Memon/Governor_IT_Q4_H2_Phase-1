# CLI Contract: Mark Todo Complete/Incomplete Commands

**Feature**: 006-mark-todo
**Contract**: Mark Todo Status via Console
**Created**: 2025-12-29

## Command Definitions

### Complete Command
```
python -m src.todo.main complete [ID]
```

### Incomplete Command
```
python -m src.todo.main incomplete [ID]
```

### Parameters
- `ID` (required): UUID string identifying the todo to update status

## Input Validation

### ID Validation
- **Rule**: Must match existing todo item ID in memory
- **Format**: Valid UUID string format
- **Error**: "Todo item with ID [ID] not found" if ID doesn't exist

## Success Response

### Output Format
```
Todo status updated successfully!
ID: [UUID]
Title: [Title]
Description: [Description or "None" if empty]
Status: [New Status]
```

### Success Conditions
- Todo item exists with given ID
- Status update operation completes without error
- Todo reflects new status in memory
- Changes are reflected in subsequent operations

## Error Responses

### Invalid ID Error
```
Error: Todo item with ID [ID] not found
```

### General Error
```
Error: [Specific error message]
```

## Behavior Specifications

### Atomicity
- Status update operation is atomic: either fully succeeds or fails without partial changes
- If validation fails, original todo status remains unchanged

### Consistency
- After successful status update, the todo reflects the new status
- All other properties of the todo remain unchanged
- Updated status is immediately visible in list command results

### Concurrency
- Single-threaded operation (no concurrent access concerns)
- Status updates happen in same memory space as other operations

## Integration Points

### With TodoList
- Calls TodoList.update_item_status() method
- Validates against TodoList.get_item() for ID existence
- Results visible through TodoList.get_all_items()

### With TodoView
- Updated statuses appear in list command immediately
- No additional synchronization required

## Edge Cases

### Non-existent ID
- When ID doesn't exist in the list, appropriate error message is returned
- No changes made to existing todo list

### Malformed ID
- Invalid UUID format should be treated as non-existent ID
- Error message indicates the ID was not found

### Already Correct Status
- When item is already in requested status, update still succeeds
- Status remains unchanged but success message is displayed