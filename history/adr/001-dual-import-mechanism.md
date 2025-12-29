# ADR-001: Dual Import Mechanism for Todo List CLI Application

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-29
- **Feature:** 007-interactive-cli
- **Context:** Need to support both module execution (`python -m src.todo`) and direct execution (VS Code "Run") while maintaining clean code organization with proper imports for the Todo List CLI application.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Implement a dual import mechanism that handles both relative imports for module execution and absolute imports for direct execution. The solution uses a try/except block to attempt relative imports first (for `python -m src.todo`), falling back to absolute imports (for direct execution like VS Code "Run").

```python
# Handle both direct execution and module execution
try:
    # When running as module (python -m src.todo)
    from .model import TodoList
    from .add_todo import add_todo
    from .view_todo import view_todos
    from .update_todo import update_todo
    from .delete_todo import delete_todo
    from .mark_todo import mark_todo_complete, mark_todo_incomplete
except ImportError:
    # When running directly (python src/todo/main.py)
    from todo.model import TodoList
    from todo.add_todo import add_todo
    from todo.view_todo import view_todos
    from todo.update_todo import update_todo
    from todo.delete_todo import delete_todo
    from todo.mark_todo import mark_todo_complete, mark_todo_incomplete
```

Additionally, for direct execution, we modify sys.path to ensure proper module resolution:
```python
if __name__ == "__main__":
    # Get the project root directory (two levels up from this file)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
```

## Consequences

### Positive

- Application works seamlessly with both execution methods: `python -m src.todo` and direct execution
- Maintains clean separation of modules while supporting different execution contexts
- Provides compatibility with VS Code "Run" button and command-line module execution
- No breaking changes to existing functionality or import structure
- Enables proper development workflow for both direct debugging and module usage

### Negative

- Slightly more complex import logic that requires understanding of Python's import system
- Potential confusion for developers unfamiliar with dual import patterns
- Additional code path that needs to be maintained and tested
- Runtime import error handling adds minimal overhead

## Alternatives Considered

Alternative A: Single execution method only (either module or direct, not both)
- Why rejected: Would limit development flexibility and user experience

Alternative B: Separate entry point files for each execution method
- Why rejected: Would create code duplication and maintenance overhead

Alternative C: Using sys.path modification for all execution contexts
- Why rejected: Would be less clean and potentially cause import conflicts

## References

- Feature Spec: specs/007-interactive-cli/spec.md
- Implementation Plan: specs/007-interactive-cli/plan.md
- Related ADRs: None
- Evaluator Evidence: Implementation successfully tested with both execution methods