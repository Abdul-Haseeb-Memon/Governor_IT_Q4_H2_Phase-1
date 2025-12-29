#!/bin/bash
# Spec-Kit Plus verification script

echo "Checking Spec-Kit Plus installation..."

# Check if Claude Code is installed (Spec-Kit Plus is part of Claude Code)
if command -v claude &> /dev/null; then
    echo "✓ Claude Code is installed, checking for Spec-Kit Plus commands..."

    # Test if spec-kit commands are available
    if claude sp --help > /dev/null 2>&1; then
        echo "✓ Spec-Kit Plus commands are available:"
        echo ""
        claude sp --help
        echo ""
        echo "✓ Spec-Kit Plus verification completed successfully"
        exit 0
    else
        echo "✗ Spec-Kit Plus commands are not available"
        echo "Spec-Kit Plus should be available as part of Claude Code installation"
        exit 1
    fi
else
    echo "✗ Claude Code is not installed, so Spec-Kit Plus is not available"
    echo "Please install Claude Code first"
    exit 1
fi