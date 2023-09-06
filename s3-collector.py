import requests
from colorama import Fore
import threading
import argparse

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
            ".s3.us-west-3.amazonaws.com",
            ".s3-fips.us-east-2.amazonaws.com",
            ".s3.dualstack.us-east-2.amazonaws.com",
            ".s3-fips.dualstack.us-east-2.amazonaws.com",
            ".s3-website-eu-west-1.amazonaws.com",

            "s3-accesspoint-fips.ca-central-1.amazonaws.com",
            "s3-accesspoint-fips.dualstack.ca-central-1.amazonaws.com",
            "s3-accesspoint-fips.dualstack.us-east-1.amazonaws.com", 
            "s3-accesspoint-fips.dualstack.us-east-2.amazonaws.com", 
            "s3-accesspoint-fips.dualstack.us-gov-east-1.amazonaws.com", 
            "s3-accesspoint-fips.dualstack.us-gov-west-1.amazonaws.com",   
            "s3-accesspoint-fips.dualstack.us-west-1.amazonaws.com",   
            "s3-accesspoint-fips.dualstack.us-west-2.amazonaws.com",  
            "s3-accesspoint-fips.us-east-1.amazonaws.com",  
            "s3-accesspoint-fips.us-east-2.amazonaws.com",   
            "s3-accesspoint-fips.us-gov-east-1.amazonaws.com",  
            "s3-accesspoint-fips.us-gov-west-1.amazonaws.com",  
            "s3-accesspoint-fips.us-west-1.amazonaws.com", 
            "s3-accesspoint-fips.us-west-2.amazonaws.com",  
            "s3-accesspoint.af-south-1.amazonaws.com",   
            "s3-accesspoint.ap-east-1.amazonaws.com",   
            "s3-accesspoint.ap-northeast-1.amazonaws.com",   
            "s3-accesspoint.ap-northeast-2.amazonaws.com",   
            "s3-accesspoint.ap-northeast-3.amazonaws.com",   
            "s3-accesspoint.ap-south-1.amazonaws.com",  
            "s3-accesspoint.ap-south-2.amazonaws.com",  
            "s3-accesspoint.ap-southeast-1.amazonaws.com",    
            "s3-accesspoint.ap-southeast-2.amazonaws.com",  
            "s3-accesspoint.ap-southeast-3.amazonaws.com",   
            "s3-accesspoint.ap-southeast-4.amazonaws.com",   
            "s3-accesspoint.ca-central-1.amazonaws.com",   
            "s3-accesspoint.cn-north-1.amazonaws.com",   
            "s3-accesspoint.cn-northwest-1.amazonaws.com",   
            "s3-accesspoint.dualstack.af-south-1.amazonaws.com",  
            "s3-accesspoint.dualstack.ap-east-1.amazonaws.com",  
            "s3-accesspoint.dualstack.ap-northeast-1.amazonaws.com", 
            "s3-accesspoint.dualstack.ap-northeast-2.amazonaws.com",   
            "s3-accesspoint.dualstack.ap-northeast-3.amazonaws.com",   
            "s3-accesspoint.dualstack.ap-south-1.amazonaws.com",    
            "s3-accesspoint.dualstack.ap-south-2.amazonaws.com",   
            "s3-accesspoint.dualstack.ap-southeast-2.amazonaws.com",  
            "s3-accesspoint.dualstack.ap-southeast-3.amazonaws.com",  
            "s3-accesspoint.dualstack.ap-southeast-4.amazonaws.com",  
            "s3-accesspoint.dualstack.ca-central-1.amazonaws.com",   
            "s3-accesspoint.dualstack.cn-north-1.amazonaws.com",  
            "s3-accesspoint.dualstack.cn-northwest-1.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-central-1.amazonaws.com",   
            "s3-accesspoint.dualstack.eu-central-2.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-north-1.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-south-1.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-south-2.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-west-1.amazonaws.com",   
            "s3-accesspoint.dualstack.eu-west-2.amazonaws.com",  
            "s3-accesspoint.dualstack.eu-west-3.amazonaws.com",  
            "s3-accesspoint.dualstack.il-central-1.amazonaws.com", 
            "s3-accesspoint.dualstack.me-central-1.amazonaws.com",   
            "s3-accesspoint.dualstack.me-south-1.amazonaws.com",   
            "s3-accesspoint.dualstack.sa-east-1.amazonaws.com",  
            "s3-accesspoint.dualstack.us-east-1.amazonaws.com",  
            "s3-accesspoint.dualstack.us-east-2.amazonaws.com",  
            "s3-accesspoint.dualstack.us-gov-east-1.amazonaws.com",   
            "s3-accesspoint.dualstack.us-gov-west-1.amazonaws.com",   
            "s3-accesspoint.dualstack.us-west-1.amazonaws.com",
            "s3-accesspoint.dualstack.us-west-2.amazonaws.com",   
            "s3-accesspoint.eu-central-1.amazonaws.com",  
            "s3-accesspoint.eu-central-2.amazonaws.com",   
            "s3-accesspoint.eu-north-1.amazonaws.com",  
            "s3-accesspoint.eu-south-1.amazonaws.com",  
            "s3-accesspoint.eu-south-2.amazonaws.com",  
            "s3-accesspoint.eu-west-1.amazonaws.com",   
            "s3-accesspoint.eu-west-2.amazonaws.com",   
            "s3-accesspoint.eu-west-3.amazonaws.com",  
            "s3-accesspoint.il-central-1.amazonaws.com",  
            "s3-accesspoint.me-central-1.amazonaws.com",  
            "s3-accesspoint.me-south-1.amazonaws.com",  
            "s3-accesspoint.sa-east-1.amazonaws.com",  
            "s3-accesspoint.us-east-1.amazonaws.com", 
            "s3-accesspoint.us-east-2.amazonaws.com",  
            "s3-accesspoint.us-gov-east-1.amazonaws.com", 
            "s3-accesspoint.us-gov-west-1.amazonaws.com",  
            "s3-accesspoint.us-west-1.amazonaws.com",  
            "s3-accesspoint.us-west-2.amazonaws.com",  
            "s3-fips.ca-central-1.amazonaws.com",
            "s3-fips.dualstack.ca-central-1.amazonaws.com", 
            "s3-fips.dualstack.us-east-1.amazonaws.com", 
            "s3-fips.dualstack.us-east-2.amazonaws.com",   
            "s3-fips.dualstack.us-gov-east-1.amazonaws.com",  
            "s3-fips.dualstack.us-gov-west-1.amazonaws.com",  
            "s3-fips.dualstack.us-west-1.amazonaws.com",
            "s3-fips.dualstack.us-west-2.amazonaws.com",
            "s3-fips.us-east-1.amazonaws.com",  
            "s3-fips.us-east-2.amazonaws.com",  
            "s3-fips.us-gov-east-1.amazonaws.com", 
            "s3-fips.us-gov-west-1.amazonaws.com",
            "s3-fips.us-west-1.amazonaws.com",   
            "s3-fips.us-west-2.amazonaws.com",  
            "s3.af-south-1.amazonaws.com",  
            "s3.ap-east-1.amazonaws.com",  
            "s3.ap-northeast-1.amazonaws.com", 
            "s3.ap-northeast-2.amazonaws.com", 
            "s3.ap-northeast-3.amazonaws.com", 
            "s3.ap-south-1.amazonaws.com", 
            "s3.ap-south-2.amazonaws.com",   
            "s3.ap-southeast-1.amazonaws.com", 
            "s3.ap-southeast-2.amazonaws.com", 
            "s3.ap-southeast-3.amazonaws.com", 
            "s3.ap-southeast-4.amazonaws.com", 
            "s3.ca-central-1.amazonaws.com",  
            "s3.dualstack.af-south-1.amazonaws.com",  
            "s3.dualstack.ap-east-1.amazonaws.com",  
            "s3.dualstack.ap-northeast-1.amazonaws.com", 
            "s3.dualstack.ap-northeast-2.amazonaws.com",   
            "s3.dualstack.ap-northeast-3.amazonaws.com",  
            "s3.dualstack.ap-south-1.amazonaws.com", 
            "s3.dualstack.ap-south-2.amazonaws.com", 
            "s3.dualstack.ap-southeast-1.amazonaws.com", 
            "s3.dualstack.ap-southeast-2.amazonaws.com",  
            "s3.dualstack.ap-southeast-3.amazonaws.com",  
            "s3.dualstack.ap-southeast-4.amazonaws.com",  
            "s3.dualstack.ca-central-1.amazonaws.com",  
            "s3.dualstack.cn-north-1.amazonaws.com.cn",  
            "s3.dualstack.cn-northwest-1.amazonaws.com.cn", 
            "s3.dualstack.eu-central-1.amazonaws.com",  
            "s3.dualstack.eu-central-2.amazonaws.com",  
            "s3.dualstack.eu-north-1.amazonaws.com",  
            "s3.dualstack.eu-south-1.amazonaws.com",  
            "s3.dualstack.eu-south-2.amazonaws.com",  
            "s3.dualstack.eu-west-1.amazonaws.com",   
            "s3.dualstack.eu-west-2.amazonaws.com",  
            "s3.dualstack.eu-west-3.amazonaws.com",  
            "s3.dualstack.il-central-1.amazonaws.com",  
            "s3.dualstack.me-central-1.amazonaws.com",  
            "s3.dualstack.me-south-1.amazonaws.com", 
            "s3.dualstack.sa-east-1.amazonaws.com",  
            "s3.dualstack.us-east-1.amazonaws.com",
            "s3.dualstack.us-east-2.amazonaws.com",  
            "s3.dualstack.us-gov-east-1.amazonaws.com", 
            "s3.dualstack.us-gov-west-1.amazonaws.com",  
            "s3.dualstack.us-west-1.amazonaws.com",  
            "s3.dualstack.us-west-2.amazonaws.com",  
            "s3.eu-central-1.amazonaws.com",  
            "s3.eu-central-2.amazonaws.com",  
            "s3.eu-north-1.amazonaws.com",  
            "s3.eu-south-1.amazonaws.com", 
            "s3.eu-south-2.amazonaws.com",  
            "s3.eu-west-1.amazonaws.com",  
            "s3.eu-west-2.amazonaws.com", 
            "s3.eu-west-3.amazonaws.com",  
            "s3.il-central-1.amazonaws.com", 
            "s3.me-central-1.amazonaws.com",  
            "s3.me-south-1.amazonaws.com", 
            "s3.sa-east-1.amazonaws.com",  
            "s3.us-east-1.amazonaws.com", 
            "s3.us-east-2.amazonaws.com",  
            "s3.us-gov-east-1.amazonaws.com",  
            "s3.us-gov-west-1.amazonaws.com"
    }

