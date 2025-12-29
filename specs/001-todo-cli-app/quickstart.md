# Quickstart Guide: Environment Setup & Development Plan

## Environment Setup

### Prerequisites
- Python 3.13+
- UV (Python environment & dependency manager)
- Claude Code and Spec-Kit Plus

### Windows Setup
1. Install WSL 2:
   ```bash
   wsl --install
   wsl --set-default-version 2
   ```

2. Install Ubuntu 22.04 from Microsoft Store

3. Open WSL 2 and verify Python installation:
   ```bash
   python3 --version
   ```

### macOS/Linux Setup
1. Install Python 3.13+ using your preferred method (pyenv, homebrew, etc.)
2. Verify Python version:
   ```bash
   python3 --version
   ```

### Install UV
```bash
pip install uv
```

## Development Environment Setup

1. Verify Claude Code installation:
   ```bash
   claude --version
   ```

2. Verify Spec-Kit Plus is available:
   ```bash
   # Check if spec commands are available
   claude sp --help
   ```

3. Set up the project structure:
   ```
   todo-cli-app/
   ├── specs/
   │   └── 001-todo-cli-app/
   │       ├── spec.md
   │       ├── plan.md
   │       ├── research.md
   │       ├── data-model.md
   │       ├── quickstart.md
   │       ├── contracts/
   │       └── checklists/
   ├── history/
   │   └── prompts/
   │       └── 001-todo-cli-app/
   ├── README.md
   ├── CLAUDE.md
   └── pyproject.toml
   ```

4. Initialize the Python project:
   ```bash
   uv init
   ```

5. Install project dependencies (as defined in pyproject.toml):
   ```bash
   uv sync
   ```

## Phase 1 Constitution Setup

1. Generate the Phase 1 Constitution file with objectives, scope, constraints, and success criteria
2. Create README.md and CLAUDE.md placeholders
3. Verify environment is ready for Phase 1 Todo Specs 2–6 implementation

## Development Workflow

1. Use the Agentic Dev Stack workflow:
   - Write spec
   - Generate plan
   - Break into tasks
   - Implement via Claude Code

2. Follow the spec-driven development approach
3. Ensure no manual code writing
4. Maintain clean architecture principles
5. Verify all constitution constraints are met