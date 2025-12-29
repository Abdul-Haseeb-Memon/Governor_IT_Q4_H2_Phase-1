"""
Todo CLI Application - Interactive Menu Interface

This module provides an interactive menu-driven interface for the Todo CLI application.
"""
import sys
import os

# Add the project root directory to the Python path for direct execution
if __name__ == "__main__":
    # Get the project root directory (two levels up from this file)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

# Handle both direct execution and module execution
try:
    # When running as module (python -m src.todo)
    from .model import TodoList
    from .add_todo import add_todo
    from .view_todo import view_todos
    from .update_todo import update_todo
    from .delete_todo import delete_todo
    from .mark_todo import mark_todo_complete, mark_todo_incomplete
except ImportError:
    # When running directly (python src/todo/main.py)
    from todo.model import TodoList
    from todo.add_todo import add_todo
    from todo.view_todo import view_todos
    from todo.update_todo import update_todo
    from todo.delete_todo import delete_todo
    from todo.mark_todo import mark_todo_complete, mark_todo_incomplete


def get_user_input(prompt: str) -> str:
    """Get input from user with proper handling."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nApplication terminated by user.")
        sys.exit(0)


def get_numeric_input(prompt: str, min_val: int, max_val: int) -> int:
    """Get numeric input from user with validation."""
    while True:
        user_input = get_user_input(prompt)
        try:
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid choice. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")


def get_task_id() -> str:
    """Get task ID from user with validation."""
    return get_user_input("Enter task ID: ").strip()


def display_header():
    """Display the application header."""
    print()
    print("**************************************************")
    print("*              TODO LIST APPLICATION             *")
    print("**************************************************")
    print()


def display_menu():
    """Display the main menu options."""
    print("**************************************************")
    print("*                    MAIN MENU                   *")
    print("**************************************************")
    print("*  [+] 1. Add a new task                         *")
    print("*  [V] 2. View all tasks                         *")
    print("*  [E] 3. Update an existing task                *")
    print("*  [D] 4. Delete a task                          *")
    print("*  [C] 5. Mark task as complete                  *")
    print("*  [I] 6. Mark task as incomplete                *")
    print("*  [X] 7. Exit application                       *")
    print("**************************************************")


def display_tasks_with_selection(todo_list: TodoList, action: str) -> str:
    """
    Display tasks with numbered options and return the selected task ID.

    Args:
        todo_list: The TodoList instance to view
        action: The action being performed (for display purposes)

    Returns:
        str: The selected task ID, or None if user wants to go back
    """
    todos = todo_list.get_all_items()

    if not todos:
        print("[!] No tasks found.")
        return None

    print(f"\nSelect a task to {action}:")
    print("==================================================")

    for i, todo in enumerate(todos, 1):
        status_symbol = "C" if todo.status.value == "complete" else "P"
        print(f"  {i:2d}. [{status_symbol}] {todo.title}")
        if todo.description:
            print(f"      |- {todo.description}")
        print("      ----------------------------------------------")

    print("==================================================")
    print("  0. <- Back to main menu")
    print("==================================================")

    while True:
        choice = get_numeric_input(f"Enter task number (0-{len(todos)}): ", 0, len(todos))
        if choice == 0:
            return None  # User wants to go back
        else:
            return todos[choice - 1].id


def main():
    """Main entry point for the interactive Todo CLI application."""
    display_header()

    # Create a shared todo list instance for this session
    todo_list = TodoList()

    while True:
        display_menu()
        print()

        choice = get_numeric_input("Enter your choice (1-7): ", 1, 7)
        print()

        if choice == 1:
            # Add a new task
            print("**************************************************")
            print("*                    ADD TASK                    *")
            print("**************************************************")

            title = get_user_input("Enter task title: ")
            if not title.strip():
                print("[!] Task title cannot be empty.")
                continue

            description = get_user_input("Enter task description (optional): ")

            try:
                todo_item = add_todo(todo_list, title, description)
                print("\n[✓] Task added successfully!")
                print(f"*  ID: {todo_item.id}")
                print(f"*  Title: {todo_item.title}")
                print(f"*  Description: {todo_item.description or 'None'}")
                print(f"*  Status: {todo_item.status.value}")
            except ValueError as e:
                print(f"[✗] Error: {e}")

        elif choice == 2:
            # View all tasks
            print("==================================================")
            print("                    ALL TASKS                     ")
            print("==================================================")

            # Call the imported view_todos function
            view_todos(todo_list)

        elif choice == 3:
            # Update an existing task
            task_id = display_tasks_with_selection(todo_list, "update")
            if task_id is None:
                print("Returning to main menu...")
                continue

            print(f"\nSelected task ID: {task_id}")
            new_title = get_user_input("Enter new title: ")
            new_description = get_user_input("Enter new description (optional): ")

            # Get current task to check status
            current_task = None
            for task in todo_list.get_all_items():
                if task.id == task_id:
                    current_task = task
                    break

            if current_task:
                print(f"Current status: {current_task.status.value}")
                change_status = get_user_input("Do you want to change the status? (y/N): ")
                if change_status.lower() in ['y', 'yes']:
                    new_status = get_user_input("Enter new status (c=complete, p=pending): ").lower().strip()
                    if new_status in ['c', 'complete', 'completed', 'yes']:
                        # Update title and description first
                        success = update_todo(todo_list, task_id, new_title, new_description)
                        if success:
                            # Then mark as complete
                            mark_success = mark_todo_complete(todo_list, task_id)
                            if mark_success:
                                print("[✓] Task updated and marked as complete!")
                            else:
                                print("[✓] Task updated but failed to mark as complete.")
                        else:
                            print("[✗] Failed to update task.")
                    elif new_status in ['p', 'incomplete', 'pending', 'no']:
                        # Update title and description first
                        success = update_todo(todo_list, task_id, new_title, new_description)
                        if success:
                            # Then mark as incomplete
                            mark_success = mark_todo_incomplete(todo_list, task_id)
                            if mark_success:
                                print("[✓] Task updated and marked as incomplete!")
                            else:
                                print("[✓] Task updated but failed to mark as incomplete.")
                        else:
                            print("[✗] Failed to update task.")
                    else:
                        print("[!] Invalid status. Updating task without changing status.")
                        success = update_todo(todo_list, task_id, new_title, new_description)
                        if success:
                            print("[✓] Task updated successfully!")
                        else:
                            print("[✗] Failed to update task.")
                else:
                    # Update without changing status
                    success = update_todo(todo_list, task_id, new_title, new_description)
                    if success:
                        print("[✓] Task updated successfully!")
                    else:
                        print("[✗] Failed to update task.")
            else:
                # Fallback if task not found
                success = update_todo(todo_list, task_id, new_title, new_description)
                if success:
                    print("[✓] Task updated successfully!")
                else:
                    print("[✗] Failed to update task.")

        elif choice == 4:
            # Delete a task
            task_id = display_tasks_with_selection(todo_list, "delete")
            if task_id is None:
                print("Returning to main menu...")
                continue

            print(f"\nSelected task ID: {task_id}")

            confirm = get_user_input("Are you sure you want to delete this task? (y/N): ")
            if confirm.lower() in ['y', 'yes']:
                try:
                    success = delete_todo(todo_list, task_id)
                    if success:
                        print("[✓] Task deleted successfully!")
                    else:
                        print("[✗] Failed to delete task.")
                except ValueError as e:
                    print(f"[✗] Error: {e}")
            else:
                print("Task deletion cancelled.")

        elif choice == 5:
            # Mark task as complete
            task_id = display_tasks_with_selection(todo_list, "mark complete")
            if task_id is None:
                print("Returning to main menu...")
                continue

            print(f"\nSelected task ID: {task_id}")

            try:
                success = mark_todo_complete(todo_list, task_id)
                if success:
                    print("[✓] Task marked as complete!")
                else:
                    print("[✗] Failed to mark task as complete.")
            except ValueError as e:
                print(f"[✗] Error: {e}")

        elif choice == 6:
            # Mark task as incomplete
            task_id = display_tasks_with_selection(todo_list, "mark incomplete")
            if task_id is None:
                print("Returning to main menu...")
                continue

            print(f"\nSelected task ID: {task_id}")

            try:
                success = mark_todo_incomplete(todo_list, task_id)
                if success:
                    print("[✓] Task marked as incomplete!")
                else:
                    print("[✗] Failed to mark task as incomplete.")
            except ValueError as e:
                print(f"[✗] Error: {e}")

        elif choice == 7:
            # Exit application
            print("**************************************************")
            print("*            THANK YOU FOR USING                 *")
            print("*              TODO LIST APP                     *")
            print("**************************************************")
            print()
            break

        print()  # Add blank line for readability
        get_user_input("Press Enter to continue...")  # Pause before showing menu again
        print()  # Add blank line for readability


if __name__ == "__main__":
    main()