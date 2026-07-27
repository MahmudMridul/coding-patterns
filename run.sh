#!/bin/bash

# Find the most recently modified file in the solutions directory
LATEST_FILE=$(ls -t solutions/lc_*.py 2>/dev/null | head -n 1)
DIVIDER='========================================'

# Check if a file was actually found
if [ -z "$LATEST_FILE" ]; then
    echo "Error: No LeetCode solution files found in solutions/"
    exit 1
fi

# Print the file being executed for clarity
echo "$DIVIDER"
echo "FILE: $LATEST_FILE"
echo "$DIVIDER"
# Execute the file using uv
uv run "$LATEST_FILE"
