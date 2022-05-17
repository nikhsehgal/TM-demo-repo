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
//token=`echo -n $response2 | cut -d '"' -f 4`
token=`echo -n $(echo $response2 | cut -d '"' -f 4)`
echo $token
//validate=$(curl --location --request POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{"JenkinsJobName":"${JOB_NAME}","ValidateWithThreatRisk":false}')

curl --location --request POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' \
--header 'Authorization: Bearer j8RvVYxP5NTzvGULmRPWslopLTril7N58Wfor9GWVdH9iZcuVZCD8babAzTjCFOH9EVEs5sSdxC9OvuZV4yrjGbPNbt1VH6yribE9vf8Uq1YdekmV1-HCyKbqxZhe08oclt_SVsGrqUxcHp-63vu5NuetM30NlBZ1nXC7SGU0fovgbZR3y0q5_42LGjbccuCEPK09Je7MC9MEmVl2RAzZ2Hti1Vn3kSYRV6hMVuMXQ5u4CSZnOw3dzLgZGacRpxde40yASLNokSfUx1gpxgOji83CgP4vLGsi4rbEDqBPCcNKRKc2xn8yVrCw15DjTl0yBy0jB46YHQZi_xlNursK5xUG9kHLuCPV8FyGOGN4CzeXPT0bHz-AeVcJ8cPrbP0rAimEE3JPB37xP7Yrupbsm0TK5DS2Z_go2boJJQ_F2cc__1l-epglRHu0uj6FMdOiW_JakjjJsOwX9_dBpGQ-vbb0OWSvGInyGNy746bg4FuP5IvWgC1ilmVAEkagwG-AESTjCi7OU7GGw45OxhXp5CV-73xP_0A6JGFPqQ3ue9_rPgccTCLERehvqdxtqycbjrEscTwLNfE5NJyXPOSiFDDTicSwQgWAzCajT0OOqAok3O2smmBWbrUrq-n6ToUPD1FZLpww7iASI9iIhFz7lz5aTYNqMv9TbrfpSzNytQQFRCEvmyACCIiu728smTrE5pXmrWJHfnq1Wcq4gIkRHKqLLhF1NJgrJFftwXP42JzxXKxzOgHjpjU_9rCxxAGNB61VZ9O_gnlWkKIpZsMoeTXk7f2aqeXEmUXd6cdFcFEgLXp5XCWKiH6aDfOBNH5Rr9KBFbWWWaUwH4j-CjpjprWl3tRLQS3Wzik6gd5M0gAmvv5VQn1LZsqsTfyNCvcAqBU5HY0NltFQvRqJ8e6DVcriGVIQ1m9d5HvcG72_RKLrcJFZxWKrijipRAu90UA6GuWt49xXlPwNBVlCTAnh5sKaTk-QBCpSQZ-benSR4EnGeKEOfE2gm1FJK3614gdmjNgZu9csn7vG-GyIjcYBrd7by5u8BRT1LD_VziXpRtQ83CIGJvMxjLlUBz57vZIp7HwIWmsjBmcp-CxOL-wk6iSh0GTUZp-ztFlojOevt2QetIPMwj7bLFeOstY1EgKdbOVo_3xzdRipdJpiQKMxsFy_J4jGm611NEUpweJzkKIdeuA4AKM0N-6otFr3nLNNMmnAcJXxGJzr_QtR6XrnouD8vd-7xa1QqEgUUVF3U11kkGWLrOCmkLYSSMsjtTuzKk3avmt6Vz1I-uMoOUDSdkaWIta7zrJFcH8uiX9_cYdpnzPvl2m5YzXkzIH1551fodhtrGEVhSPgYQDAu-IrZAnNf5KM5ReGDhiwH5FD-snAmlEFgWKCkuzAh7FoHNG_71qTrwMSqVDHHQSYim7_VIxuRBgPRi3LObuzkW6i5rHKPcHQVo0186MZvLeYR95' \
--header 'Content-Type: application/json' \
--data-raw '{
"JenkinsJobName":"TM pipeline",
"ValidateWithThreatRisk":"false"
}'








//curlCommand="curl --location --request POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{\"JenkinsJobName\":\"$JOB_NAME\",\"ValidateWithThreatRisk\":false}'"
echo $curlCommand

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
