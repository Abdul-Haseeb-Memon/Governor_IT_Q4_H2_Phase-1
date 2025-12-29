---
description: "Task list template for feature implementation"
---

# Tasks: Update Todo

**Input**: Design documents from `/specs/004-update-todo/`
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

- [X] T001 Create update_todo.py module for update functionality in src/todo/update_todo.py
- [X] T002 Update main.py to support update command for modifying todos in src/todo/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T003 [P] Extend TodoList class with update_item method in src/todo/model.py
- [X] T004 [P] Implement validation for update operations in src/todo/model.py
- [X] T005 [P] Create update-specific error handling mechanism in src/todo/model.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Update Todo Title and Description (Priority: P1) 🎯 MVP

**Goal**: Allow users to update the title and/or description of an existing todo item via console command, with changes reflected immediately in subsequent list views.

**Independent Test**: Can be fully tested by running the CLI command to update a todo's title and/or description and verifying that the changes are reflected when viewing the todo list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Test update functionality with valid inputs in tests/unit/test_update.py
- [ ] T007 [P] [US1] Test update functionality with invalid ID in tests/unit/test_update.py

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement update_todo function to modify existing todo in src/todo/update_todo.py
- [X] T009 [P] [US1] Implement input validation for ID and title in src/todo/update_todo.py
- [X] T010 [US1] Update main.py to handle update command and call update_todo function
- [X] T011 [US1] Implement success message display after update in src/todo/update_todo.py
- [X] T012 [US1] Add update functionality to CLI in src/todo/main.py with proper argument parsing
- [X] T013 [US1] Test end-to-end update functionality with valid inputs

**Checkpoint**: At this point, update todo functionality should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update Todo Title Only (Priority: P2)

**Goal**: Allow users to update only the title of an existing todo item while preserving the description.

**Independent Test**: Can be fully tested by updating only the title of a todo and verifying that the description remains unchanged when viewing the todo list.

### Implementation for User Story 2

- [X] T014 [P] [US2] Implement title-only update functionality in src/todo/update_todo.py
- [X] T015 [P] [US2] Preserve description during title-only updates in src/todo/update_todo.py
- [X] T016 [US2] Test title-only update functionality with valid inputs
- [X] T017 [US2] Verify description preservation during title updates

**Checkpoint**: At this point, title-only update functionality should be fully functional

---

## Phase 5: User Story 3 - Update Todo Description Only (Priority: P3)

**Goal**: Allow users to update only the description of an existing todo item while preserving the title.

**Independent Test**: Can be fully tested by updating only the description of a todo and verifying that the title remains unchanged when viewing the todo list.

### Implementation for User Story 3

- [X] T018 [P] [US3] Implement description-only update functionality in src/todo/update_todo.py
- [X] T019 [P] [US3] Preserve title during description-only updates in src/todo/update_todo.py
- [X] T020 [US3] Test description-only update functionality with valid inputs
- [X] T021 [US3] Verify title preservation during description updates

**Checkpoint**: At this point, description-only update functionality should be fully functional

---

## Phase 6: Error Handling & Edge Cases

**Goal**: Handle all error conditions and edge cases properly

- [X] T022 [P] Implement validation for empty/whitespace-only titles in src/todo/update_todo.py
- [X] T023 [P] Implement error message for invalid todo IDs in src/todo/update_todo.py
- [X] T024 [P] Test error cases (invalid ID, empty title) in tests/unit/test_update.py
- [X] T025 Test update functionality with very long titles/descriptions

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T026 [P] Update documentation in docs/
- [X] T027 Code cleanup and refactoring
- [X] T028 [P] Additional unit tests (if requested) in tests/unit/
- [X] T029 Run quickstart.md validation
- [X] T030 Update CLI help text to include update command

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
Task: "Implement update_todo function to modify existing todo in src/todo/update_todo.py"
Task: "Implement input validation for ID and title in src/todo/update_todo.py"
Task: "Implement success message display after update in src/todo/update_todo.py"
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