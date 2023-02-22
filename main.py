import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Get the value from cell A1
cell_value = sheet['A1'].value

# Print the input value
print(f"Input value: {cell_value}")
