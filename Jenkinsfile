  pipeline {
    agent any
    stages {
        stage('Building Pilot App') {
            steps {
                sh 'exit 0'
            }
        }
        stage('Threat Model Validation') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                //    sh "exit 1"
               
                sh '''#!/bin/bash -l
response2=$(curl --location --request POST 'https://deloitte-poc.threatmodeler.net/token' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'username=nikhsehgal@deloitte.com' --data-urlencode 'password=Containers@765' --data-urlencode 'grant_type=password')
echo $response2
token=`echo $response2 | cut -d '"' -f 4`
echo $token
validate=$(curl --location --request POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{"JenkinsJobName":"$JOB_NAME","ValidateWithThreatRisk":false}')
echo $validate
'''
                }
            }
        }
        stage('Push') {
            steps {
                sh 'exit 0'
            }
        }
    }
}
