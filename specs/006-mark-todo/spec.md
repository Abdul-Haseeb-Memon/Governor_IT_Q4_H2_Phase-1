# Feature Specification: Mark Todo Complete/Incomplete

**Feature Branch**: `006-mark-todo`
**Created**: 2025-12-29
**Status**: Draft
**Input**: User description: "# /sp.specify

## Phase I — Spec 6: Mark Todo Complete / Incomplete

---

## Objective
Allow users to **toggle the completion status** of a Todo in memory via console.

---

## Inputs
- Todo ID
- Desired status (complete or incomplete)

---

## Outputs
- Todo status updated in memory
- Confirmation message displayed

---

## Edge Cases
- Invalid or non-existent ID → display error message

---

## Constraints
- ❌ No manual coding
- ❌ No file/database persistence
- ❌ No AI
- ❌ No leftover test/debug code

---

## Tasks
1. Access in-memory Todo data structure
2. Implement "Mark Complete/Incomplete" console command
3. Validate Todo ID exists
4. Toggle status as requested
5. Confirm change in console output

---

## Files to Generate
- `/specs/phase-1/spec-6.md` → this spec
- `/src/todo/mark_todo.py` → Claude Code generated

---

## Definition of Done
- Users can toggle Todo completion in console
- Status changes immediately visible in list view
- Fully Claude Code–generated, clean and minimal
 and D:\PR0j3CTs\HACKATHON_02\T0D0_List_Phase_01\src\todo\main.py"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Mark Todo as Complete (Priority: P1)

As a user, I want to mark a todo as complete so that I can track which tasks I have finished.

**Why this priority**: This is core functionality for a todo management system. Users need to be able to indicate when they've completed tasks so they can track their progress and focus on remaining tasks.

**Independent Test**: Can be fully tested by running the CLI command to mark a todo as complete and verifying that the status changes from "incomplete" to "complete" when viewing the todo list.

**Acceptance Scenarios**:

1. **Given** a todo exists with ID "12345" and status "incomplete", **When** user runs `python -m src.todo.main complete 12345`, **Then** the todo's status changes to "complete" and this is visible in subsequent list views
2. **Given** a todo exists with ID "12345", **When** user runs `python -m src.todo.main complete 12345`, **Then** a confirmation message is displayed showing the status change

---

### User Story 2 - Mark Todo as Incomplete (Priority: P2)

As a user, I want to mark a completed todo as incomplete so that I can change my mind about a task's status.

**Why this priority**: This provides flexibility for users who may have accidentally marked a task as complete or need to revisit a completed task.

**Independent Test**: Can be tested by running the CLI command to mark a completed todo as incomplete and verifying that the status changes from "complete" to "incomplete" when viewing the todo list.

**Acceptance Scenarios**:

1. **Given** a todo exists with ID "12345" and status "complete", **When** user runs `python -m src.todo.main incomplete 12345`, **Then** the todo's status changes to "incomplete" and this is visible in subsequent list views

---

### User Story 3 - Handle Invalid Todo ID (Priority: P3)

As a user, I want to receive a clear error message when I try to mark a non-existent todo, so that I understand why the operation failed.

**Why this priority**: This provides good user experience by giving clear feedback when invalid input is provided, preventing confusion about why the operation didn't work.

**Independent Test**: Can be tested by attempting to mark a todo with an invalid/non-existent ID and verifying that an appropriate error message is displayed.

**Acceptance Scenarios**:

1. **Given** no todo exists with ID "invalid-id", **When** user runs `python -m src.todo.main complete invalid-id`, **Then** an error message "Todo item with ID invalid-id not found" is displayed

---

### Edge Cases

- What happens when the provided todo ID doesn't exist? → The system should display an error message "Todo item with ID [ID] not found"
- How does the system handle malformed UUIDs? → The system should treat malformed IDs as non-existent and show appropriate error
- What happens when the user provides an empty ID? → The system should validate and show appropriate error message

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to mark an existing todo as complete using its ID via console command
- **FR-002**: System MUST allow users to mark an existing todo as incomplete using its ID via console command
- **FR-003**: System MUST validate that the provided todo ID exists before attempting to change status
- **FR-004**: System MUST update the todo's status in memory upon successful status change
- **FR-005**: System MUST display a confirmation message when a todo's status is successfully changed
- **FR-006**: System MUST display an appropriate error message when an invalid todo ID is provided
- **FR-007**: System MUST ensure that status changes are immediately visible in list view
- **FR-008**: System MUST preserve all other properties of the todo during status change

### Key Entities *(include if feature involves data)*

- **Todo Item**: Represents a single task with ID, title, description, and status that can have its status changed
- **Todo List**: In-memory collection that maintains all todo items and supports status updates to individual items

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully mark a todo as complete in under 30 seconds
- **SC-002**: 100% of valid status change requests result in successfully updated todos that appear with correct status in list view
- **SC-003**: 100% of invalid status change requests (invalid ID) result in appropriate error messages
- **SC-004**: Status changes are immediately visible when viewing the todo list without requiring a restart