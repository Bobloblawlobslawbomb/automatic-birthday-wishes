import smtplib
from datetime import datetime
import random
import json


MY_EMAIL = "[YOUR_EMAIL]"
MY_PASSWORD = "[YOUR_EMAIL_PASSWORD]"
EMAIL_SMTP_PORT = "[YOUR_EMAIL_SMTP_PORT]"

A = "data/letter1.txt"
B = "data/letter2.txt"
letters_list = [A, B]

current_month = datetime.now().month
current_day = datetime.now().day

with open("data/birthdays.json") as file:
    data = json.load(file)

for key, value in data.items():
    if current_month in value.values() and current_day in value.values():
        birthday_person = value["name"]
        to_email = value["email"]
    letter = random.choice(letters_list)
    with open(letter) as file:
        letter = file.read()

email_body = letter.replace("[NAME]", birthday_person)

with smtplib.SMTP(EMAIL_SMTP_PORT) as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=to_email,
        msg=f"Subject:Happy Birthday\n\n{email_body}"
    )
