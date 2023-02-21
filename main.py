import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Iterate over the rows and columns to read data
for row in sheet.iter_rows(values_only=True):
    for cell in row:
        print(cell)
