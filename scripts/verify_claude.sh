#!/bin/bash
# Claude Code verification script

echo "Checking Claude Code installation..."

# Check if Claude Code is installed
if command -v claude &> /dev/null; then
    CLAUDE_VERSION=$(claude --version 2>&1)
    echo "✓ Claude Code is installed: $CLAUDE_VERSION"

    # Check if Claude Code can run basic commands
    echo "Testing Claude Code functionality..."
    if claude --help > /dev/null 2>&1; then
        echo "✓ Claude Code basic functionality test passed"
    else
        echo "✗ Claude Code basic functionality test failed"
        exit 1
    fi

    # Check if Spec-Kit Plus commands are available
    if claude sp --help > /dev/null 2>&1; then
        echo "✓ Spec-Kit Plus commands are available"
    else
        echo "✗ Spec-Kit Plus commands are not available"
        exit 1
    fi

    exit 0
else
    echo "✗ Claude Code is not installed"
    echo "Please install Claude Code following the instructions at https://docs.anthropic.com/claude/"
    exit 1
fi