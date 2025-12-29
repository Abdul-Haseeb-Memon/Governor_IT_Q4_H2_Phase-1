"""
Todo CLI Application - Mark Todo Status Functionality

This module contains the functions for updating todo item status in-memory storage.
"""
from .model import TodoList, TodoItem, TodoStatus


def mark_todo_complete(todo_list: TodoList, item_id: str) -> bool:
    """
    Mark a todo item as complete.

    Args:
        todo_list: The TodoList instance containing the item to update
        item_id: The ID of the todo item to mark as complete

    Returns:
        bool: True if the status update was successful, False otherwise
    """
    try:
        # Update the item status to complete
        updated_item = todo_list.update_item_status(item_id, TodoStatus.COMPLETE)

        # Display success message
        print("Todo status updated successfully!")
        print(f"ID: {updated_item.id}")
        print(f"Title: {updated_item.title}")
        print(f"Description: {updated_item.description or 'None'}")
        print(f"Status: {updated_item.status.value}")

        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False


def mark_todo_incomplete(todo_list: TodoList, item_id: str) -> bool:
    """
    Mark a todo item as incomplete.

    Args:
        todo_list: The TodoList instance containing the item to update
        item_id: The ID of the todo item to mark as incomplete

    Returns:
        bool: True if the status update was successful, False otherwise
    """
    try:
        # Update the item status to incomplete
        updated_item = todo_list.update_item_status(item_id, TodoStatus.INCOMPLETE)

        # Display success message
        print("Todo status updated successfully!")
        print(f"ID: {updated_item.id}")
        print(f"Title: {updated_item.title}")
        print(f"Description: {updated_item.description or 'None'}")
        print(f"Status: {updated_item.status.value}")

        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False