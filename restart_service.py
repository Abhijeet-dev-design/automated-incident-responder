import time

def main():
    restart_application_service()


def restart_application_service():
    print("--Automation Recovery Process Started---")
    print("Application support Automation_Triggered")

    time.sleep(2)
    print("Killing Zombie  and stuck process")

    time.sleep(2)
    print("clearing temp cache ")

    time.sleep(2)
    print("Executing systemctl restart servicename")

    print("Successful Restarted Service")

    print("--Automation Recovery Done---")


if __name__ == "__main__":
    main()



