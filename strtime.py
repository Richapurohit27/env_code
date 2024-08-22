from datetime import datetime

# Original date string
date_string = '20200304'

# Parse the date string using strptime() method
date_object = datetime.strptime(date_string, '%Y%m%d')

# Format the date object to the desired format
formatted_date = date_object.strftime('%Y-%m-%d')

# Print the formatted date
print(formatted_date)
