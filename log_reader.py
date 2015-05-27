# coding=utf-8
__author__ = 'Michael Nickey'

"""
REQUEST:
On a Host that is connected to a LAN, you have a log-file that contains a list of users who have
logged onto some of the machines on the network,
in the past 24 hrs. Write a script that searches for computers on the network that are currently online,
and then sends a text-file to appropriate users on the online computers.
At the end of the run, the script should mark in the log file, computers to which the file has been transmitted.
In the log file, it should also add computers that have been discovered in the current traversal,
which were not listed originally.

Please specify any assumptions you make and explain how you’d test your code.

Assumptions:
The log file is in csv form.
The log file contains
	a date/time stamp
	username
	user-email address
	computer-id
	online status (online vs offline)
	script will be in the same directory as the logfile or the logfile will be copied to the same directory
"""

# Imports
import csv
import datetime
import logging

# SET GLOBAL VARIABLES
# This is the time delta. To change this time, change the number to the days that you want to search the log for.
DAY = datetime.timedelta(days=4)
# Format of the dates that are being compared
FORMAT = "%Y-%m-%d"
# Create a date variable for the current date
TODAY = datetime.date.today()

# Set the log output file, and the log level
logging.basicConfig(filename="output.txt", level=logging.DEBUG)
#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    :param file_obj: This is the logfile that is to be read. The log file needs to be in CSV format
    :return: info from the CSV log file of those users that have a time delta greater than what is set in DAY.
    In this example the time delta is set to 4 days.
    """
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
        line["Date"] = datetime.date(*(int(x) for x in line["Date"].split("-")))
        if (TODAY - (line["Date"] )) < DAY:
            # Log the computers that have been accessed within the last day
            logging.info("{} -- User: {} at {} accessed {}".format(TODAY, line["Username"], line["User Email"], line["Computer ID"]))
            print line["Username"], line["User Email"]
            send_the_Mail(line["User Email"])

def send_the_Mail(recipient):
    """
    This function takes in recipient and will send the email to that email address with an attachment.
    :param recipient: the email of the person to get the text file attachment
    """

    # Import the needed email libraries
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from smtplib import SMTP

    # Set the server and the message details
    send_from = 'mnickey@gmail.com'
    send_to = recipient
    subject = "Computer Access text file"

    # Create the multipart
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to

    # msg preable for those that do not have a email reader
    msg.preamble = 'Multipart message.\n'

    # Text part of the message
    part = MIMEText("This is an automated message. No need to reply... it won't be answered anyway :) ")
    msg.attach(part)

    # The attachment part of the message
    part = MIMEApplication(open("output.txt", "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename="output.txt")
    msg.attach(part)

    # Create an instance of a SMTP server
    smtp = SMTP(host='smtp.gmail.com', port='587')

    # Start the server
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mnickey@gmail.com', 'ifrfqsuzrqssdzzn')

    # Send the email
    smtp.sendmail(msg['From'], msg['To'], msg.as_string() )
    smtp.quit()

if __name__ == "__main__":
    with open("ComputerLog.csv",) as f_obj:
        csv_dict_reader(f_obj)
