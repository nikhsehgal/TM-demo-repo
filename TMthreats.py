import requests
import json
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username", type=str)
parser.add_argument("password", help="Password", type=str)
parser.add_argument("projectId", help="Project ID", type=str)

args = parser.parse_args()

print("Username: "+ args.username)
print("Password: " + args.password)

TMAuthenticationURL='https://deloitte-poc.threatmodeler.net/token'
TMThreatsURL = "https://deloitte-poc.threatmodeler.net/api/project/"+ args.projectId +"/threats/true"
username=args.username
password=args.password

#API call for Authentication to TM
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

body = {
    'username': username,
    'password': password,
    'grant_type': "password"
}

response = requests.post(TMAuthenticationURL, data=body, headers=headers)
if response.status_code==400:
    print("Authentication Failed")

response_json = json.loads(response.text.encode('utf8'))
access_token=response_json["access_token"]


headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.get(TMThreatsURL, json=body, headers=headers)
response_json = json.loads(response.text.encode('utf8'))
if len(response_json["Data"])>0:
    print("Threats Detected in ThreatModeler")
else:
    print("No Threats Detected in ThreatModeler")

#if response_json["Data"] != None:
 #   print("Threats Detected in ThreatModeler")
#else:
 #   print("No Threats Detected in ThreatModeler")
