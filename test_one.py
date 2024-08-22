import pandas as pd

# Define the path to your Excel file
excel_file_path = 'C:\\Users\\tl323\\de_practice\\BH data.xlsx'

# Specify the sheet name where the data is located
sheet_name = 'US L & OS Split by State'



# Read data from Excel file
df = pd.read_excel(excel_file_path,skiprows=4)
print(df)




# Drop columns with all NaN values
df = df.dropna(axis=1, how='all')
print(df)
# Extract state columns dynamically
state_columns = [col for col in df.columns if col != 'DATE']

# Unpivot the DataFrame
df_melted = pd.melt(df, id_vars=['DATE'], value_vars=state_columns, var_name='Location', value_name='Value')

# Extract relevant data
extracted_data = df_melted[['DATE', 'Location', 'Value']]

# Display the result
print(extracted_data)
