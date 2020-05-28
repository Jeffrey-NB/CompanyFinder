import json
import requests
import sys

import argparse

p = argparse.ArgumentParser(description='Company from MAC Address')
p.add_argument("-mac", type=str, required=True)
args = p.parse_args()

mac = args.mac #convert from namespace to string


# Function Name: Finder
# Purpose: Takes in command line parameter of MAC address and outputs corresponding company name
# Parameters: mac address(command line)
# Date Modified: 5/27/20 - initial build Jeffrey-NB

def finder(mac):

    url = ("https://api.macaddress.io/v1?apiKey=at_B7Gkr4HpshszzxM2rSHKNUtDEREpE&output=json&search=" + mac)    #hardcoded my own api key for ease of access but normally would require individual key


    
    try:
        r = requests.get(url, timeout = 10) #api call and response creation

        r.raise_for_status()

    except requests.exceptions.HTTPError as httpError:  #raises error if request returned unsuccessful status code
        print ("Http Error:", httpError) 

    except requests.exceptions.ConnectionError as connectError:  #raises error if there is connection issue
        print ("Connection Error:", connectError) 
        sys.exit(1)

    except requests.exceptions.Timeout as timeOutError:  #raises error if connection takes longer than 10s
        print ("Timeout Error:", timeOutError) 

    except requests.exceptions.RequestException as reqError:  #raises for all other errors
        print ("Unknown Error:", reqError) 
        sys.exit(1)

    statusCode = r.status_code

    if statusCode != 200:                       #prints out status code if not 200(all good status)
        print('Status Code: ', statusCode)
        sys.exit(1)

    try:

        data = r.json()

        company = data['vendorDetails']['companyName']

        print('Company Name: ' + company)

    except ValueError:
        print('Invalid Data Received')

    except Exception as e:
        print('Error Occured: \n' + str(e))


finder(mac)


