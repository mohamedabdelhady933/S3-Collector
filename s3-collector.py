import requests
import sys
from colorama import Fore


file = open(sys.argv[1],'r')

buckets = file.read().splitlines()


cases = {
        ".s3.amazonaws.com",
        ".s3.us-east-1.amazonaws.com",
        ".s3.us-east-2.amazonaws.com",
        ".s3.us-east-3.amazonaws.com",
        ".s3.eu-west-1.amazonaws.com",
        ".s3.eu-west-2.amazonaws.com",
        ".s3.eu-west-3.amazonaws.com",
        ".s3.us-west-1.amazonaws.com",
        ".s3.us-west-2.amazonaws.com",
        ".s3.us-west-3.amazonaws.com"
}

print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")

for i in buckets:


    for x in cases:
        url = "https://" + i + x
        try:

            response = requests.get(url)
            print(Fore.GREEN , "\nThis Bucket Found : {}".format(response.url))
        except:
            print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
