import requests
import sys
from colorama import Fore
import threading

if len(sys.argv) == 1 or len(sys.argv) == 2:
    print("Usage : "+sys.argv[0]+" subdomains.txt bucket_names.txt")
else:

    subs = open(sys.argv[1],'r')

    subdomains = subs.read().splitlines()


    bucket = open(sys.argv[2],'r')


    buckets = bucket.read().splitlines()

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

    print(Fore.GREEN, "\n[+] Start Enumerate Buckets \n")

    def sub_N_regions():
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
                

    def sub_N_names_N_regions():
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
                



    thread1 = threading.Thread(target=sub_N_regions)
    thread2 = threading.Thread(target=sub_N_names_N_regions)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("-"*50 +"\n Finished\n")
