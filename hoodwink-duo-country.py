import json

# Load the JSON data from the file
with open('insert-your-log-filename.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the log events per country
log_events_per_country = {}

# Iterate through the data array
for log_event in data['data']:
    # Get the access device country
    country = log_event['Access Device Country']
    # If the country is not in the dictionary, add it and set the value to 1
    if country not in log_events_per_country:
        log_events_per_country[country] = 1
    # If the country is already in the dictionary, increment the value by 1
    else:
        log_events_per_country[country] += 1

# Print the log events per country
for country, count in log_events_per_country.items():
    print(f'{country}: {count} log events')
