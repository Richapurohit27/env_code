import pandas as pd
import datetime

def create_date_dict_list(data):
    date_dict_list = []
    for i in range(2, len(data), 5):
        date_str = data.iloc[i, 0]
        # date = datetime.datetime.strptime(date_str, "%m-%d-%Y")
        date_dict = {"date": date}
        for j in range(1, len(data.columns) - 1, 2):  # Exclude the last column (TOTAL US)
            region_name = data.iloc[i-1, j]
            land_value = data.iloc[i, j]
            offshore_value = data.iloc[i, j + 1]
            region_dict = {"region_name": region_name, "land": land_value, "offshore": offshore_value}
            date_dict[region_name.lower()] = region_dict
        date_dict_list.append(date_dict)
    return date_dict_list

# Example usage:
excel_file_path = 'C:\\Users\\tl323\\de_practice\\BH data.xlsx'
sheet_name = 'US L & OS Split by State'
data = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None, skiprows=2)

date_dict_list = create_date_dict_list(data)

# Function to get land and offshore values for a specific region on a particular date
def get_region_values(date_dict_list, date, region_name):
    for date_dict in date_dict_list:
        if date_dict["date"] == date and region_name.lower() in date_dict:
            region_dict = date_dict[region_name.lower()]
            return region_dict.get("land"), region_dict.get("offshore")
    return None, None

# Example usage:
date = datetime.datetime(2022, 4, 1)
region_name = "Arkansas"

land_value, offshore_value = get_region_values(date_dict_list, date, region_name)

print(f"Land value for {region_name}: {land_value}")
print(f"Offshore value for {region_name}: {offshore_value}")
