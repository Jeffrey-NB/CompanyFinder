import json
import requests
import sys

mac = sys.argv[1]   #sets parameter as command line input

# Function Name: Finder
# Purpose: Takes in command line parameter of MAC address and outputs corresponding company name
# Parameters: mac address(command line)
# Date Modified: 5/27/20 - initial build Jeffrey-NB

def finder(mac):

    url = ("https://api.macaddress.io/v1?apiKey=at_B7Gkr4HpshszzxM2rSHKNUtDEREpE&output=json&search=" + mac)
    
    try:
        r = requests.get(url, timeout = 25)
        r.raise_for_status()
    except requests.exceptions.HTTPError as httpError: 
        print ("Http Error:",httpError) 
    except requests.exceptions.ConnectionError as connectError: 
        print ("Connection Error:",connectError) 
    except requests.exceptions.Timeout as timeOutError: 
        print ("Timeout Error:",timeOutError) 
    except requests.exceptions.RequestException as reqError: 
        print ("Unknown Error:",reqError) 
        sys.exit(1)

    statusCode = r.status_code

    if statusCode != 200:
        print(statusCode)
        sys.exit(1)

    data = r.json()

    company = data['vendorDetails']['companyName']

    print('Company Name: ' + company)

finder(mac)


