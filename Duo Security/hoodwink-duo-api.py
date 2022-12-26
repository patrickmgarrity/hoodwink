#!/usr/bin/env python
import duo_client
import json
from datetime import datetime, timedelta

def get_next_arg(prompt):
    return input(prompt)

# Configuration and information about objects to create.
admin_api = duo_client.Admin(
    ikey=get_next_arg('Admin API integration key ("DI..."): '),
    skey=get_next_arg('integration secret key: '),
    host=get_next_arg('API hostname ("api-....duosecurity.com"): '),
)

# Download all logs from the past 180 days
start_time = datetime.utcnow() - timedelta(days=180)
end_time = datetime.utcnow()
logs = admin_api.get_authentication_log(start=start_time, end=end_time)

# Save the logs in a JSON file
with open('logs.json', 'w') as f:
    json.dump(logs, f)

# Calculate the number of unique users per integration
logs_by_integration = {}
for log in logs:
    integration_key = log['integration']
    if log['result'] == 'SUCCESS':
        if integration_key not in logs_by_integration:
            logs_by_integration[integration_key] = []
        logs_by_integration[integration_key].append(log)

for integration_key, logs in logs_by_integration.items():
    # Extract the unique usernames from the logs
    usernames = set()
    for log in logs:
        usernames.add(log['username'])

    # Print the number of unique usernames
    print(f"{integration_key}: {len(usernames)} unique users")
