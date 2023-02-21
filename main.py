import pandas as pd

# read data from Excel file
data = pd.read_excel('input_data.xlsx')

# process data (replace with your own processing logic)
processed_data = data * 2

# save output to a text file
with open('output_data.txt', 'w') as f:
    f.write(str(processed_data))
