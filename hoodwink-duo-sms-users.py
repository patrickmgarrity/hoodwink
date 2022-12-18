import json

# Load the JSON file
with open("insert-your-log-filename.json", "r") as f:
  data = json.load(f)

# Initialize an empty set to store the unique usernames
unique_usernames = set()

# Iterate through the data
for item in data["data"]:
  # Check if the result is successful and if the reason is either "Bypass Status" or "Bypass Code"
  if item["Result"] == "SUCCESS" and (item["Factor"] == "SMS Passcode"):
    # Add the username to the set of unique usernames
    unique_usernames.add(item["User"])

# Convert the set of unique usernames to a list and print it
print(list(unique_usernames))
