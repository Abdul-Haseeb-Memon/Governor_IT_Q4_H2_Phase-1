"""
Todo CLI Application - Data Models

This module contains the data models for the Todo CLI application.
"""
from dataclasses import dataclass
from typing import List
import uuid
from enum import Enum


class TodoStatus(Enum):
    """Enumeration of possible todo statuses."""
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


@dataclass
class TodoItem:
    """Represents a single todo item with properties as defined in the feature specification."""

    id: str
    title: str
    description: str = ""
    status: TodoStatus = TodoStatus.INCOMPLETE

    def __post_init__(self):
        """Validate the TodoItem after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        # Ensure the title is stripped of leading/trailing whitespace
        self.title = self.title.strip()


class TodoList:
    """In-memory collection of TodoItem objects for the current session."""

    def __init__(self):
        """Initialize an empty todo list."""
        self.items: List[TodoItem] = []

    def add_item(self, title: str, description: str = "") -> TodoItem:
        """Add a new TodoItem to the collection."""
        # Generate a unique ID using UUID
        item_id = str(uuid.uuid4())

        # Create the TodoItem with the generated ID
        todo_item = TodoItem(
            id=item_id,
            title=title,
            description=description,
            status=TodoStatus.INCOMPLETE
        )

        # Add the item to the collection
        self.items.append(todo_item)

        return todo_item

    def get_item(self, item_id: str) -> TodoItem:
        """Retrieve a specific TodoItem by ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        raise ValueError(f"Todo item with ID {item_id} not found")

    def get_all_items(self) -> List[TodoItem]:
        """Retrieve all TodoItems in the collection."""
        return self.items[:]

    def update_item(self, id: str, new_title: str = None, new_description: str = None) -> TodoItem:
        """Update an existing todo item's title and/or description."""
        for item in self.items:
            if item.id == id:
                # Update title if provided
                if new_title is not None:
                    if not new_title or not new_title.strip():
                        raise ValueError("Title cannot be empty or contain only whitespace")
                    item.title = new_title.strip()

                # Update description if provided
                if new_description is not None:
                    item.description = new_description

                return item

        raise ValueError(f"Todo item with ID {id} not found")

    def delete_item(self, id: str) -> TodoItem:
        """Delete an existing todo item by ID."""
        for i, item in enumerate(self.items):
            if item.id == id:
                deleted_item = self.items.pop(i)
                return deleted_item

        raise ValueError(f"Todo item with ID {id} not found")

    def update_item_status(self, id: str, new_status: TodoStatus) -> TodoItem:
        """Update the status of an existing todo item by ID."""
        for item in self.items:
            if item.id == id:
                item.status = new_status
                return item

        raise ValueError(f"Todo item with ID {id} not found")

    def clear(self):
        """Clear all items from the list (for testing purposes)."""
        self.items.clear()