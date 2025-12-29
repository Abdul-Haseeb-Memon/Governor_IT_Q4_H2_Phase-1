#!/bin/bash
# Python installation verification script

echo "Checking Python version..."

# Check if Python is installed
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "Python version found: $PYTHON_VERSION"

    # Extract major and minor version numbers
    MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d'.' -f2)

    # Check if version is 3.13 or higher
    if [ "$MAJOR_VERSION" -eq 3 ] && [ "$MINOR_VERSION" -ge 13 ]; then
        echo "✓ Python version is 3.13+ (requirements met)"
        exit 0
    else
        echo "✗ Python version is less than 3.13 (requirements not met)"
        echo "Please install Python 3.13 or higher"
        exit 1
    fi
else
    echo "✗ Python is not installed"
    echo "Please install Python 3.13 or higher"
    exit 1
fi