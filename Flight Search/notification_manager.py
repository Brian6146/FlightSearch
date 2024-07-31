import smtplib
from dotenv import load_dotenv,dotenv_values
import os
class NotificationManager:
    def __init__(self):
        self.my_email="briannambari386@gmail.com"
        self.email_password=os.getenv("EMAIL_PASSWORD")

    def send_email(self,message_body):
        with smtplib.SMTP("smtp.gmail.com")as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.email_password)
            connection.sendmail(from_addr="briannambari386@gmail.com",to_addrs="briannambari@gmail.com")

