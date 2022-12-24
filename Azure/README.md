**hoodwink-azure**
Hoodwink Azure uses Azure AD authentication logs to identify how many unique active users accessed an application over the time defined. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Microsoft Azure Console
2. Open Azure Active Directory
3. Under monitoring click Sign-in logs
3. Set your desired time
4. Click Download > Download JSON
5. Download the Interactive Signons
6. Open hoodwink-okta.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
7. Run hoodwink-azure.py w/ the JSON CSV in the same folder

A list will print with the number of Unique Users for each application. 
