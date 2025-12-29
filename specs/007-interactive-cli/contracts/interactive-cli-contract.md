# UI Contract: Interactive CLI Application

**Feature**: 007-interactive-cli
**Contract**: Interactive Menu-Driven Todo Application
**Created**: 2025-12-29

## Entry Points

### Direct Execution
```
python -m src.todo
```

### VS Code Run
- Execute via VS Code "Run Python File" button
- No command line arguments required

## User Interface Flow

### Initial Display
```
Todo List Application
=====================

Please select an option:
1. Add a new task
2. View all tasks
3. Update an existing task
4. Delete a task
5. Mark task as complete
6. Mark task as incomplete
7. Exit application

Enter your choice (1-7):
```

## Menu Operations

### Option 1: Add a new task
**Flow**:
1. Prompt: "Enter task title: "
2. Prompt: "Enter task description (optional): "
3. Execute add operation
4. Display success/error message
5. Return to main menu

### Option 2: View all tasks
**Flow**:
1. Execute view operation
2. Display all tasks in standard format:
   ```
   [ID] Title - status
       Description: description text
   ```
3. If no tasks: "No tasks found."
4. Return to main menu

### Option 3: Update an existing task
**Flow**:
1. Prompt: "Enter task ID to update: "
2. Prompt: "Enter new title: "
3. Prompt: "Enter new description (optional): "
4. Execute update operation
5. Display success/error message
6. Return to main menu

### Option 4: Delete a task
**Flow**:
1. Prompt: "Enter task ID to delete: "
2. Execute delete operation
3. Display success/error message
4. Return to main menu

### Option 5: Mark task as complete
**Flow**:
1. Prompt: "Enter task ID to mark as complete: "
2. Execute complete operation
3. Display success/error message
4. Return to main menu

### Option 6: Mark task as incomplete
**Flow**:
1. Prompt: "Enter task ID to mark as incomplete: "
2. Execute incomplete operation
3. Display success/error message
4. Return to main menu

### Option 7: Exit application
**Flow**:
1. Terminate application gracefully

## Input Validation

### Menu Selection Validation
- **Rule**: Must be integer between 1-7
- **Error**: "Invalid choice. Please enter a number between 1 and 7."
- **Behavior**: Return to menu prompt after error

### Task ID Validation
- **Rule**: Must be valid UUID format and exist in list
- **Error**: "Task with ID [ID] not found."
- **Behavior**: Return to menu after error

### Task Title Validation
- **Rule**: Must not be empty or contain only whitespace
- **Error**: "Title cannot be empty or contain only whitespace."
- **Behavior**: Return to menu after error

## Success Responses

### Standard Success Format
```
Operation completed successfully!
[Additional details specific to operation]
```

## Error Responses

### Menu Input Error
```
Invalid choice. Please enter a number between 1 and 7.
```

### Task ID Error
```
Error: Task with ID [ID] not found.
```

### Title Error
```
Error: Title cannot be empty or contain only whitespace.
```

### General Error
```
Error: [Specific error message]
```

## Behavior Specifications

### Loop Continuation
- Application continues running until user selects option 7
- After each operation, returns to main menu
- No operation terminates the application except explicit exit

### Error Recovery
- Invalid input shows error message and returns to menu
- No crashes or stack traces shown to user
- User can continue using application after errors

### Session Persistence
- All tasks remain in memory during session
- Tasks persist across different menu operations
- Memory cleared only when application exits