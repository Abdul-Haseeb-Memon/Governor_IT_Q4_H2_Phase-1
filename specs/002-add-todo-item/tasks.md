---
description: "Task list template for feature implementation"
---

# Tasks: Add Todo Item

**Input**: Design documents from `/specs/002-add-todo-item/`
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

- [X] T001 Create TodoItem data model in src/todo/model.py
- [X] T002 Update main.py to support add command with argparse
- [X] T003 [P] Create add_todo.py module for add functionality

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create TodoList in-memory storage mechanism
- [X] T005 [P] Implement UUID generation for unique todo IDs
- [X] T006 [P] Create input validation functions for title validation

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Allow the user to **add a new Todo item** with title and description, and store it in memory with a unique ID and default incomplete status.

**Independent Test**: Can be fully tested by running the CLI command to add a todo and verifying it appears in the list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T007 [P] [US1] Test TodoItem creation with required fields in tests/unit/test_model.py
- [ ] T008 [P] [US1] Test add command functionality in tests/unit/test_add_command.py

### Implementation for User Story 1

- [X] T009 [P] [US1] Implement TodoItem data model with id, title, description, status in src/todo/model.py
- [X] T010 [P] [US1] Implement TodoList in-memory storage in src/todo/model.py
- [X] T011 [US1] Implement add_todo function to create and store todo items in src/todo/add_todo.py
- [X] T012 [US1] Implement title validation to reject empty/whitespace-only titles in src/todo/add_todo.py
- [X] T013 [US1] Update main.py to handle add command and call add_todo function
- [X] T014 [US1] Add success/error message output to CLI in src/todo/main.py

**Checkpoint**: At this point, add todo functionality should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T015 [P] Update documentation in docs/
- [X] T016 Code cleanup and refactoring
- [X] T017 [P] Additional unit tests (if requested) in tests/unit/
- [X] T018 Run quickstart.md validation
- [X] T019 Update CLI help text to include add command

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Setup components before verification
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- All user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all setup tasks for User Story 1 together:
Task: "Implement TodoItem data model with id, title, description, status in src/todo/model.py"
Task: "Implement TodoList in-memory storage in src/todo/model.py"
Task: "Implement add_todo function to create and store todo items in src/todo/add_todo.py"
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

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
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