import pandas as pd

# Read the CSV files into data frames
megamart_sales = pd.read_csv("C:\\Users\\tl323\\de_practice\\MegaMart_sales.csv")
megamart_new_sales = pd.read_csv("C:\\Users\\tl323\\de_practice\\MegaMart_newsales.csv")

# # Concatenate or merge the data frames
# combined_df = pd.concat([megamart_sales, megamart_new_sales], ignore_index=True)

# # # Filter for rows where the category is 'Office Supplies'
# # office_supplies_df = combined_df[combined_df['Category'] == 'Office Supplies']

# # # Find the total sales value of the category 'Office Supplies'
# # total_sales_office_supplies = office_supplies_df['Sales'].sum()

# # Group by category and sum up the sales value for each category
# sales_by_category = combined_df.groupby('Category')['Sales'].sum()

# # Get the total sales value for the 'Office Supplies' category
# total_sales_office_supplies = sales_by_category.get('Office Supplies', 0)

# print("Total sales value of the category 'Office Supplies':", total_sales_office_supplies)


# Drop duplicate rows
megamart_sales = megamart_sales.drop_duplicates()
megamart_new_sales=megamart_new_sales.drop_duplicates()

# # Filter for rows where the category is 'Office Supplies'
# office_supplies_df = megamart_sales[megamart_sales['Category'] == 'Office Supplies']

# # Concatenate or merge the data frames
# combined_df = pd.concat([megamart_sales, megamart_new_sales], ignore_index=True)

# # # Filter for rows where the category is 'Office Supplies'
# office_supplies_df = combined_df[combined_df['Category'] == 'Office Supplies']

# # # Find the total sales value of the category 'Office Supplies'
# total_sales_office_supplies = office_supplies_df['Sales'].sum()

# print("Total sales value of the category 'Office Supplies' after dropping duplicates:", total_sales_office_supplies)

# Calculate net profit for each row
megamart_sales['Net Profit'] = megamart_sales['Sales'] - megamart_sales['Cost']

# Group by category and subcategory and sum up the net profit for each combination
profit_by_category_subcategory = megamart_sales.groupby(['Category', 'Sub-Category'])['Net Profit'].sum()

# Find the combination with the highest net profit
most_profitable_combination = profit_by_category_subcategory.idxmax()

print("Most profitable category and subcategory combination:", most_profitable_combination)