parser = argparse.ArgumentParser(description="Enumerate S3 Buckets Names for Company")

parser.add_argument("-sf", "--subs-file", required=False, help="Subdomains File to enumerate")
parser.add_argument("-c", "--company", required=False, help="Company Name")
parser.add_argument("-bn", "--bucket-names", required=False, help="Buckets Name wordlist")
args = parser.parse_args()










# Subdomain And Region
def sub_N_regions(subdomains):
    for sub in subdomains:

        for region in cases:
            url = "https://" + sub + region
            try:

                response = requests.get(url)
                if "NoSuchBucket" in response.text:
                    print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
                else:
                    print(Fore.GREEN , "\nThis Bucket Found : {}".format(response.url))
            except:
                print(Fore.RED, "\nNot Exist Bucket : {}".format(url))



def sub_N_names_N_regions(subdomains , buckets):
    for sub in subdomains:

        for region in cases:

            for buck in buckets:
                url = "https://" + sub + buck + region
                try:

                    response = requests.get(url)
                    if "NoSuchBucket" in response.text:
                        print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
                    else:
                        print(Fore.GREEN , "\nThis Bucket Found : {}".format(response.url))
                except:
                    print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
                

def company_N_regions(company):
    for region in cases:
            url = "https://" + company + region
            try:
                response = requests.get(url)
                if "NoSuchBucket" in response.text:
                    print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
                else:
                    print(Fore.GREEN , "\nThis Bucket Found : {}".format(response.url))
            except:
                print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
        


