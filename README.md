**How to Use Hoodwink?**

This project currently provides python scripts that use authentication logs to calculate the number of unique active users that log into your SaaS applications over the last 180-days. The scripts generate a list that allows you to better understand your SaaS licensing and security needs.

**The Security Use Case for Hoodwink** 

SaaS applications are frequently provisioned with overly broad access. By aligning with the principals of least priveledged access, you can identify where there is application level opportunity to prune unused user accounts.

**How to use hoodwink-duo**

Hoodwink Duo uses Duo Security authentication logs to identify how many unique active users accessed an application in the past 180-days. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo.py 
5. Open hoodwink-duo.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo.py w/ the JSON file in the same folder

Upon Success You Should See a List Print Out of Unique Users for each integration

**How to use hoodwink-duo-bypass**

Hoodwink Duo Bypass uses Duo Security authentication logs to identify users that successfully authenticated using a bypass authentication method. Bypassing MFA is against best practices and when used often goes forgotten. Quickly identify which users are bypassing MFA so you can take action.

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo-bypass.py 
5. Open hoodwink-duo-bypass.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo-bypass.py w/ the JSON file in the same folder

**How to use hoodwink-duo-sms-users**

Hoodwink Duo SMS Users uses Duo Security authentication logs to identify users that successfully authenticated using the SMS authentication method. Using SMS for MFA is against best practices and we strongly recommend disabling SMS authentication in [Duo Security's global policy settings](https://duo.com/docs/policy#authentication-methods). But before you do, this script will help assess what users will be impacted.

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo-sms-users.py 
5. Open hoodwink-duo-sms-users.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo-sms-users.py w/ the JSON file in the same folder

**How to use hoodwink-okta**

Hoodwink Okta uses Okta authentication logs to identify how many unique active users accessed an application in the past 180-days. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Okta Admin console 
2. Access Reports>Application Usage
3. Set the time range to 180+ days and click the "Request report" button
4. Check your email for the report link and download the csv 
5. Open hoodwink-duo.py and modify 'insert-your-log-filename.csv' to the name of the downloaded CSV file 
6. Run hoodwink-duo.py w/ the JSON CSV in the same folder

**How to use hoodwink-okta-country**

Hoodwink Okta Country uses Okta authentication logs to identify how many successful authentication attempts have been successful per country. This information can be used to identify where users are logging in from which could help identify risky or malicious access to systems. 

1. Access your Okta Admin console 
2. Access Reports>System Log
3. Set the time range to 180+ days and click the "Download CSV" link 
5. Open hoodwink-duo-country.py and modify 'insert-your-log-filename.csv' to the name of the downloaded CSV file 
6. Run hoodwink-duo-country.py w/ the CSV file in the same folder


**hoodwink-azure-ad**

Coming Soon...

**hoodwink-google-workspace**

Coming Soon...

**Considerations**
- This project is based on a theory that I am in the process of validating. I expect the results might require modifications of the scrips I am building and I plan to re-iterate on them over time. Everyone is welcome to help contribute to this project. 
- The Duo script is likely most valuable if you use Duo SSO for SaaS applications. 

**Discloser**

I am not a developer... These scripts are created using ChatGPL and have only been tested by me at this time. I take no responsibility for the accuracy of these scripts. Please feel free to double check my work and provide feedback at https://www.linkedin.com/in/patrickmgarrity/
