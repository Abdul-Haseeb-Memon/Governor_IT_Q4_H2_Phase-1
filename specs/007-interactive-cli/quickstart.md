# Quickstart: Interactive CLI Application

**Feature**: 007-interactive-cli
**Created**: 2025-12-29

## Overview
The Interactive CLI Application transforms the command-line tool into a user-friendly menu-driven application that can be run directly without arguments. All existing functionality is preserved while improving usability.

## Prerequisites
- Python 3.14+ installed
- Project repository cloned and set up
- Current working directory: project root

## Execution Methods

### Method 1: Module Execution
```bash
python -m src.todo
```

### Method 2: VS Code Run
- Open `src/todo/__main__.py` in VS Code
- Click the "Run" button or press F5

## User Interface Flow

### Main Menu
When the application starts, you'll see:
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

### Operation Examples

1. **Add a new task**:
   - Select option 1
   - Enter a title when prompted
   - Enter a description (optional) when prompted
   - Task will be added and you'll return to the main menu

2. **View all tasks**:
   - Select option 2
   - All tasks will be displayed in the format: `[ID] Title - status`
   - You'll return to the main menu after viewing

3. **Update a task**:
   - Select option 3
   - Enter the task ID when prompted
   - Enter new title and description when prompted
   - Task will be updated and you'll return to the main menu

4. **Delete a task**:
   - Select option 4
   - Enter the task ID when prompted
   - Task will be deleted and you'll return to the main menu

5. **Mark task as complete/incomplete**:
   - Select option 5 or 6
   - Enter the task ID when prompted
   - Task status will be updated and you'll return to the main menu

6. **Exit application**:
   - Select option 7
   - Application will terminate gracefully

## Test Scenarios

### Scenario 1: Complete Workflow
1. Start the application: `python -m src.todo`
2. Add a task (option 1)
3. View tasks (option 2) - verify task appears
4. Update the task (option 3)
5. Mark task as complete (option 5)
6. View tasks again (option 2) - verify status updated
7. Exit (option 7)

### Scenario 2: Error Handling
1. Start the application
2. Enter an invalid menu option (e.g., 8)
3. Verify error message appears and menu is shown again
4. Enter an invalid task ID for any operation
5. Verify error message appears and you return to menu

## Expected Behavior

### Success Cases
- All menu options work correctly
- Tasks are added, updated, deleted, and status changed as expected
- Input validation works properly
- Application continues running until explicit exit

### Error Cases
- Invalid menu choices show error and return to menu
- Invalid task IDs show appropriate error messages
- Empty/invalid titles show appropriate error messages
- No stack traces are shown to the user

## Integration Testing
1. Run the application with `python -m src.todo`
2. Test all menu options
3. Verify all existing functionality works through the new interface
4. Test error conditions and validate user-friendly error messages