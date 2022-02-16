#Britany Cano
#url file request
from urllib.request import urlretrieve
#recevies url link
url_path="https://s3.amazonaws.com/tcmg476/http_access_log"
log_file='log_copy.log'

log_file, headers= urlretrieve(url_path, log_file, lambda x,y,z: print('.', end='',flush=True) if x % 100 == 0 else False)

f = open('log_file','r')

for line in f:
    print line.split('')
f.close()
