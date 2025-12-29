# Data Model: Mark Todo Complete/Incomplete Feature

**Feature**: 006-mark-todo
**Created**: 2025-12-29
**Model**: TodoItem/TodoList

## Entities

### TodoItem
**Purpose**: Represents a single todo item that can have its status updated

**Attributes**:
- `id: str` - Unique identifier (UUID string, immutable)
- `title: str` - Title of the todo
- `description: str` - Description of the todo
- `status: TodoStatus` - Status of the todo (mutable via status update)

**Validation Rules**:
- `id`: Must be valid UUID string format (set at creation, immutable)
- No validation needed for status updates beyond enum values

**State Transitions**:
- `status`: Can transition from INCOMPLETE to COMPLETE (complete operation)
- `status`: Can transition from COMPLETE to INCOMPLETE (incomplete operation)
- Other properties remain constant during status update

### TodoList
**Purpose**: In-memory collection that manages TodoItem instances

**Methods**:
- `get_item(id: str) -> TodoItem` - Retrieve existing item by ID
- `get_all_items() -> List[TodoItem]` - Get all items (for list view)
- `update_item_status(id: str, new_status: TodoStatus) -> TodoItem` - Update status of specific item

**Validation Rules**:
- `update_item_status`: Must validate that item with given ID exists before updating
- `update_item_status`: Should return success indicator after status update

## Relationships

- TodoList contains multiple TodoItem instances
- Each TodoItem belongs to exactly one TodoList (in memory)
- Status updates modify TodoItem status property in place

## Constraints

- **Status Updates**: TodoItem status can be changed between INCOMPLETE and COMPLETE
- **Validation**: ID must exist in collection before status update
- **Consistency**: After status update, item should reflect new status in subsequent operations
- **Integrity**: All other properties of the item remain unchanged during status update