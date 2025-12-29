---
description: "Task list template for feature implementation"
---

# Tasks: View Todo Items

**Input**: Design documents from `/specs/003-view-todo-items/`
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

- [X] T001 Create view_todo.py module for view functionality
- [X] T002 Update main.py to support list command for viewing todos

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T003 Access existing TodoList in-memory storage mechanism
- [X] T004 [P] Implement console output formatting function
- [X] T005 [P] Create empty list handling mechanism

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Todo Items (Priority: P1) 🎯 MVP

**Goal**: Display all Todo items currently stored **in memory** via console.

**Independent Test**: Can be fully tested by running the CLI command to view todos and verifying the output format.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Test view functionality with todos present in tests/unit/test_view.py
- [ ] T007 [P] [US1] Test empty list handling in tests/unit/test_view.py

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement view_todos function to access and format todo list in src/todo/view_todo.py
- [X] T009 [P] [US1] Implement console output formatting with ID, title, description, status in src/todo/view_todo.py
- [X] T010 [US1] Update main.py to handle list command and call view_todos function
- [X] T011 [US1] Implement empty list handling to display "No tasks found." message in src/todo/view_todo.py
- [X] T012 [US1] Add view functionality to CLI in src/todo/main.py with proper output format

**Checkpoint**: At this point, view todo functionality should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T013 [P] Update documentation in docs/
- [X] T014 Code cleanup and refactoring
- [X] T015 [P] Additional unit tests (if requested) in tests/unit/
- [X] T016 Run quickstart.md validation
- [X] T017 Update CLI help text to include list command

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
Task: "Implement view_todos function to access and format todo list in src/todo/view_todo.py"
Task: "Implement console output formatting with ID, title, description, status in src/todo/view_todo.py"
Task: "Implement empty list handling to display "No tasks found." message in src/todo/view_todo.py"
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