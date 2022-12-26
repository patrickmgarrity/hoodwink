**How to Use Hoodwink?**

Project Hoodwink provides visibility and insights into SaaS applications so you can make better SaaS licensing decisions and implement cybersecurity best practices such as least priveledged access.

**The Security Use Case for Hoodwink** 

SaaS applications are frequently provisioned with overly broad access. By aligning with the principals of least priveledged access, hoodwink helps you identify opportunities to prune unnecessary application access.

[**Hoodwink for Azure**](https://github.com/patrickmgarrity/hoodwink/tree/main/Azure)

- [hoodwink-azure.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Azure/hoodwink-azure.py) - Identify how many unique users accessed each application.

[**Hoodwink for Duo Security**](https://github.com/patrickmgarrity/hoodwink/tree/main/Duo%20Security)

- [hoodwink-duo.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo.py) - Identify how many unique users accessed each application in the past 180-days.
- [hoodwink-duo-sms-users.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-sms-users.py) - Identify users that use SMS authentication for MFA.
- [hoodwink-duo-bypass.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-bypass.py) - Identify user accounts that have recently bypassed MFA.
- [hoodwink-duo-country.py](https://github.com/patrickmgarrity/hoodwink/blob/main/Duo%20Security/hoodwink-duo-country.py) - Identify which countries users are accessing applications from.

[**Hoodwink for Okta**](https://github.com/patrickmgarrity/hoodwink/tree/main/OKTA)

- [hoodwink-okta.py](https://github.com/patrickmgarrity/hoodwink/blob/main/OKTA/hoodwink-okta.py) - Identify how many unique users accessed each application.
- [hoodwink-okta-country.py](https://github.com/patrickmgarrity/hoodwink/blob/main/OKTA/hoodwink-okta-country.py) - Identify which countries users are accessing applications from.

**hoodwink-google-workspace**

Coming Soon...

**Considerations**

- This project is based on a theory that authentication logs can be used to make better decisions about SaaS licensing while helping organizations implement least stronger access controls. Based on community contributed feedback, we plan to re-iterate and develop new scripts over time. Everyone is welcome to help contribute to this project. 

**Discloser**

I am not a developer... These scripts are created using ChatGPL and have only been tested by me at this time. I take no responsibility for the accuracy of these scripts. This is not intenteded to be a full time project and is an experiment with ChatGPL. Please feel free to contribute to the project and provide feedback at https://www.linkedin.com/in/patrickmgarrity/
