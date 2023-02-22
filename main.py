import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the cell reference
cell_reference = input("Enter the cell reference (e.g. A1): ")

# Get the value from the corresponding cell
value = sheet[cell_reference].value

# Print the input value
print(f"Value at {cell_reference}: {value}")
