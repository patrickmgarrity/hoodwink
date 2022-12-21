import json
from datetime import datetime, timedelta

# 180 days in seconds
PAST_180_DAYS = 180 * 24 * 60 * 60

# Load the JSON logs
with open('insert-your-log-filename.json', 'r') as f:
    logs = json.load(f)

# Initialize a dictionary to store the active users per integration
active_users_per_integration = {}

# Iterate through the logs
for log in logs['data']:
    # Extract the timestamp, integration, and user ID from the log
    timestamp = log['Timestamp (UTC)']
    integration = log['Integration']
    user_id = log['User']

    # Convert the timestamp to a datetime object
    timestamp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f+00:00')

    # Calculate the difference between the current time and the timestamp in seconds
    elapsed_time = (datetime.utcnow() - timestamp_datetime).total_seconds()

    # If the elapsed time is within the past 180 days
    if elapsed_time <= PAST_180_DAYS:
        # Increment the active users for the integration, if the user ID has not been seen before
        if integration in active_users_per_integration:
            if user_id not in active_users_per_integration[integration]:
                active_users_per_integration[integration][user_id] = 1
        else:
            active_users_per_integration[integration] = {user_id: 1}

# Print the number of unique users per integration
for integration, user_ids in sorted(active_users_per_integration.items()):
    print(f'{integration}: {len(user_ids)} unique users')
