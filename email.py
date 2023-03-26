from email.mime.text import MIMEText
from data_configuration import message
import smtplib
import pyodbc
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

host_email = os.getenv('EMAIL')
host_password = os.getenv('PASSWORD')
driver = os.getenv('DRIVER')
server = os.getenv('SERVER')
database = os.getenv('DATABASE')

# connect to the database
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

# retrieve the email address from the database
cursor = cnxn.cursor()
cursor.execute('SELECT DISTINCT email_address FROM emails')
emails = [row[0] for row in cursor.fetchall()]

# set the time you want the script to run
run_time = datetime.time(hour=18, minute=21, second=0)

while True:
    # calculate the number of seconds until the scheduled time
    today = datetime.datetime.today()
    scheduled_time = datetime.datetime.combine(today, run_time)

    if scheduled_time < today:
        scheduled_time += datetime.timedelta(days=1)

    time_to_wait = (scheduled_time - today).seconds
    # wait until the scheduled time
    time.sleep(time_to_wait)

    # create the email message
    for email in emails:
        msg = MIMEText(message)
        msg['Subject'] = 'NBA Newsletter'
        msg['From'] = host_email
        msg['To'] = email
        # connect to the SMTP server
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login(host_email, host_password)
        smtp_obj.ehlo()  # Add this line to initialize the SMTP session
        print(email)
        smtp_obj.sendmail(host_email,
                          email, msg.as_string())
        # close the smtp connection
        smtp_obj.quit()
