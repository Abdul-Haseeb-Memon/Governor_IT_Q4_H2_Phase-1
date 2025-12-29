# CLI Contract: Delete Todo Command

**Feature**: 005-delete-todo
**Contract**: Delete Todo via Console
**Created**: 2025-12-29

## Command Definition

### Primary Command
```
python -m src.todo.main delete [ID]
```

### Parameters
- `ID` (required): UUID string identifying the todo to delete

## Input Validation

### ID Validation
- **Rule**: Must match existing todo item ID in memory
- **Format**: Valid UUID string format
- **Error**: "Todo item with ID [ID] not found" if ID doesn't exist

## Success Response

### Output Format
```
Todo deleted successfully!
ID: [UUID]
Title: [Title]
Description: [Description or "None" if empty]
Status: [Status]
```

### Success Conditions
- Todo item exists with given ID
- Deletion operation completes without error
- Todo is removed from memory
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
- Deletion operation is atomic: either fully succeeds or fails without partial changes
- If validation fails, original todo list remains unchanged

### Consistency
- After successful deletion, the specific todo is no longer available
- All other todos remain unchanged and accessible
- Deleted todo does not appear in list command results

### Concurrency
- Single-threaded operation (no concurrent access concerns)
- Deletions happen in same memory space as other operations

## Integration Points

### With TodoList
- Calls TodoList.delete_item() method
- Validates against TodoList.get_item() for ID existence
- Results visible through TodoList.get_all_items()

### With TodoView
- Deleted todos no longer appear in list command
- No additional synchronization required

## Edge Cases

### Non-existent ID
- When ID doesn't exist in the list, appropriate error message is returned
- No changes made to existing todo list

### Malformed ID
- Invalid UUID format should be treated as non-existent ID
- Error message indicates the ID was not found