import csv

# Initialize a dictionary to store the count of "SUCCESS" results per country
success_counts = {}

# Open the csv file and read it using the csv module
with open('insert-your-log-filename.csv', 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Iterate through each row in the csv file
    for row in reader:
        # Get the value for the "outcome.result" column and the "client.geographical_context.country" column
        result = row[6]
        country = row[24]
        # If the result is "SUCCESS", increment the count for the corresponding country
        if result == 'SUCCESS':
            if country in success_counts:
                success_counts[country] += 1
            else:
                success_counts[country] = 1

# Print the success counts for each country
for country, count in success_counts.items():
    print(f'{country}: {count}')
