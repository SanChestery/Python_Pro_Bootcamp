import smtplib
import datetime as dt
import random

my_email = "chesterysan@gmail.com"
pw = "jeebyxqakhkleznv"
with open("Birthday Wisher (Day 32) start/quotes.txt", "r") as file:
    lines = [line.rstrip() for line in file]

content = random.choice(lines)

today = dt.datetime.now().weekday()
if today == 6:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="santschiy@gmail.com",
            msg=f"Subject:An inspirational quote\n\n{content}")

print(today)

