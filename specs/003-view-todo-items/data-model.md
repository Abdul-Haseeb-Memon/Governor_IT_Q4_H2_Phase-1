# Data Model: View Todo Items

## Entities

### TodoItem (Reference)

**Description**: Represents a single todo item that already exists in the system from previous specifications

**Fields**:
- `id` (string): Unique identifier generated using UUID (required)
- `title` (string): Title of the todo item (required, validated non-empty)
- `description` (string): Optional description of the todo item (optional, can be empty)
- `status` (string): Status of the todo item, defaults to "incomplete" (required)

### TodoList (Reference)

**Description**: In-memory collection of TodoItem objects for the current session (already exists)

**Fields**:
- `items` (list): Collection of TodoItem objects, maintained in memory during session

**Operations**:
- Add: Add a new TodoItem to the collection
- List: Retrieve all TodoItems in the collection (used by this feature)
- Find: Retrieve a specific TodoItem by ID

## Relationships

- TodoList contains zero or more TodoItem objects
- Each TodoItem belongs to exactly one TodoList (in memory)
- TodoItem IDs are unique within the TodoList

## Constraints for View Feature

- All data is stored in memory only (no persistence)
- Data is lost when the application exits
- View operation must display all fields (ID, title, description, status) as specified
- Empty list must be handled gracefully with appropriate message
- Output must be formatted for console display