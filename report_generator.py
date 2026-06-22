import os
from datetime import datetime


def main():
    generate_report()


def generate_report(issue_name,status):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    report_path = "reports/incident_report.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open(report_path,"w") as file:
        file.write("--Incident Report Summary--\n")
        file.write(f"Incident_time : {current_time}\n")
        file.write(f"Issue_name :{issue_name}\n")
        file.write(f"current_status:{status}\n")
        file.write("(-------------------------)")


    print(f"Report successfully generated at {report_path}")

if __name__ == "__main__":
    main()

        


