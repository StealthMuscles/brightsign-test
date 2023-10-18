import argparse
import os
import sys

import requests

API_KEY = os.getenv('API_KEY')
API_URL = 'http://api.ipstack.com'

parser = argparse.ArgumentParser(
                    prog='locateip',
                    description='Returns the latitude and longitude for an ip address according to ipstack.com')
parser.add_argument('ip_address')
args = parser.parse_args()
r = requests.get(API_URL + "/" + args.ip_address, params={'access_key': API_KEY})

# All error info prints to stderr (including python/requests exceptions), success prints 'lat long' as values to stdout
r.raise_for_status()
json = r.json()
if 'error' in json:
    print(json, file=sys.stderr)
    sys.exit(1)

print(json['latitude'], json['longitude'], file=sys.stdout)
