import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the input value
input_value = input("Enter the input value: ")

# Print the input value
print(f"Input value: {input_value}")
