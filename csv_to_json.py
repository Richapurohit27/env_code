import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("organizations-100.csv")

# Convert DataFrame to JSON array
json_array = df.to_json(orient="records")

# Save the JSON array into a JSON file
with open("organizations-100.json", "w") as json_file:
    json_file.write(json_array)
