 #beggining of code 
#imports log file
import requests
#gets the url link
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)
#saves the content with name
open('tcmg412.log', 'wb').write(r.content)
#Splits the file into a list 
f = open("tcmg412.log", "r")
#read file contents
content = f.read()
content_list = content.splitlines()
f.close()

#how many total request were made in the last 6 months
months = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]
m_requests = []
for m in months:
  requests = content.count(f'{m}/1995')
  m_requests.append(requests)
total_requests = sum(m_requests)
print("Number of requests made in the last 6 months:", total_requests)
#prints the logs in the content list 
#len function gets the number of elements in the list
number_of_logs = len(content_list)
#prints number of requests in the time period represented in the log 
print("Total requests in the period:", number_of_logs)
f.close()