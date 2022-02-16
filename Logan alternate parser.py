#Logan K. MacDonald
#TCMG-412, Project 3
#Texas A&M University
#Spring 2022


import re
# use os.path for file checking capability to check if log file has already been downloaded
from os.path import exists
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
counter = 0
recentcounter = 0
month = 0

print("Stand By")
#Count total requests in the log file from Oct 94 to Oct 95
for line in open(FILE_NAME):
    counter += 1

#Count recent requests, i.e the assigned months. This can be copied/pasted and renamed to expand or reduce the count.
#search paramaters must include the month and year because log file contains Oct 94 and Oct 95.
for line in open(FILE_NAME):
    search = re.search("Oct/1995",line)
    if search:
        recentcounter+=1

for line in open(FILE_NAME):        
    search = re.search("Sep/1995",line)
    if search:
        recentcounter+=1   

for line in open(FILE_NAME):         
    search = re.search("Aug/1995",line)
    if search:
        recentcounter+=1

for line in open(FILE_NAME):        
    search = re.search("Jul/1995",line)
    if search:
        recentcounter+=1

for line in open(FILE_NAME):        
    search = re.search("Jun/1995",line)
    if search:
        recentcounter+=1

for line in open(FILE_NAME):        
    search = re.search("May/1995",line)
    if search:
        recentcounter+=1
        
#Print message
print("There were",counter, "requests in total. ", recentcounter, "of them were in the last 6 months.")