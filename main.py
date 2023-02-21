import openpyxl
import os

file_path = os.path.join(os.getcwd(), 'input_data.xlsx')

# Load the workbook
workbook = openpyxl.load_workbook(file_path)

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the cell coordinates
cell_coordinates = input("Enter the cell coordinates (e.g. A1): ")

# Read the value from the corresponding cell
value = sheet[cell_coordinates].value

# Print the input value
print(f"{cell_coordinates}: {value}")
