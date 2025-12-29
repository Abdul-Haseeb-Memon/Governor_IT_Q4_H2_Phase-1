# Todo CLI Application

This is a Todo Command Line Interface application built with Python 3.13+.

## Setup Instructions

### Prerequisites
- Python 3.13+
- UV package manager

### Installation

1. Install Python 3.13+ on your system:
   - **Windows**:
     - Install from [python.org](https://www.python.org/downloads/) (make sure to check "Add Python to PATH")
     - Or use WSL2 with Ubuntu (recommended for Windows users)
   - **macOS**:
     - Use Homebrew: `brew install python@3.13`
     - Or install from [python.org](https://www.python.org/downloads/)
   - **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install python3.13 python3.13-venv python3.13-dev`
   - **Linux (CentOS/RHEL/Fedora)**: `sudo dnf install python3.13 python3.13-pip`

2. Verify Python installation:
   ```bash
   python3 --version
   # Should output Python 3.13.x or higher
   ```

3. Install UV package manager:
   ```bash
   pip install uv
   # Or on macOS/Linux:
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

4. Install project dependencies:
   ```bash
   uv sync
   ```

5. Run the application:
   ```bash
   python -m todo.main
   ```

### For Windows Users
If you're on Windows, it's recommended to use WSL2 with Ubuntu 22.04 for the best development experience:

1. Install WSL2:
   - Open PowerShell as Administrator and run:
   ```powershell
   wsl --install
   ```
   - This will install WSL2 and the default Linux distribution

2. Install Ubuntu 22.04:
   - Option A: From Microsoft Store: https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW
   - Option B: Using command line after WSL installation:
   ```powershell
   wsl --install -d Ubuntu-22.04
   ```

3. After installation, restart your computer

4. Follow the Linux installation instructions within WSL2

For more information about WSL installation, visit: https://docs.microsoft.com/en-us/windows/wsl/install

## Usage

```bash
# Run
python main.py

# Add a todo
python -m todo add "Buy groceries"

# List todos
python -m todo list

# Complete a todo
python -m todo complete 1
```

## Development

This project uses the Agentic Dev Stack workflow (Spec → Plan → Tasks → Claude Code).

To run tests:
```bash
# Run unit tests
python -m pytest tests/unit/

# Run all tests
python -m pytest
```
