# This code will downlod the log file
from urllib import request
import re
from collections import Counter
import csv


file_url = r'https://s3.amazonaws.com/tcmg476/http_access_log'

def download_file(url):
    #open file
    fileOpen = request.urlopen(url)
    # read file
    file_info = fileOpen.read()
    file_info_str = str(file_info)
    file_lines = file_info_str.split('\\n')

    #store data as new file
    new_file = open('pthree_proj.log', "w")

    for info in file_lines:
        new_file.write(info + '\n')

    new_file.close()
download_file(file_url)
# File should be downloaded

# Attempts to make a csv file of all log requests
def reader(new_file):
    with open(new_file) as f:
        pthree_proj = f.read()
        print(pthree_proj)
    #Date regular expression
        regexp = r"[0-9]{1,2}\d+\/[a-zA-Z]{1,3}\w+\/[0-9]{1,4}"

        date_list = re.findall(regexp, pthree_proj)
        return date_list

def count(date_list):
   counter = Counter(date_list)
   return counter
#New file
def write_csv(counter):
    with open("output.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Date", "Requests"]

        writer.writerow(header)

        for item in counter:
           writer.writerow( (item, counter[item]) )


if __name__ == '__main__':
    write_csv(count(reader("pthree_proj")))
