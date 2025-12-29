---
id: 1
title: "spec-todo-cli-app"
stage: "spec"
date: "2025-12-29"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli-app"
branch: "001-todo-cli-app"
user: "ahas3"
command: "/sp.specify"
labels: ["spec", "todo", "cli", "python"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "specs/001-todo-cli-app/spec.md"
  - "specs/001-todo-cli-app/checklists/requirements.md"
tests: []
---

# PHR: spec-todo-cli-app

## User Prompt

```
# /sp.specify

## Project
**The Evolution of Todo — Phase I: In-Memory Python Console Application**

---

## Focus & Theme
From a simple CLI script to a future cloud-native, AI-powered distributed system.

Phase I establishes the **foundational discipline** of spec-driven development, clean architecture, and agentic workflows using AI — without persistence, AI logic, or cloud deployment.

---

## Goal
Students act as **Product Architects**, using **Claude Code** and **Spec-Kit Plus** to design and generate a fully working **in-memory Todo CLI application**, without writing manual application code.

---

## Phase Scope (STRICT)

### Included
- Python console application
- In-memory task storage only
- CRUD-style Todo operations
- Spec → Plan → Tasks → Claude Code generation loop

### Explicitly Excluded
- ❌ File saving or loading
- ❌ Databases (JSON, SQLite, etc.)
- ❌ AI / chatbot features
- ❌ Web UI or APIs
- ❌ Cloud or containerization

---

## Success Criteria
After completing Phase I:
- The application runs from the terminal
- All 5 basic Todo operations work correctly
- All logic is generated from Specs
- Repository is clean, minimal, and reproducible
- Data is lost on program exit (in-memory only)

---

## Technology Stack
- Python 3.13+
- UV (Python environment & dependency manager)
- Claude Code
- Spec-Kit Plus
- WSL 2 (Ubuntu 22.04) for Windows users

---

## Repository Deliverables
- `sp.constitution.md`
- `/specs/phase-1/` (all specs preserved as history)
- `/src/` (Claude-generated Python source)
- `README.md` (setup & run instructions)
- `CLAUDE.md` (Claude Code usage rules)

---

# Phase I Specifications

## Spec 1 — Environment Setup & Development Plan

### Objective
Define the development plan, tooling, and environment requirements for Phase I.

### Must Define
- WSL 2 requirement for Windows users
- Ubuntu 22.04 setup
- Python 3.13+ installation
- UV usage for environment management
- Agentic Dev Stack workflow:
  - Write spec
  - Generate plan
  - Break into tasks
  - Implement via Claude Code
- Prohibition of manual application code

### Acceptance Criteria
- Developer can set up environment from README
- Claude Code operates inside WSL 2
- No platform-specific hacks required

---

## Spec 2 — Add Todo Item

### Objective
Allow users to add a new Todo item via the console.

### Inputs
- Title (required)
- Description (optional)

### Outputs
- New Todo item stored in memory
- Unique ID assigned
- Default status: incomplete

### Edge Cases
- Empty title → reject with message
- Whitespace-only input → reject

### Acceptance Criteria
- Todo appears when listing tasks
- No persistence after program exit

---

## Spec 3 — View Todo Items

### Objective
Display all Todo items in the console.

### Outputs
- List of Todos showing:
  - ID
  - Title
  - Completion status (complete / incomplete)

### Edge Cases
- No Todos → show friendly message

### Acceptance Criteria
- Output is readable and deterministic
- Reflects current in-memory state only

---

## Spec 4 — Update Todo Item

### Objective
Modify an existing Todo's title and/or description.

### Inputs
- Todo ID
- New title and/or description

### Edge Cases
- Invalid ID → error message
- Empty updated title → reject

### Acceptance Criteria
- Changes reflected immediately in memory
- No new Todo created accidentally

---

## Spec 5 — Delete Todo Item

### Objective
Remove a Todo item by ID.

### Inputs
- Todo ID

### Edge Cases
- Invalid or non-existent ID

### Acceptance Criteria
- Todo is removed from memory
- Cannot be viewed or updated afterward

---

## Spec 6 — Mark Todo Complete / Incomplete

### Objective
Toggle completion status of a Todo item.

### Inputs
- Todo ID
- Desired state (complete or incomplete)

### Edge Cases
- Invalid ID

### Acceptance Criteria
- Status change reflected in list view
- No impact on other Todos

---

## Constraints
- ❌ No manual Python code
- ❌ No persistence of any kind
- ❌ No skipped Specs
- ❌ No duplicate files or logic
- ❌ No leftover test or debug artifacts

---

## Definition of Done
- All 6 Specs implemented via Claude Code
- Console application demonstrates all required behaviors
- Clean repository structure
- Phase I ready for Phase II evolution
```

## Response Summary

Created a comprehensive specification for the Todo CLI application feature. The specification includes:

- 6 detailed user stories covering all required functionality (add, view, update, delete, mark complete/incomplete, and environment setup)
- Clear acceptance scenarios for each user story
- Identified edge cases and error conditions
- 10 functional requirements with clear testable criteria
- 2 key entities (TodoItem and TodoList)
- 7 measurable success criteria

The specification adheres to all constraints specified in the user input, focusing on an in-memory Python console application without persistence, AI features, or cloud deployment. The specification is complete and ready for the planning phase.

## Outcome

Specification successfully created at `specs/001-todo-cli-app/spec.md` with all required sections and quality validation checklist at `specs/001-todo-cli-app/checklists/requirements.md`. The feature branch `001-todo-cli-app` has been created with all necessary directories.