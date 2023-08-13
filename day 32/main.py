import smtplib
import datetime as dt
import pandas as pd
import os
import random


def send_email(person, body):
    # Email Params
    my_email = "NOT_MY_EMAIL@gmail.com"
    pw = "NOT_MY_PASSWORD"

    # Send Email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="santschiy@gmail.com",
            msg=f"Subject:Happy Birthday {person}!\n\n{body}")


# Read all birthdays and check if one of them matches, if yes send_email
df = pd.read_csv("birthday-wisher-extrahard-start/birthdays.csv")

today = dt.datetime.now()
for index, row in df.iterrows():
    if today.day == row['day'] and today.month == row['month']:
        chosen_letter = random.choice(os.listdir("birthday-wisher-extrahard-start/letter_templates"))

        with open(f"birthday-wisher-extrahard-start/letter_templates/{chosen_letter}", "r") as letter:
            content = letter.read()
            content = content.replace("[NAME]", row['name'])
        send_email(row['name'], content)




