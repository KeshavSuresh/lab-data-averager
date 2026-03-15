import csv
import os

# -----------------------------------------------
# Lab Data Averager
# Built by Keshav Suresh
# Calculates min, max, and average for each column
# -----------------------------------------------

print("Lab Data Averager")
print("-----------------")

# Keep asking until a valid file is entered
filename = input("Enter your CSV filename: ")

while not os.path.exists(filename):
    print("Error: File '" + filename + "' not found. Try again.")
    filename = input("Enter your CSV filename: ")

output = input("Enter output filename (e.g. summary.txt): ")

file = open(filename, "r")
reader = csv.DictReader(file)

# Get column names and remove 'sample' since it's not a number
headers = reader.fieldnames
columns = [col for col in headers if col != "sample"]

# Create an empty list for each column
data = {}
for col in columns:
    data[col] = []

# Loop through every row and collect the numbers
for row in reader:
    for col in columns:
        try:
            data[col].append(float(row[col]))
        except ValueError:
            print("Skipping non-numeric value in column: " + col)

file.close()

# Calculate and display stats
outfile = open(output, "w")
outfile.write("Lab Data Summary\n")
outfile.write("----------------\n")

for col in columns:
    col_min = min(data[col])
    col_max = max(data[col])
    col_avg = round(sum(data[col]) / len(data[col]), 2)

    line = col + " — Min: " + str(col_min) + "  Max: " + str(col_max) + "  Average: " + str(col_avg)
    print(line)
    outfile.write(line + "\n")

outfile.close()

print("----------------")
print("Saved to: " + output)
print("Done.")