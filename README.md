**How to Use Hoodwink?**

This project currently provides python scripts that use authentication logs to calculate the number of unique active users that log into your SaaS applications over the last 180-days. The scripts generate a list that allows you to better understand your SaaS licensing needs.

**The Security Use Case for Hoodwink** 

We believe these assessment tools could also be used for assessing active user counts and auditing provisioned users to provide least priveledged access. It's commonly a best practice to remove users from a service that they do not need or use.

**How to use hoodwink-duo**
1. Access your Duo Security console 
2. Access Reports>Authentication Log
3. Set the time range to "Last 180 days" and Export to JSON
4. Download and open hoodwink-duo.py 
5. Open hoodwink-duo.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
6. Run hoodwink-duo.py w/ the JSON in the same folder

Upon Success You Should See a List Print Out of Unique Users for each integration

**How to use hoodwink-okta**

1. Access your Okta Admin console 
2. Access Reports>Application Usage
3. Set the time range to 180+ days and click the "Request report" button
4. Check your email for the report link and download the csv 
5. Open hoodwink-duo.py and modify 'insert-your-log-filename.csv' to the name of the downloaded CSV file 
6. Run hoodwink-duo.py w/ the JSON in the same folder

**hoodwink-azure-ad**

Coming Soon...

**hoodwink-google-workspace**

Coming Soon...

**Considerations**
- This project is based on a theory that I am in the process of validating. I expect the results might require modifications of the scrips I am building and I plan to re-iterate on them over time. Everyone is welcome to help contribute to this project. 
- The Duo script is likely most valuable if you use Duo SSO for SaaS applications. 

**Discloser**

I am not a developer... These scripts are created using ChatGPL and have only been tested by me at this time. I take no responsibility. Please feel free to double check my work and provide feedback at https://www.linkedin.com/in/patrickmgarrity/