def company_N_bucket_N_regions(company , buckets):
    for region in cases:
        for buck in buckets:
            url = "https://" + company + buck + region
            try:
                response = requests.get(url)
                if "NoSuchBucket" in response.text:
                    print(Fore.RED, "\nNot Exist Bucket : {}".format(url))
                else:
                    print(Fore.GREEN , "\nThis Bucket Found : {}".format(response.url))
            except:
                print(Fore.RED, "\nNot Exist Bucket : {}".format(url))

# ----------------------------------------------------------------------------



if args.subs_file == None and args.company == None and args.bucket_names == None:
    parser.print_help()


if args.company:
    print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")
    company = args.company
    company_N_regions(company)
    print("-"*50 +"\n Finished\n")

if args.subs_file:
    print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")
    subs = open(args.file,'r')
    subdomains = subs.read().splitlines()
    sub_N_regions(subdomains)
    print("-"*50 +"\n Finished\n")

if args.company and args.bucket_names:
    print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")
    company = args.company
    bucket = open(args.bucket_names,'r')
    buckets = bucket.read().splitlines()
    company_N_bucket_N_regions(company , buckets)
    print("-"*50 +"\n Finished\n")

if args.subs_file and args.bucket_names:
    print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")
    subs = open(args.file,'r')
    subdomains = subs.read().splitlines()
    bucket = open(args.bucket_names,'r')
    buckets = bucket.read().splitlines()
    sub_N_names_N_regions(subdomains , buckets)
    print("-"*50 +"\n Finished\n")


