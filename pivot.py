import pandas as pd

# Define the path to your Excel file
excel_file_path = 'C:\\Users\\tl323\\de_practice\\BH data1.xlsx'

# Specify the sheet name where the data is located
sheet_name = 'US L & OS Split by State'

# Read the data from the Excel sheet into a pandas DataFrame
data = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=[5, 6])

# Unstack the second level of the columns to make it easier to work with
data.columns = data.columns.map('_'.join)

# Unpivot the DataFrame
df_melted = pd.melt(data, id_vars=['Unnamed: 0_level_0_DATE'], var_name='Location_Type', value_name='Value')

# Extract relevant data
df_melted[['Location', 'Type']] = df_melted['Location_Type'].str.split('_', expand=True)

# Extract relevant data
extracted_data = df_melted[['Unnamed: 0_level_0_DATE', 'Location', 'Type', 'Value']]

# Rename the columns for clarity
extracted_data.columns = ['DATE', 'Location', 'Type', 'Value']

# Display the result
print(extracted_data)


# Select distinct regions
distinct_regions = extracted_data['Location'].unique()
print(distinct_regions)


# Convert DataFrame to list of dictionaries
example_data = extracted_data.to_dict(orient='records')

# Display the result
print(example_data)


# for data in example_data:
#     if data['Type']=='Land' :
#         data['Type']=1
#     elif data['Type']=='Offshore' :
#         data['Type']=2


# Convert the list of dictionaries to a DataFrame
new_df = pd.DataFrame(example_data)

# Specify the path for the new Excel file
new_excel_path = 'C:\\Users\\tl323\\de_practice\\new_data.xlsx'

# Write the DataFrame to the new Excel file
new_df.to_excel(new_excel_path, index=False)

# Print a message indicating the file has been created
print(f"New Excel file created at: {new_excel_path}")