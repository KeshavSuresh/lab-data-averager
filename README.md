# Lab Data Averager

A command-line tool that calculates min, max, and average for each column in a lab data CSV file.
Built as a practical tool for research assistant work in university labs.

## What it does
- Takes any CSV file containing numerical lab measurements
- Automatically detects all numerical columns
- Calculates minimum, maximum, and average for each column
- Exports a clean summary to a text file
- Handles non-numeric values gracefully by skipping them
- Re-prompts if an invalid filename is entered

## Input format
A CSV file with a header row and numerical data. Example:

sample,voltage,current,temperature
A,2.3,0.5,25.1
B,2.7,0.6,26.3

## Output format
voltage — Min: 2.1  Max: 2.7  Average: 2.40
current — Min: 0.4  Max: 0.6  Average: 0.51
temperature — Min: 24.8  Max: 26.3  Average: 25.52

## How to run it
Make sure you have Python installed, then run:

    python averager.py

You will be prompted to enter:
1. Your input CSV filename (re-prompted if file is not found)
2. A name for the output summary file

## Error handling
- If the input file does not exist, the program asks again instead of crashing
- If a cell contains a non-numeric value, that value is skipped with a message
- Any column named "sample" is automatically ignored

## Skills used
- Python
- CSV file handling
- Float conversion and math on lists
- Error handling with loops and try/except
- File input and output

## Built by
Keshav Suresh
Incoming Waterloo Nanotechnology Engineering, Fall 2026
LinkedIn: linkedin.com/in/keshav-suresh-74926b361
