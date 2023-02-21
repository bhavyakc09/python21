import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Read the name and age values from the first row
name = sheet.cell(row=1, column=1).value
age = sheet.cell(row=1, column=2).value

# Print the values
print(f"Name: {name}, Age: {age}")
