# Automated Incident Responder & Monitoring System

An automated Python-based automation pipeline that monitors application logs for critical interface failures, automatically triggers a recovery workflow (killing zombie processes, clearing caches, and restarting services), generates an incident report, and dispatches an email alert to the production support team.

---

## System Architecture & Flow

This project follows a modular design where each script handles a single responsibility in the self-healing pipeline:

[alert_generator.py]  --> Generates fake production issues
│
▼
[logs/alerts.log]     --> Centralized log store (System Diary)
│
▼
[monitor.py]          --> Continuously parses logs for "[ERROR]" & "DOWN"
│
▼
[restart_service.py]  --> Auto-recovery (Kills zombie processes, clears cache, restarts service)
│
▼
[report_generator.py] --> Documents the issue and action taken
│
▼
[reports/incident_report.txt] --> Saved artifact of the incident
│
▼
[send_email.py]       --> Dispatches TLS-secured SMTP email notification


---

##  Project Structure

text
.
├── alert_generator.py       # Simulates production/server failures
├── monitor.py               # Main monitoring daemon / orchestrator
├── restart_service.py       # Recovery & self-healing automation script
├── report_generator.py      # Generates incident text reports
├── send_email.py            # Handles SMTP configuration and email sending
├── logs/
│   └── alerts.log           # Application logs (monitored by system)
└── reports/
    └── incident_report.txt  # Auto-generated incident summaries

 Components & Responsibilities
1. alert_generator.py
Role: Simulates a production issue by injecting a breakdown signature into the logs.

Example Log Entry: [ERROR] Geneos_Interface DOWN

2. monitor.py
Role: The core engine. It periodically reads logs/alerts.log searching for specific keywords ([error] and down). Once found, it stops looking and triggers the recovery pipeline.

3. restart_service.py
Role: Mimics the actions of a Production Support Engineer. It clears system temp caches, kills stuck/zombie processes, and executes a simulated systemctl restart (or triggers an Autosys job).

4. report_generator.py
Role: Creates official documentation for audit trails. It logs the exact timestamp, root cause, action taken, and final resolution state inside the reports/ directory.

5. send_email.py
Role: Connects via SMTP over a secure TLS connection to notify the on-call support mailbox that a self-healing action was successfully completed.

How to Run the Project

Prerequisites
Python 3.x installed.

Standard Python libraries (os, time, smtplib).

Step-by-Step Execution
Clone the project & navigate to the directory:


1) cd automated-incident-responder
Generate a Simulated Error:
Run your alert generator to create a fake failure signature inside the logs:


 python alert_generator.py

Start the Monitoring Daemon:
Run the monitor script to look for the issue, auto-heal the service, generate a report, and send an email:


 python monitor.py

Sample Automation Output
checking Log file

 Alert Detected [Error] Server Down
Restarting service
--Automation Recovery Process Started---
Application support Automation_Triggered
Killing Zombie  and stuck process
clearing temp cache 
Executing systemctl restart servicename
Successful Restarted Service
--Automation Recovery Done---
Report successfully generated at reports/incident_report.txt
--EMAIL AUTOMATION TRIGGERED--
Connecting to SMTP Server...
Authenticating Secure Connection via TLS
Preparing email load for Support Team 
To : abhixxx.gmail.com
subject :Resolved:[Error] Server Down
Body : Alert! Automation Recovery Done successfully. Please verify report details to reports/incident_report.txt
Success: Notification Mail Successfully sent to Support Team
--EMAIL AUTOMATION COMPLETED-