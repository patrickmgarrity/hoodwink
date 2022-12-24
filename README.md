**How to Use Hoodwink?**

This project currently provides python scripts that generate lists that allow you to better understand your SaaS licensing and help implement security best practices.

**The Security Use Case for Hoodwink** 

SaaS applications are frequently provisioned with overly broad access. By aligning with the principals of least priveledged access, you can identify where there is opportunity to prune unused user accounts and application access.

[**Hoodwink for Duo Security**](https://github.com/patrickmgarrity/hoodwink/tree/main/Duo%20Security)

- [hoodwink-duo.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo.py) - Identify how many unique unique users accessed an application in the past 180-days.
- [hoodwink-duo-sms-users.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-sms-users.py) - Identify users that use SMS authentication for MFA.
- [hoodwink-duo-bypass.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-bypass.py) - Identify user accounts that have recently bypassed MFA.
- [hoodwink-duo-country.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-country.py) - Identify which countries users are accessing applications from.

[**Hoodwink for Okta**](https://github.com/patrickmgarrity/hoodwink/tree/main/OKTA)

- [hoodwink-okta.py](https://github.com/patrickmgarrity/hoodwink/blob/main/OKTA/hoodwink-okta.py) - Identify how many unique unique users accessed an application.
- [hoodwink-okta-country.py](https://github.com/patrickmgarrity/hoodwink/blob/main/OKTA/hoodwink-okta-country.py) - Identify which countries users are accessing applications from.

[**Hoodwink for Azure**](https://github.com/patrickmgarrity/hoodwink/tree/main/Azure)

- [hoodwink-azure.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/hoodwink-azure.py) - Identify how many unique users accessed an application.

**hoodwink-google-workspace**

Coming Soon...

**Considerations**
- This project is based on a theory that I am in the process of validating. I expect the results might require modifications of the scrips I am building and I plan to re-iterate on them over time. Everyone is welcome to help contribute to this project. 
- The Duo script is likely most valuable if you use Duo SSO for SaaS applications. 

**Discloser**

I am not a developer... These scripts are created using ChatGPL and have only been tested by me at this time. I take no responsibility for the accuracy of these scripts. This is not intenteded to be a full time project and is an experiment with ChatGPL. Please feel free to contribute to the project and provide feedback at https://www.linkedin.com/in/patrickmgarrity/
