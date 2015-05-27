# emails-with-attachments
A quick way to send emails with python that will read from a log file, process the data and then email the recipients a file.

#####Configuration instructions
Install python 2.7 and required packages  
I recommend that you use a virtual environment to keep the system clean but this is up to you.  

#####Operating instructions
After cloning this script, launch your temrinal window where the script lives.  
Type in `python log_reader.py`.  This will run the main program.

#####File manifest
log_reader.py: This is the main script that does the work. The script will check for users in the CSV file and find those that are either `online` or those computers whose last login was within the `DAY` timedelta set.  

ComputerLog.csv: This is a csv file that contains the raw data. This is used by `log_reader.py` and is parsed to find computers that match the corresponding criteria.  

output.txt: This file is created by `log_reader.py`. When a computer is found to match the criteria, we log that information in this log.  

#####Contact information  
For any questions or comments, please email [me here](mailto:mnickey@gmail.com).