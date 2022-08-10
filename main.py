"""
Automation tool to send a motivational email to yourself on Mondays
  NOTE:
  if the code fails to run,
  GMAIL:
  go to security settings and turn off 2 step verification and use phone to sign in
  In the same tab, turn ON access by less secure apps
  YAHOO:
  Go to security and generate an app access password to use in the code
  """
import smtplib
import random
import datetime as dt

my_email = "useremail@gmail.com"
my_password = "abcdefu"
curr_dt = dt.datetime.now()
day_of_week = curr_dt.weekday()

# send weekly email on Monday
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # secure connection and log in
        connection.starttls()
        connection.login(my_email, my_password)

        # getting a birthday quote
        with open("quotes.txt") as quotes:
            lines = quotes.readlines()
            lines = [line.rstrip() for line in lines]
        quote_msg = random.choice(lines)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject: Monday Motivation!! \n\n f{quote_msg}")
