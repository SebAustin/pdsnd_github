# Bikeshare Data Analysis Project

## Overview
This project analyzes US bikeshare data for three major cities: **Chicago**, **New York City**, and **Washington**. The interactive Python application allows users to explore bikeshare usage patterns through statistical analysis and data filtering.

## Table of Contents
- [Project Files](#project-files)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Using the Application](#using-the-application)
- [Features](#features)
- [References](#references)

## Project Files
- `bikeshare.py` - Main Python script containing all analysis code
- `chicago.csv` - Bikeshare data for Chicago (not tracked in Git)
- `new_york_city.csv` - Bikeshare data for New York City (not tracked in Git)
- `washington.csv` - Bikeshare data for Washington (not tracked in Git)
- `requirements.txt` - Python package dependencies
- `run_bikeshare.sh` - Shell script to easily run the application
- `.gitignore` - Git ignore file to exclude CSV data files

## Software Requirements
- **Python 3.x** (Python 3.7 or higher recommended)
- **pandas** 2.3.3 - Data manipulation and analysis
- **numpy** 2.3.5 - Numerical computing
- **python-dateutil** 2.9.0 - Date/time utilities
- **pytz** 2025.2 - Timezone support

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add Data Files
Place the CSV data files in the project directory:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

**Note:** These files are excluded from version control via `.gitignore`.

## How to Run

### Option 1: Using the Run Script (Easiest)
```bash
./run_bikeshare.sh
```
This automatically activates the virtual environment and runs the script.

### Option 2: Manual Execution
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Run the script
python bikeshare.py

# Deactivate when done
deactivate
```

### Option 3: Direct Execution
```bash
venv/bin/python bikeshare.py
```

## Using the Application

After starting the script, follow the interactive prompts:

1. **Select a City**: Choose from Chicago, New York City, or Washington
2. **Choose Month Filter**: Select a specific month (January-June) or "all" for no filter
3. **Choose Day Filter**: Select a specific day of the week or "all" for no filter
4. **View Statistics**: The application displays computed statistics
5. **View Raw Data**: Optionally view raw data 5 rows at a time
6. **Restart or Exit**: Choose to analyze different filters or exit

### Example Session
```
Hello! Let's explore some US bikeshare data!

Which city would you like to explore? (Chicago, New York City, Washington)
> New York City

Which month would you like to filter by? (all, January, February, March, April, May, June)
> June

Which day of the week would you like to filter by? (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
> all
```

## Features

### Robust Input Validation
- Case-insensitive input handling
- Clear error messages for invalid inputs
- User-friendly prompts

### Statistical Analysis
The application computes and displays:

#### Time Statistics
- Most popular month for travel
- Most popular day of the week
- Most popular hour of the day

#### Station Statistics
- Most popular start station
- Most popular end station
- Most popular trip (start-end station combination)

#### Trip Duration Statistics
- Total travel time
- Average travel time

#### User Statistics
- User type breakdown (Subscriber vs. Customer)
- Gender distribution (when available)
- Birth year statistics (earliest, most recent, most common)

### Interactive Raw Data Display
- View raw data 5 rows at a time
- Continue viewing or exit at any point

### Error Handling
- Proper handling for missing data columns
- Note: Gender and Birth Year data not available for Washington

## References
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
- Udacity Data Science Nanodegree course materials

## Development Notes
All code was developed following Python best practices:
- Descriptive variable names
- Comprehensive docstrings
- Appropriate data types and structures
- Error handling with try/except blocks
- User-friendly prompts and output formatting

## License
This project is part of the Udacity Data Science Nanodegree program.

## Author
Created as part of the Udacity Programming for Data Science with Python Nanodegree.

