# Data Model: Add Todo Item

## Entities

### TodoItem

**Description**: Represents a single todo item with properties as defined in the feature specification

**Fields**:
- `id` (string): Unique identifier generated using UUID (required)
- `title` (string): Title of the todo item (required, validated non-empty)
- `description` (string): Optional description of the todo item (optional, can be empty)
- `status` (string): Status of the todo item, defaults to "incomplete" (required)

**Validation Rules**:
- `id`: Must be a valid UUID string, automatically generated
- `title`: Must not be empty or whitespace-only after trimming
- `description`: No specific validation (can be any string including empty)
- `status`: Must be one of ["incomplete", "complete"], defaults to "incomplete"

**State Transitions**:
- Default state: "incomplete" when created via add functionality
- Can transition to "complete" via other functionality (not in this feature)

### TodoList

**Description**: In-memory collection of TodoItem objects for the current session

**Fields**:
- `items` (list): Collection of TodoItem objects, maintained in memory during session

**Operations**:
- Add: Add a new TodoItem to the collection
- List: Retrieve all TodoItems in the collection
- Find: Retrieve a specific TodoItem by ID

## Relationships

- TodoList contains zero or more TodoItem objects
- Each TodoItem belongs to exactly one TodoList (in memory)
- TodoItem IDs are unique within the TodoList

## Constraints

- All data is stored in memory only (no persistence)
- Data is lost when the application exits
- Title validation: Must be non-empty and non-whitespace after trimming
- IDs are automatically generated and unique
- Status defaults to "incomplete" for new items