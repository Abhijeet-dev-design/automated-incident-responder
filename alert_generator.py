def main():
    generate_alert()

def generate_alert():
    with open("logs/alerts.log", "a") as file:
        file.write("[Error] Server Down\n")
         
    print("Alert generated Successfully")

main()

