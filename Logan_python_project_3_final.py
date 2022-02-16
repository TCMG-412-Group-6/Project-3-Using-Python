#Logan K. MacDonald
#TCMG-412, Project 3
#Texas A&M University
#Spring 2022

from ast import Str
import re
# use os.path for file checking capability to check if log file has already been downloaded
from os.path import exists
import string
from tokenize import String
# use urlretrieve to retrieve log file after file check determined log had not already been downloaded
from urllib.request import urlretrieve

FILE_NAME = 'http_access_log.txt'

# check for log file prescence on system, if found use that file, if not retrieve from web
if not exists(FILE_NAME):
    print("Log file not found on system. Log file is being retrieved, please wait.")
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'http_access_log.txt'
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    print("Done")

fh = open(FILE_NAME)

print("Stand By")

#start line counter, and for loop to count total number of lines in log
line_count = 0
for line in fh:
    if line != "\n":
        line_count += 1
fh.close()

#data count for each instance of the phrase for each month
fh = open(FILE_NAME)
data = fh.read()
Oct_1995 = data.count("Oct/1995")

fh = open(FILE_NAME)
data = fh.read()
Sep_1995 = data.count("Sep/1995")

fh = open(FILE_NAME)
data = fh.read()
Aug_1995 = data.count("Aug/1995")

fh = open(FILE_NAME)
data = fh.read()
Jul_1995 = data.count("Jul/1995")

fh = open(FILE_NAME)
data = fh.read()
Jun_1995 = data.count("Jun/1995")

fh = open(FILE_NAME)
data = fh.read()
May_1995 = data.count("May/1995")
#simple addition to get the total number of requests in the log file for the requested months.
monthly_total_log_entry = Oct_1995+Sep_1995+Aug_1995+Jul_1995+Jun_1995+May_1995
#last_6_months = occurrences1 + occurrences2
#print('The total number of requests during the last 6 months of this log file are:', monthly_total_log_entry)
#print('The total number of requests contained within this log are:', line_count)
print('The total number of requests to the website were,', line_count, 'and the number of request made in the last six monthe were,', monthly_total_log_entry, ",Thanks and Gig'Em")