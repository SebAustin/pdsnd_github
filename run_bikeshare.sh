#!/bin/bash

# Bikeshare Data Analysis - Run Script
# This script activates the virtual environment and runs the bikeshare analysis

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run the bikeshare script
echo "Starting Bikeshare Data Analysis..."
echo "=========================================="
python bikeshare.py

# Deactivate when done
deactivate

