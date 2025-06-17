# CST8919 Lab 2 - Threat Detection with Azure Monitor and KQL

## 👨‍💻 What This Project Does

This is a small Python Flask app with a login route. It logs both successful and failed login attempts. The app is deployed to Azure App Service, and the logs are sent to Azure Monitor.

We use Kusto Query Language (KQL) to check for failed logins. If someone fails to log in many times (like a brute-force attack), we trigger an alert and send an email notification.

---

## 🛠 Technologies Used

- Python Flask  
- Azure App Service  
- Log Analytics Workspace  
- KQL (Kusto Query Language)  
- Azure Monitor Alerts

---

## ✅ What I Learned

- How to build and deploy a Flask app to Azure  
- How to turn on diagnostic logging with Azure Monitor  
- How to write KQL queries to search logs  
- How to make an alert rule to detect suspicious activity

---

## ⚠️ Challenges I Faced

- Setting up diagnostic logs took some trial and error  
- Making sure the logs were actually showing failed logins in Azure  
- Writing a KQL query that shows only failed login attempts

---

## 🧠 How I Would Improve It

In a real-world system, I would:
- Add IP logging to track which IPs are failing  
- Block IPs after too many failed logins  
- Store logins in a database  
- Add multi-factor authentication (MFA)

---

## 🔎 KQL Query Used

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(1h)
| where Message has "FAILED login"
```

### Explanation:
This query looks at logs from the app's console. It filters only the logs from the last 1 hour and shows the ones that contain the phrase "FAILED login".

---

## 📁 Files in This Repo

- `app.py`: Flask app with /login route  
- `requirements.txt`: Python dependencies  
- `test-app.http`: Used to test login requests from VS Code  
- `README.md`: This file

---

## 📹 YouTube Demo

[![Watch the Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

---

## 📬 Alert Rule Setup

- **Scope**: My Log Analytics Workspace  
- **Condition**: More than 5 failed logins in 5 minutes  
- **Frequency**: Every 1 minute  
- **Action Group**: Sends an email to me  
- **Severity**: 2 (Warning)

