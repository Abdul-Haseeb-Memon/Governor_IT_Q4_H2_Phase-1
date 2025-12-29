#!/bin/bash
# UV installation script

echo "Checking UV installation..."

# Check if UV is installed
if command -v uv &> /dev/null; then
    UV_VERSION=$(uv --version)
    echo "✓ UV is installed: $UV_VERSION"
    exit 0
else
    echo "UV is not installed. Installing UV..."

    # Install UV using the official installation script
    if command -v curl &> /dev/null; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        # Add UV to PATH for this session
        source $HOME/.local/bin/env
        echo "✓ UV installed successfully"
        UV_VERSION=$(uv --version)
        echo "UV version: $UV_VERSION"
        exit 0
    elif command -v wget &> /dev/null; then
        wget -qO- https://astral.sh/uv/install.sh | sh
        # Add UV to PATH for this session
        source $HOME/.local/bin/env
        echo "✓ UV installed successfully"
        UV_VERSION=$(uv --version)
        echo "UV version: $UV_VERSION"
        exit 0
    else
        echo "✗ Neither curl nor wget is available to download UV installer"
        echo "Please install curl or wget first, or install UV manually from https://github.com/astral-sh/uv"
        exit 1
    fi
fi