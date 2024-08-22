# Create a Python program to separate alphabetic and numeric characters 
# from the given string: '3Cf5gVHt7IY1kFzjLoqPmZd6x9vn0S'

# ail='3Cf5gVHt7IY1kFzjLoqPmZd6x9vn0S'
# num=[]
# alp=[]
# for i in ail :
#     if i.isnumeric() :
#         num.append(i)
#     else:
#         alp.append(i)
# print(num)
# print(alp)

# Use list comprehension to obtain numbers between 1 and 10, excluding 7: 
# [1, 2, 3, 4, 5, 6, 8, 9,10]

# list1= [i for i in range(1,10) if i!=7]
# print(list1)


# Develop a Python function that takes first name, last name, and email as arguments, and
#  appends the data to a CSV file each time the function is called.

# shikha.sharma@terminus.com, Shikha Sharma
# dipesh.sehgal@terminus.com, Dipesh Sehgal

# import pandas as pd 



# import pandas as pd

# data = [{'email': 'shikha.sharma@terminus.com', 'name': 'Shikha Sharma'},
#         {'email': 'dipesh.sehgal@terminus.com', 'name': 'Dipesh Sehgal'}]

# def emp_details(data):
#     df = pd.DataFrame(data)
#     print(df)

#     # To write the DataFrame to an Excel file
#     df.to_excel('employee_details.xlsx', index=False)

# # Call the function
# emp_details(data)


# How do you merge the values of Dict1 into Dict2?
# Dict1 = {'id': 83673} and Dict2 = {'name': 'john doe'}.

# Dict1 = {'id': 83673} 
# Dict2 = {'name': 'john doe'}
# dict3= {**Dict1,**Dict2}
# print(dict3)

# Dict1.update(Dict2)
# print(Dict1)
# # ginja template engine


# import csv

# def csv_data(name, email):
#     # Splitting the name into first name and last name
#     first_name, last_name = name.split()

#     # Appending data to CSV file
#     with open('data.csv', 'a', newline='') as csvfile:
#         fieldnames = ['Email', 'First Name', 'Last Name']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         # Checking if the file is empty, if yes, write the header
#         if csvfile.tell() == 0:
#             writer.writeheader()

#         # Writing data to CSV
#         writer.writerow({'Email': email, 'First Name': first_name, 'Last Name': last_name})

# # Example usage:
# csv_data('Shikha Sharma', 'shikha.sharma@terminus.com')
# csv_data('Dipesh Sehgal', 'dipesh.sehgal@terminus.com')

