"""
Todo CLI Application - Add Todo Functionality

This module contains the functions for adding todo items to the in-memory storage.
"""
from .model import TodoList, TodoItem


def add_todo(todo_list: TodoList, title: str, description: str = "") -> TodoItem:
    """
    Implement add_todo function to create and store todo items.

    Args:
        todo_list: The TodoList instance to add the item to
        title: The title of the todo item (required)
        description: The description of the todo item (optional)

    Returns:
        TodoItem: The newly created todo item

    Raises:
        ValueError: If the title is empty or contains only whitespace
    """
    # Validate title (T012: Implement title validation to reject empty/whitespace-only titles)
    if not title or not title.strip():
        raise ValueError("Title cannot be empty or contain only whitespace")

    # Add the todo item to the list and return it
    return todo_list.add_item(title, description)