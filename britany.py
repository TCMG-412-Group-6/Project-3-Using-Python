#Britany Cano
#url file request
from urllib.request import urlretrieve
#recevies url link
url_path="https://s3.amazonaws.com/tcmg476/http_access_log"
log_file='log_copy.log'

log_file, headers= urlretrieve(url_path, log_file, lambda x,y,z: print('.', end='',flush=True) if x % 100 == 0 else False)
#opens log and reads content
f = open('log_copy.log','r')

content = f.read()
content_list = content.splitlines()
f.close()

#cristian code (trouble in my code)
months = ["May", "Jun", "Jul", "Aug", "Sep", "Oct"]
m_requests = []
for m in months:
  requests = content.count(f'{m}/1995')
  m_requests.append(requests)
total_requests = sum(m_requests)
print("Number of requests made in the last 6 months:", total_requests)

number_of_logs = len(content_list)

print("requests in the period:", number_of_logs)
f.close()
