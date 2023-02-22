import openpyxl
import sys

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Read the input coordinates from the command line argument
if len(sys.argv) < 2:
    print("Usage: python main.py <cell_coordinates>")
    exit(1)

cell_coordinates = sys.argv[1]

# Read the value from the corresponding cell
value = sheet[cell_coordinates].value

# Print the input value
print(f"{cell_coordinates}: {value}")
