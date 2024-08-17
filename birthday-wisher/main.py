import pandas
import datetime
import random
import smtplib

LETTERS = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
MY_EMAIL = "solomiiayakymets@gmail.com"
MY_PASSWORD = "<PASSWORD>"
PLACEHOLDER = '[NAME]'
NOW = datetime.datetime.now()
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict("records")

for person in data_dict:
    if NOW.month == person["month"] and NOW.day == person["day"]:
        random_letter = random.choice(LETTERS)
        with open(random_letter) as file:
            letter = file.read()
            letter = letter.replace(PLACEHOLDER, person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Birthday Congratulations\n\n{letter}"
            )
