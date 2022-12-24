**hoodwink-azure**
Hoodwink Azure uses Azure AD authentication logs to identify how many unique active users accessed an application over the time defined. This information can be used to help right size your SaaS licensing and determine how many users actually need access to an application. 

1. Access your Microsoft Azure Console
2. Open Azure Active Directory

![Azure AD](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad.png)
3. Under monitoring click Sign-in logs

![Azure AD Sign-in Logs](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-sign-in-logs.png)
3. Set your desired time

![Azure AD Date](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-sign-in-logs-date.png)
4. Click Download > Download JSON

![Download JSON](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-download-json.png)
5. Download the Interactive Sign-ins

![Download JSON](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/readme-images/azure-ad-interactive-signins.png)
6. Open hoodwink-azure.py and modify 'insert-your-log-filename.json' to the name of the downloaded JSON file 
7. Run hoodwink-azure.py w/ the JSON CSV in the same folder

A list will print with the number of Unique Users for each application.