print("""
░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░░██████╗
██╔════╝████╗░████║██╔══██╗██║██║░░░░░██╔════╝
█████╗░░██╔████╔██║███████║██║██║░░░░░╚█████╗░
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░░╚═══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗██████╔╝
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░""")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

sender_email = input("Enter your email: ")
app_password = input("Enter app password: ")

def create_message(sender, receiver, body_text):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "Automated Message"
    message.attach(MIMEText(body_text, "plain"))
    return message

def loop():
    # Prompt for the message once before sending to the list
    body_text = input('Enter the message you want to send: ')
    
    try:
        with open("targets.txt", "r", encoding="utf-8") as file:
            targets = [line.strip() for line in file if line.strip()]
            
        if not targets:
            print("No targets found in targets.txt!")
            return

        try:
            # Fixed typos: SMTP and starttls
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
        except Exception as ex:
            print(f"Connection/Login failed: {ex}")
            return

        for receiver_email in targets:
            try:
                message = create_message(sender_email, receiver_email, body_text)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print(f"{receiver_email} - successfully sent!")
                time.sleep(2)
            except Exception as x:
                print(f"Failed to send to {receiver_email}: {x}")
                
        server.quit()
        
    except FileNotFoundError:
        print("The targets.txt file was not found!")

if __name__ == "__main__":
    loop()