import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the name and age values
name = input("Enter name: ")
age = input("Enter age: ")

# Read the name and age values from the first row of the sheet
expected_name = sheet.cell(row=1, column=1).value
expected_age = sheet.cell(row=1, column=2).value

# Check if the user's input matches the expected values
if name == expected_name and age == expected_age:
    print("Input is correct.")
else:
    print("Input is incorrect.")
