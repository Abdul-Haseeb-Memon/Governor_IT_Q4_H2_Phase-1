# Data Model: Update Todo Feature

**Feature**: 004-update-todo
**Created**: 2025-12-29
**Model**: TodoItem/TodoList

## Entities

### TodoItem
**Purpose**: Represents a single todo item that can be updated

**Attributes**:
- `id: str` - Unique identifier (UUID string, immutable)
- `title: str` - Title of the todo (mutable via update)
- `description: str` - Description of the todo (mutable via update)
- `status: TodoStatus` - Status of the todo (immutable during update)

**Validation Rules**:
- `id`: Must be valid UUID string format (set at creation, immutable)
- `title`: Must not be empty or whitespace-only (validated on update)
- `description`: Optional, can be empty string (no validation required)
- `status`: Enum value (INCOMPLETE, COMPLETE) - unchanged during update

**State Transitions**:
- No state transitions during update operation
- ID remains constant
- Status remains constant
- Title and/or description change based on user input

### TodoList
**Purpose**: In-memory collection that manages TodoItem instances

**Methods**:
- `get_item(id: str) -> TodoItem` - Retrieve existing item by ID
- `update_item(id: str, new_title: str, new_description: str) -> TodoItem` - Update specific item
- `get_all_items() -> List[TodoItem]` - Get all items (for list view)

**Validation Rules**:
- `update_item`: Must validate that item with given ID exists
- `update_item`: Must validate that new title is not empty/whitespace
- `update_item`: Should preserve ID and status during update

## Relationships

- TodoList contains multiple TodoItem instances
- Each TodoItem belongs to exactly one TodoList (in memory)
- Updates to TodoItem are reflected immediately in TodoList queries

## Constraints

- **Immutability**: TodoItem ID and status are immutable during update operations
- **Validation**: Title must remain non-empty/meaningful after update
- **Consistency**: Updates must be immediately visible in subsequent operations
- **Integrity**: All existing functionality must continue to work after update