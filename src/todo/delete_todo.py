"""
Todo CLI Application - Delete Todo Functionality

This module contains the functions for deleting todo items from in-memory storage.
"""
from .model import TodoList, TodoItem


def delete_todo(todo_list: TodoList, item_id: str) -> bool:
    """
    Delete a todo item by its ID.

    Args:
        todo_list: The TodoList instance containing the item to delete
        item_id: The ID of the todo item to delete

    Returns:
        bool: True if the deletion was successful, False otherwise
    """
    try:
        # Delete the item from the todo list
        deleted_item = todo_list.delete_item(item_id)

        # Display success message
        print("Todo deleted successfully!")
        print(f"ID: {deleted_item.id}")
        print(f"Title: {deleted_item.title}")
        print(f"Description: {deleted_item.description or 'None'}")
        print(f"Status: {deleted_item.status.value}")

        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False