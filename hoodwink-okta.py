import csv

# create an empty dictionary to store the counts
counts = {}

# open the csv file and read the rows
with open('insert-your-log-filename.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  
  # skip the header row
  next(reader)
  
  # iterate through the rows
  for row in reader:
    instance_name = row[3]
    login = row[1]
    
    # if the instance name is not in the dictionary, add it and create an empty set
    if instance_name not in counts:
      counts[instance_name] = set()
    # if the login is not in the set for the instance name, add it
    if login not in counts[instance_name]:
      counts[instance_name].add(login)

# print the results
for instance_name, logins in counts.items():
  print(f'{instance_name}: {len(logins)} unique active logins')