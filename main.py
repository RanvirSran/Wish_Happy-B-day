##################### Extra Hard Starting Project ######################

import random
import smtplib
import datetime as dt
import pandas

USER = "email@xyz.com"
PASSWORD = "your_pass"

today = dt.datetime.today().date()

with open("birthdays.csv") as file:
    data_object = pandas.read_csv(file)

    day = data_object.day.to_list()
    month = data_object.month.to_list()
    year = data_object.year.to_list()
    emails = data_object.email.to_list()
    names = data_object.name.to_list()

    for i in range(len(day)):
        dob = dt.date(day=day[i], month=month[i], year=year[i])

        if dob.day == today.day and dob.month == today.month:

            with open(f"letter_templates/letter_{random.choice([1, 2, 3])}.txt") as letter:
                template = letter.read()
                prepped_letter = template.replace("[NAME]", names[i])

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=USER, password=PASSWORD)
                connection.sendmail(from_addr=USER, to_addrs=emails[i],
                                    msg=f"Subject: Happy Birthday!\n\n{prepped_letter}")
