---
description: "Task list template for feature implementation"
---

# Tasks: Mark Todo Complete/Incomplete

**Input**: Design documents from `/specs/006-mark-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create mark_todo.py module for status update functionality in src/todo/mark_todo.py
- [X] T002 Update main.py to support complete/incomplete commands for updating status in src/todo/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T003 [P] Extend TodoList class with update_status method in src/todo/model.py
- [X] T004 [P] Implement validation for status update operations in src/todo/model.py
- [X] T005 [P] Create status update-specific error handling mechanism in src/todo/model.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Mark Todo as Complete (Priority: P1) 🎯 MVP

**Goal**: Allow users to mark a todo as complete using its ID via console command, with the status being updated in memory and visible in subsequent list views.

**Independent Test**: Can be fully tested by running the CLI command to mark a todo as complete and verifying that the status changes from "incomplete" to "complete" when viewing the todo list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Test mark complete functionality with valid inputs in tests/unit/test_mark.py
- [ ] T007 [P] [US1] Test mark complete functionality with invalid ID in tests/unit/test_mark.py

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement mark_todo_complete function to update status to complete in src/todo/mark_todo.py
- [X] T009 [P] [US1] Implement input validation for ID in src/todo/mark_todo.py
- [X] T010 [US1] Update main.py to handle complete command and call mark_todo_complete function
- [X] T011 [US1] Implement success message display after status update in src/todo/mark_todo.py
- [X] T012 [US1] Add complete functionality to CLI in src/todo/main.py with proper argument parsing
- [X] T013 [US1] Test end-to-end mark complete functionality with valid inputs

**Checkpoint**: At this point, mark complete functionality should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Todo as Incomplete (Priority: P2)

**Goal**: Allow users to mark a completed todo as incomplete using its ID via console command.

**Independent Test**: Can be tested by running the CLI command to mark a completed todo as incomplete and verifying that the status changes from "complete" to "incomplete" when viewing the todo list.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US2] Test mark incomplete functionality with valid inputs in tests/unit/test_mark.py
- [ ] T015 [P] [US2] Test mark incomplete functionality with invalid ID in tests/unit/test_mark.py

### Implementation for User Story 2

- [X] T016 [P] [US2] Implement mark_todo_incomplete function to update status to incomplete in src/todo/mark_todo.py
- [X] T017 [P] [US2] Implement input validation for ID in src/todo/mark_todo.py
- [X] T018 [US2] Update main.py to handle incomplete command and call mark_todo_incomplete function
- [X] T019 [US2] Add incomplete functionality to CLI in src/todo/main.py with proper argument parsing
- [X] T020 [US2] Test end-to-end mark incomplete functionality with valid inputs

**Checkpoint**: At this point, mark incomplete functionality should be fully functional

---

## Phase 5: User Story 3 - Handle Invalid Todo ID (Priority: P3)

**Goal**: Provide clear error messaging when users attempt to mark status for non-existent todos.

**Independent Test**: Can be tested by attempting to mark status of a todo with an invalid/non-existent ID and verifying that an appropriate error message is displayed.

### Implementation for User Story 3

- [X] T021 [P] [US3] Implement error handling for invalid IDs in src/todo/mark_todo.py
- [X] T022 [P] [US3] Create appropriate error messages for invalid IDs in src/todo/mark_todo.py
- [X] T023 [US3] Test error handling with invalid IDs
- [X] T024 [US3] Verify error message clarity and accuracy

**Checkpoint**: At this point, error handling for invalid IDs should be fully functional

---

## Phase 6: Error Handling & Edge Cases

**Goal**: Handle all error conditions and edge cases properly

- [X] T025 [P] Implement validation for non-existent IDs in src/todo/mark_todo.py
- [X] T026 [P] Implement error message for invalid todo IDs in src/todo/mark_todo.py
- [X] T027 [P] Test error cases (invalid ID) in tests/unit/test_mark.py
- [X] T028 Test status update functionality with malformed IDs

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T029 [P] Update documentation in docs/
- [X] T030 Code cleanup and refactoring
- [X] T031 [P] Additional unit tests (if requested) in tests/unit/
- [X] T032 Run quickstart.md validation
- [X] T033 Update CLI help text to include status update commands

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Error Handling (Phase 6)**: Depends on all user stories being implemented
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Depends on User Story 1 completion
- **User Story 3 (P3)**: Depends on User Story 1 completion

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Setup components before verification
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- All user stories can start in parallel (if team capacity allows) after foundational phase
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all setup tasks for User Story 1 together:
Task: "Implement mark_todo_complete function to update status to complete in src/todo/mark_todo.py"
Task: "Implement input validation for ID in src/todo/mark_todo.py"
Task: "Implement success message display after status update in src/todo/mark_todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence