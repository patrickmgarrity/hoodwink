import json

# Load the JSON data from the file
with open('insert-your-log-filename.json.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the sets of unique userPrincipalName values
user_sets = {}

# Create a dictionary to map appId values to appDisplayName values
app_names = {}

# Iterate through the JSON data
for entry in data:
    app_id = entry['appId']
    app_display_name = entry['appDisplayName']
    user_name = entry['userPrincipalName']
    
    # Check if the authenticationDetails list is not empty and if the succeeded attribute is set to True
    if entry.get('authenticationDetails', []) and entry['authenticationDetails'][0].get('succeeded', False):
        if app_id in user_sets:
            # If the app id is already in the dictionary, add the userPrincipalName to the set
            user_sets[app_id].add(user_name)
        else:
            # If the app id is not in the dictionary, add it and create a new set with the userPrincipalName value
            user_sets[app_id] = set([user_name])
            app_names[app_id] = app_display_name

# Print the counts for each app name
for app_id, user_set in user_sets.items():
    app_display_name = app_names[app_id]
    count = len(user_set)
    print(f'{app_display_name}: {count} unique userPrincipalName values')
