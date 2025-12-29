# Data Model: Delete Todo Feature

**Feature**: 005-delete-todo
**Created**: 2025-12-29
**Model**: TodoItem/TodoList

## Entities

### TodoItem
**Purpose**: Represents a single todo item that can be deleted

**Attributes**:
- `id: str` - Unique identifier (UUID string, immutable)
- `title: str` - Title of the todo
- `description: str` - Description of the todo
- `status: TodoStatus` - Status of the todo

**Validation Rules**:
- `id`: Must be valid UUID string format (set at creation, immutable)
- No validation needed for deletion operation

**State Transitions**:
- No state transitions during deletion operation
- Item is removed from collection entirely

### TodoList
**Purpose**: In-memory collection that manages TodoItem instances

**Methods**:
- `get_item(id: str) -> TodoItem` - Retrieve existing item by ID
- `get_all_items() -> List[TodoItem]` - Get all items (for list view)
- `delete_item(id: str) -> bool` - Delete specific item by ID

**Validation Rules**:
- `delete_item`: Must validate that item with given ID exists before deletion
- `delete_item`: Should return success indicator after deletion

## Relationships

- TodoList contains multiple TodoItem instances
- Each TodoItem belongs to exactly one TodoList (in memory)
- Deletion removes TodoItem from TodoList collection

## Constraints

- **Deletion**: TodoItem is completely removed from memory upon deletion
- **Validation**: ID must exist in collection before deletion
- **Consistency**: After deletion, item should no longer be accessible via get_item
- **Integrity**: All other existing functionality must continue to work after deletion