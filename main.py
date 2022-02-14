##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import os

import pandas as pd

MY_EMAIL = "jerryomwaka@gmail.com"
MY_PASSWORD = "3rillianT.me"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
birth_day = today.day
birth_month = today.month

# read csv file. Pick the birthday
birthday_file = pd.read_csv("birthdays.csv")
birthday_date = birthday_file.to_dict()
birthday_month = birthday_date['month'][1]
birthday_day = birthday_date['day'][1]
birthday_person = birthday_date['name'][1]

if birth_day == birthday_day and birth_month == birthday_month:
    # create the birthday wish
    random_file = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{random_file}", "r+") as new_file:
        data = new_file.readlines()
        data[0] = f"Dear {birthday_person}"
        new_data = "".join(data)
        print(new_data)

    # send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="nzioker@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{new_data}")






# 4. Send the letter generated in step 3 to that person's email address.




