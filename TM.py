import requests
import json
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username", type=str)
parser.add_argument("password", help="Password", type=str)
parser.add_argument("jenkinsJobName", help="Jenkins Job Name", type=str)

args = parser.parse_args()

#Environment Variables
TMAuthenticationURL='https://deloitte-poc.threatmodeler.net/token'
TMJenkinsValidationURL = 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate'
username=args.username
password=args.password
jenkinsJobName=args.jenkinsJobName


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
response_json = json.loads(response.text.encode('utf8'))
access_token=response_json["access_token"]


#API call to get validation from TM
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

body = {
    'JenkinsJobName': jenkinsJobName,
    'ValidateWithThreatRisk': "false"
}

response = requests.post(TMJenkinsValidationURL, json=body, headers=headers)
response_json = json.loads(response.text.encode('utf8'))

if response_json["IsSuccess"]==True:
    print("ThreatModeler Approval Validation Successful.")
else:
    print(response_json["Message"])
