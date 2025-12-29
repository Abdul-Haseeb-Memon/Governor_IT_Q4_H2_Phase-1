#!/usr/bin/env python3
"""
Python version checker for the Todo CLI application
Verifies that Python 3.13+ is installed and available
"""

import sys

def check_python_version():
    """Check if Python version is 3.13 or higher"""
    major, minor = sys.version_info[:2]

    if major < 3 or (major == 3 and minor < 13):
        print(f"✗ Python version {major}.{minor} is less than required 3.13")
        print("Please install Python 3.13 or higher")
        return False
    else:
        print(f"✓ Python version {major}.{minor} meets requirements (3.13+)")
        return True

if __name__ == "__main__":
    success = check_python_version()
    sys.exit(0 if success else 1)