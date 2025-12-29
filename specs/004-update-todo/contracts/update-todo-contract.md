# CLI Contract: Update Todo Command

**Feature**: 004-update-todo
**Contract**: Update Todo via Console
**Created**: 2025-12-29

## Command Definition

### Primary Command
```
python -m src.todo.main update [ID] [TITLE] [DESCRIPTION?]
```

### Parameters
- `ID` (required): UUID string identifying the todo to update
- `TITLE` (required): New title for the todo (must be non-empty)
- `DESCRIPTION` (optional): New description for the todo

## Input Validation

### ID Validation
- **Rule**: Must match existing todo item ID in memory
- **Format**: Valid UUID string format
- **Error**: "Todo item with ID [ID] not found" if ID doesn't exist

### Title Validation
- **Rule**: Must not be empty or contain only whitespace
- **Format**: Any non-empty string after whitespace trimming
- **Error**: "Title cannot be empty or contain only whitespace" if validation fails

### Description Validation
- **Rule**: No validation required (can be empty)
- **Format**: Any string including empty string
- **Error**: None

## Success Response

### Output Format
```
Todo updated successfully!
ID: [UUID]
Title: [Updated Title]
Description: [Updated Description or "None" if empty]
Status: [Current Status]
```

### Success Conditions
- Todo item exists with given ID
- New title passes validation
- Update operation completes without error
- Changes are reflected in memory

## Error Responses

### Invalid ID Error
```
Error: Todo item with ID [ID] not found
```

### Invalid Title Error
```
Error: Title cannot be empty or contain only whitespace
```

### General Error
```
Error: [Specific error message]
```

## Behavior Specifications

### Atomicity
- Update operation is atomic: either fully succeeds or fails without partial changes
- If validation fails, original todo remains unchanged

### Consistency
- After successful update, all properties except title/description remain unchanged
- ID and status are preserved during update
- Updated todo is immediately available for other operations

### Concurrency
- Single-threaded operation (no concurrent access concerns)
- Updates happen in same memory space as other operations

## Integration Points

### With TodoList
- Calls TodoList.update_item() method
- Validates against TodoList.get_item() for ID existence
- Results visible through TodoList.get_all_items()

### With TodoView
- Updated todos immediately visible in list command
- No additional synchronization required

## Edge Cases

### Empty Description
- When description parameter is omitted, description remains unchanged
- When description parameter is empty string, description is set to empty string

### Whitespace Handling
- Title validation trims whitespace and checks for non-empty result
- Description preserves all whitespace characters

### Long Text
- No explicit length limits (constrained by Python string limits)
- Should handle reasonable length text without performance issues