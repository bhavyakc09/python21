import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Initialize variables to hold the input data
name = None
age = None

# Iterate over the rows and columns to read data
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, age = row
    print(f"Name: {name}, Age: {age}")

