import sys
import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Read the cell reference from command line arguments
if len(sys.argv) < 2:
    print("Usage: python main.py [cell reference (e.g. A1)]")
    exit()

cell_reference = sys.argv[1]

# Read the value from the corresponding cell
value = sheet[cell_reference].value

# Print the input value
print(f"{cell_reference}: {value}")
