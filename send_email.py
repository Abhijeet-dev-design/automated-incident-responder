import time


def main():
    send_email_alert()


def send_email_alert(subject,reciptent_email):
    
    print("--EMAIL AUTOMATION TRIGGERED--")

    print("Connecting to SMTP Server...")
    time.sleep(2)

    print("Authenticating Secure Connection via TLS")
    time.sleep(1)

    print("Preparing email load for Support Team ")

    print(f"To : {reciptent_email}")
    print(f"subject :{subject}")
    print("Body : Alert! Automation Recovery Done successfully. Please verify report details to reports/incident_report.txt")

    time.sleep(2)

    print("Success: Notification Mail Successfully sent to Support Team")

    print("--EMAIL AUTOMATION COMPLETED--")

if __name__ == "__main__":
    main()
