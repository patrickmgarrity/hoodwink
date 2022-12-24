**Hoodwink Azure Overview**

Hoodwink Azure uses Azure AD authentication logs to identify how many unique active users accessed each SaaS application. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

**Setup Instructions**

Step 1: Access your Microsoft Azure Console

Step 2: Open Azure Active Directory

![Azure AD](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad.png)

Step 3: Under monitoring click Sign-in logs

![Azure AD Sign-in Logs](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-sign-in-logs.png)

Step 4: Set your desired time

![Azure AD Date](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-sign-in-logs-date.png)

Step 5: Click Download > Download JSON

![Download JSON](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-download-json.png)

Step 6: Download the Interactive Sign-ins

![Download JSON](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-interactive-signins.png)

Step 7: Open hoodwink-azure.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 

Step 8: Run hoodwink-azure.py w/ the JSON CSV in the same folder

**Example Results**

A list will print with the number of Unique Users for each application.

Example Output

![Azure AD Example Output](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/example-azure-ad-output.png)
