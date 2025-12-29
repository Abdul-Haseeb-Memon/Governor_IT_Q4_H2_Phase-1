---
description: "Task list template for feature implementation"
---

# Tasks: CLI UX/UI & Execution Mode Upgrade

**Input**: Design documents from `/specs/007-interactive-cli/`
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

- [X] T001 Update main.py to interactive menu-driven interface in src/todo/main.py
- [X] T002 Create __main__.py for module execution support in src/todo/__main__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T003 [P] Implement main menu loop structure in src/todo/main.py
- [X] T004 [P] Implement input validation and error handling in src/todo/main.py
- [X] T005 [P] Create TodoList instance management for interactive session in src/todo/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Interactive Menu Experience (Priority: P1) 🎯 MVP

**Goal**: Provide a menu-driven interface when the application runs without arguments, displaying options for all todo operations and continuing to run until user explicitly exits.

**Independent Test**: Can be fully tested by running the application directly and verifying that a menu appears with options to perform all todo operations.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Test application runs with menu interface in tests/unit/test_interactive.py
- [ ] T007 [P] [US1] Test menu displays all required options in tests/unit/test_interactive.py

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement menu display with all required options in src/todo/main.py
- [X] T009 [P] [US1] Implement numeric input handling for menu selection in src/todo/main.py
- [X] T010 [US1] Update __main__.py to launch interactive interface
- [X] T011 [US1] Implement application loop that continues until user exits in src/todo/main.py
- [X] T012 [US1] Test basic menu functionality and loop behavior

**Checkpoint**: At this point, interactive menu functionality should be fully functional and testable independently

---

## Phase 4: User Story 2 - Menu Navigation and Task Operations (Priority: P1)

**Goal**: Allow users to navigate through the menu system to perform all todo operations (add, view, update, delete, mark complete/incomplete) with the same functionality as previous specs but through the new interface.

**Independent Test**: Can be tested by navigating through the menu and performing each operation to verify that all existing functionality works through the new interface.

### Implementation for User Story 2

- [X] T013 [P] [US2] Implement option 1: Add a new task functionality in src/todo/main.py
- [X] T014 [P] [US2] Implement option 2: View all tasks functionality in src/todo/main.py
- [X] T015 [P] [US2] Implement option 3: Update an existing task functionality in src/todo/main.py
- [X] T016 [P] [US2] Implement option 4: Delete a task functionality in src/todo/main.py
- [X] T017 [P] [US2] Implement option 5: Mark task as complete functionality in src/todo/main.py
- [X] T018 [P] [US2] Implement option 6: Mark task as incomplete functionality in src/todo/main.py
- [X] T019 [US2] Implement option 7: Exit application functionality in src/todo/main.py
- [X] T020 [US2] Test all menu operations with valid inputs

**Checkpoint**: At this point, all menu operations should be fully functional

---

## Phase 5: User Story 3 - Input Validation and Error Handling (Priority: P2)

**Goal**: Provide clear error messages and input validation so that users understand what went wrong when they enter invalid data, without showing stack traces.

**Independent Test**: Can be tested by entering invalid data for each operation and verifying that appropriate error messages are displayed without stack traces.

### Implementation for User Story 3

- [X] T021 [P] [US3] Implement validation for invalid menu selections in src/todo/main.py
- [X] T022 [P] [US3] Implement validation for invalid task IDs in src/todo/main.py
- [X] T023 [P] [US3] Implement validation for empty/invalid titles in src/todo/main.py
- [X] T024 [P] [US3] Create user-friendly error messages without stack traces in src/todo/main.py
- [X] T025 [US3] Test error handling with invalid inputs
- [X] T026 [US3] Verify no stack traces are shown to users

**Checkpoint**: At this point, error handling for invalid inputs should be fully functional

---

## Phase 6: Compatibility & Integration

**Goal**: Ensure the new interactive interface is fully compatible with existing functionality and entry points

- [X] T027 [P] Ensure VS Code "Run" button works with new interface
- [X] T028 [P] Ensure `python -m src.todo` execution works properly
- [X] T029 [P] Test compatibility with all existing business logic modules
- [X] T030 Test complete workflow through interactive interface

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T031 [P] Update documentation in docs/
- [X] T032 Code cleanup and refactoring
- [X] T033 [P] Additional unit tests (if requested) in tests/unit/
- [X] T034 Run quickstart.md validation
- [X] T035 Update CLI help text and remove deprecated CLI argument code
- [X] T036 [P] Implement beautiful ASCII art UI formatting with consistent borders in src/todo/main.py
- [X] T037 [P] Implement number-based task selection instead of UUID entry in src/todo/main.py
- [X] T038 [P] Add status shortcuts (c=complete, p=pending) during task updates in src/todo/main.py
- [X] T039 [P] Ensure no long UUIDs are visible to users in display functions in src/todo/view_todo.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Compatibility (Phase 6)**: Depends on all user stories being implemented
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
Task: "Implement menu display with all required options in src/todo/interactive_main.py"
Task: "Implement numeric input handling for menu selection in src/todo/interactive_main.py"
Task: "Implement application loop that continues until user exits in src/todo/interactive_main.py"
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