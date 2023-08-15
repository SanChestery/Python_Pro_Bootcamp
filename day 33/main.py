import time
import requests
import smtplib
import datetime

# Global Vars
MY_LONG = 1.000000
MY_LAT = 1.000000
MY_POSITION = (MY_LONG, MY_LAT)
MY_EMAIL = "NOT_MY_EMAIL@gmail.com"
MY_PW = "NOT_MY_PASSWORD"


def get_iss():
    # Get current ISS data
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

    data_iss = response_iss.json()

    longitude_iss = float(data_iss["iss_position"]["longitude"])
    latitude_iss = float(data_iss["iss_position"]["latitude"])

    iss_position = (longitude_iss, latitude_iss)

    print(f"My position: {MY_POSITION}")
    print(f"ISS position: {iss_position}")

    if (latitude_iss + 5 > MY_LAT > latitude_iss - 5) and (longitude_iss + 5 > MY_LONG > longitude_iss - 5):
        return True


def get_sun():
    # Get current own data and information on sunrise/sunset
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

    # Get current time
    curr_time = datetime.datetime.now().hour
    print(f"Current time: {curr_time}")
    if sunrise > curr_time or curr_time > sunset:
        return True


while True:
    time.sleep(60)
    # Conditional statement
    if get_sun() and get_iss():

        print("Passed Condition")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:The ISS is above you\n\nThe ISS is above you! Crazy!"
            )