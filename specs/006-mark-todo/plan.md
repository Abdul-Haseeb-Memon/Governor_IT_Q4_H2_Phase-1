# Implementation Plan: Mark Todo Complete/Incomplete

**Feature**: 006-mark-todo
**Created**: 2025-12-29
**Status**: Draft
**Spec**: [specs/006-mark-todo/spec.md](file:///D:/PR0j3CTs/HACKATHON_02/T0D0_List_Phase_01/specs/006-mark-todo/spec.md)

## Technical Context

**Problem**: Need to implement functionality that allows users to toggle the completion status of existing todo items in memory via console command using the todo's ID.

**Solution Approach**:
- Create mark_todo.py module with status update functionality
- Add complete and incomplete commands to main.py CLI interface
- Implement validation for ID existence
- Update todo status in in-memory storage

**Technology Stack**:
- Python 3.14
- In-memory data structures
- argparse for CLI parsing
- UUID for todo identification
- Dataclasses for data modeling
- TodoStatus enum for status management

**Project Structure**:
- `src/todo/mark_todo.py` - Status update functionality implementation
- `src/todo/main.py` - CLI command integration
- `src/todo/model.py` - Todo data model (existing)

**Dependencies**:
- Standard Python libraries only
- Existing src/todo/model.py (TodoItem, TodoList classes, TodoStatus enum)
- Existing src/todo/add_todo.py (for reference patterns)
- Existing src/todo/view_todo.py (for reference patterns)
- Existing src/todo/update_todo.py (for reference patterns)
- Existing src/todo/delete_todo.py (for reference patterns)

**Constraints**:
- ❌ No persistence (in-memory only)
- ❌ No external libraries
- ❌ No AI implementation
- ❌ No manual coding (spec-driven)
- All code must be Claude Code generated

## Constitution Check

### SDD Principles Verification

- [X] **Spec-Driven**: Feature fully specified in `specs/006-mark-todo/spec.md`
- [X] **Zero Manual Coding**: Implementation will be Claude Code generated only
- [X] **Clean Architecture**: Follows existing separation of concerns
- [X] **Minimal Changes**: Only implement required functionality
- [X] **Testable Design**: Each user story independently testable

### Architecture Compliance

- [X] **In-Memory Only**: No persistence layer needed
- [X] **CLI Interface**: Follows existing argparse patterns
- [X] **Data Validation**: Proper validation for ID existence
- [X] **Error Handling**: Appropriate error messages for invalid inputs

### Risk Assessment

- [X] **Low Complexity**: Simple status update operation on existing data structure
- [X] **No Breaking Changes**: Adding new functionality without modifying existing
- [X] **Memory Safety**: Using existing in-memory model safely

## Gates

### Gate 1: Specification Clarity ✅
- Feature requirements clearly defined
- User stories with acceptance criteria
- Edge cases identified
- Success criteria measurable

### Gate 2: Technical Feasibility ✅
- Existing data model supports status updates
- Architecture allows new CLI commands
- Validation requirements clear
- No external dependencies needed

### Gate 3: Implementation Constraints ✅
- All constraints from spec can be satisfied
- No persistence requirement aligns with in-memory model
- No AI requirement aligns with simple status update logic
- Manual coding prohibition will be followed

## Phase 0: Research & Decisions

### R01: Status Update Mechanism Research
**Decision**: Use direct property assignment to update status on existing TodoItem instance
**Rationale**: Simple, efficient, and maintains object identity
**Alternatives considered**: Creating new TodoItem vs updating existing - chose update to preserve references

### R02: CLI Command Pattern
**Decision**: Follow same pattern as existing commands but extend complete command to handle status updates
**Rationale**: Consistency with existing codebase patterns
**Alternatives considered**: Separate complete/incomplete commands vs single command with different behavior

### R03: Validation Strategy
**Decision**: Validate at both CLI entry point and model level
**Rationale**: Early validation with clear error messages
**Alternatives considered**: Model-only validation - chose dual validation for better UX

## Phase 1: Design Artifacts

### Data Model Reference
- **TodoItem**: Existing model with id, title, description, status properties
- **TodoStatus**: Existing enum with INCOMPLETE and COMPLETE values
- **TodoList**: Existing in-memory storage with get_item, update_status methods needed
- **Validation**: ID must exist in collection before status update

### API Contract (CLI)
```
Command: python -m src.todo.main complete [ID]
- ID: UUID string of existing todo to mark as complete

Command: python -m src.todo.main incomplete [ID]
- ID: UUID string of existing todo to mark as incomplete
```

### Quickstart Guide
1. Extend existing complete command or add new incomplete command to main CLI
2. Implement mark_todo function for status updates
3. Validate input (ID exists)
4. Update status in memory
5. Confirm status change to user

## Phase 2: Implementation Plan

### P2-01: Update Todo Model Methods
- Extend TodoList class with update_status method
- Add validation for ID existence
- Implement safe status updates

### P2-02: Create Mark Todo Module
- Implement mark_todo function
- Handle validation logic
- Provide success/error feedback

### P2-03: Integrate CLI Commands
- Update complete subcommand in main.py to actually complete items
- Add incomplete subcommand to main.py
- Parse arguments correctly
- Call status update functionality

### P2-04: Testing and Validation
- Test successful status updates
- Test error cases (invalid ID)
- Verify status changes persist in memory