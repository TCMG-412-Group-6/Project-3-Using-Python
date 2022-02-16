import re
# use os.path for file checking capability to check if log file has already been downloaded
from os.path import exists
# use urlretrieve to retrieve log file after file check determined log had not already been downloaded
from urllib.request import urlretrieve

FILE_NAME = 'http_access_log.txt'

# check for log file prescence on system, if found use that file, if not retrieve from web
if not exists(FILE_NAME):
    print("\nLog file not found on system. Log file is being retrieved, please wait.")
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'http_access_log.txt'
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    print("Done")


# "file", "q1", "q2" are variables that will be executed for the overall outcome
fh = open(FILE_NAME)
q1 = 0
q2 = 0

# The for loop will be iterating over the list of logs from the file and determining the number of logs documented
for line in open(FILE_NAME):
	if '/199' in line:
		q2 += 1
		
	if '/1995' in open(FILE_NAME):
		q1 += 1
			
# These print statements will give the outputs that were documented in the certain time periods
print ("The number of transactions documented in 1995 is", q1)
print ("The total number of transactions documented for this period is", q2)