"""
Todo CLI Application - View Todo Functionality

This module contains the functions for viewing todo items from in-memory storage.
"""
from .model import TodoList, TodoItem


def view_todos(todo_list: TodoList) -> bool:
    """
    Implement view_todos function to access and format todo list.

    Args:
        todo_list: The TodoList instance to view the items from

    Returns:
        bool: True if there are todos to display, False if the list is empty
    """
    todos = todo_list.get_all_items()

    if not todos:
        print("[!] No tasks found.")
        return False

    # Display each todo with user-friendly format (without showing long IDs)
    for i, todo in enumerate(todos, 1):
        status_symbol = "C" if todo.status.value == "complete" else "P"
        print(f"  {i:2d}. [{status_symbol}] {todo.title}")
        if todo.description:
            print(f"      |- {todo.description}")
        print("      ----------------------------------------------")

    return True