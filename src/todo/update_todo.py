"""
Todo CLI Application - Update Todo Functionality

This module contains the functions for updating todo items in-memory storage.
"""
from .model import TodoList, TodoItem


def update_todo(todo_list: TodoList, item_id: str, new_title: str, new_description: str = None) -> bool:
    """
    Update a todo item's title and/or description.

    Args:
        todo_list: The TodoList instance containing the item to update
        item_id: The ID of the todo item to update
        new_title: The new title for the todo item
        new_description: The new description for the todo item (optional)

    Returns:
        bool: True if the update was successful, False otherwise
    """
    try:
        # Update the item in the todo list
        updated_item = todo_list.update_item(item_id, new_title, new_description)

        # Display success message
        print("Todo updated successfully!")
        print(f"ID: {updated_item.id}")
        print(f"Title: {updated_item.title}")
        print(f"Description: {updated_item.description or 'None'}")
        print(f"Status: {updated_item.status.value}")

        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False