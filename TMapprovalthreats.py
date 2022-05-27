import requests
import json
import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username", type=str)
parser.add_argument("password", help="Password", type=str)
parser.add_argument("jenkinsJobName", help="Jenkins Job Name", type=str)
parser.add_argument("projectId", help="Project ID", type=str)
parser.add_argument("validateThreats", help="Validate Threats", type=str)

args = parser.parse_args()

#Environment Variables
TMAuthenticationURL='https://deloitte-poc.threatmodeler.net/token'
TMJenkinsValidationURL = 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate'
TMThreatsURL = https://deloitte-poc.threatmodeler.net/api/project/+ args.projectId +"/threats/true"
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

if response.status_code==400:
    print("Authentication Failed")
    
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

if response_json["IsSuccess"]=="true":
    print("ThreatModeler Approval Validation Successful.")
else:
    print(response_json["Message"])
    
if args.validateThreats=="true":
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
