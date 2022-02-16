#Andrew Dean
#TCMG 412 500 UIN - 230007137
#Program Title: Log Parser

#Functions
from urllib.request import urlretrieve
#from datetime import datetime
#import re



##Main Program
URL_PATH= 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_log= 'log_copy.log'

print('Fetching Apache log file')
# I liked this progress bar implementation, thanks for sharing!
local_log, headers= urlretrieve(URL_PATH, local_log, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
print('Done!')
print()

sesame = open("log_copy.log", "r")
##trying regex
#line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
#regex = '(.*?) - - \[.*?\] \"(.*?)\" (\d{3}) (.+)'
#regex = '(.*?) - - \[((\d{2})/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/(\d{4}))\] \"(.*?)\" (\d{3}) (.+)'

#for lines in sesame.readline():
#    if lines:
#        regex = re.search
## I deleted a lot of stuff in frustration trying to actually parse the files into useful tokens
## and convert datetime

##going off of reed's format
sixmonths= 0
count= 0

        
for line in sesame:
    logLineInfo = line.split()
    
    if(len(logLineInfo) < 4):
        continue
    else:
        date = logLineInfo[3].split('/')
        #this is only counting the number of entries on the 11th day of each of the months
        #not sure how to fix without abandoning the format!
        if((date[0][1:] == '11')
           and (date[1] == 'Apr' or 'May' or 'Jun' or 'Jul' or 'Aug' or 'Sep' or 'Oct') 
           and (date[2][:4] == '1995')):
            sixmonths += 1
sesame.close()
            
counter = open("log_copy.log", "r")
content = counter.read()
numlines = content.split('\n')
for i in numlines:
    if i:
        count+=1
counter.close()
#I'm not sure the total numbers are accurate
print()       
print("Total Requests Made 6 months starting April 11th, 1994 - Octobober 11th 1995: ", sixmonths)
print("Total Requests from the logfile: ", count)


