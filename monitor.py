import os
import time

from restart_service import restart_application_service

Log_file = "logs/alerts.log"

def main():
    monitor_logs()


def monitor_logs():
    print("checking Log file")

    if not os.path.exists(Log_file):
        print(f"{Log_file} is not available")
        return
    
    with open(Log_file, "r")as file:
        lines = file.readlines()
    

    error_detected = False

    for line in lines:
        if "[error]" in line.lower() and "down"  in line.lower():
            print(f"\n Alert Detected {line.strip()}")
            error_detected = True
            break

    if error_detected:
        print("Restarting service")
        restart_application_service()
        

    else:
        print("System is fine and successful able to reach server")
       

if __name__ == "__main__":
    main()