**How to use hoodwink-okta**

Hoodwink Okta uses Okta authentication logs to identify how many unique active users accessed an application in the past 180-days. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Okta Admin console 
2. Access Reports>Application Usage
3. Set the time range to 180+ days and click the "Request report" button
4. Check your email for the report link and download the csv 
5. Open hoodwink-okta.py and modify 'insert-your-log-filename.csv' to the name of the downloaded CSV file 
6. Run hoodwink-okta.py w/ the CSV in the same folder

**How to use hoodwink-okta-country**

Hoodwink Okta Country uses Okta authentication logs to identify how many successful authentication attempts have been successful per country. This information can be used to identify where users are logging in from which could help identify risky or malicious access to systems. 

1. Access your Okta Admin console 
2. Access Reports>System Log
3. Set the time range to 180+ days and click the "Download CSV" link 
5. Open hoodwink-okta-country.py and modify 'insert-your-log-filename.csv' to the name of the downloaded CSV file 
6. Run hoodwink-okta-country.py w/ the CSV file in the same folder