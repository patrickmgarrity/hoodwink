**How to use hoodwink-duo**

Hoodwink Duo uses Duo Security authentication logs to identify how many unique active users accessed an application in the past 180-days. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo.py 
5. Open hoodwink-duo.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo.py w/ the JSON file in the same folder

A list will print with the number of Unique Users for each integration. 

 **How to use hoodwink-duo-api**

Hoodwink Duo uses Duo Security's API to collect authentication logs to identify how many unique active users accessed an application in the past 180-days. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Duo Security console
2. Add a new application and pick Admin API
3. Configure the API permissions for only "Grant read log" access
4. Install the duo_client_python library: $ pip install duo-client
https://github.com/duosecurity/duo_client_python/blob/master/README.md
5. Run the hoodwink-duo-api.py script

A list will print with the number of Unique Users for each integration.

**How to use hoodwink-duo-bypass**

Hoodwink Duo Bypass uses Duo Security authentication logs to identify users that successfully authenticated using a bypass authentication method. Bypassing MFA is against best practices and when used often goes forgotten. Quickly identify which users are bypassing MFA so you can take action.

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo-bypass.py 
5. Open hoodwink-duo-bypass.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo-bypass.py w/ the JSON file in the same folder

A list will print with users that have bypassed MFA.

**How to use hoodwink-duo-sms-users**

Hoodwink Duo SMS Users uses Duo Security authentication logs to identify users that successfully authenticated using the SMS authentication method. Using SMS for MFA is against best practices and we strongly recommend disabling SMS authentication in [Duo Security's global policy settings](https://duo.com/docs/policy#authentication-methods). But before you do, this script will help assess what users will be impacted.

1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo-sms-users.py 
5. Open hoodwink-duo-sms-users.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo-sms-users.py w/ the JSON file in the same folder

A list will print with users that use SMS authentication factors.