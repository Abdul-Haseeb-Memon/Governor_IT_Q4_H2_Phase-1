#!/bin/bash
# WSL 2 installation script for Windows users

echo "Checking WSL installation..."

# Check if running on Windows
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Running on Windows. Checking for WSL..."

    # Try to check WSL version
    if command -v wsl &> /dev/null; then
        WSL_VERSION=$(wsl --version 2>&1)
        if [[ $? -eq 0 ]]; then
            echo "✓ WSL is installed:"
            wsl --version
            exit 0
        fi
    fi

    echo "WSL is not installed. Installing WSL2 with Ubuntu 22.04..."
    echo "Please run the following command in an elevated PowerShell as Administrator:"
    echo ""
    echo "    wsl --install"
    echo ""
    echo "This will install WSL2 and the default Linux distribution (Ubuntu)."
    echo "After installation, restart your computer and then run:"
    echo "    wsl --install -d Ubuntu-22.04"
    echo ""
    echo "For more information, visit: https://docs.microsoft.com/en-us/windows/wsl/install"
    exit 0
else
    echo "✓ Not running on Windows. WSL installation not required."
    echo "Current OS: $OSTYPE"
    exit 0
fi