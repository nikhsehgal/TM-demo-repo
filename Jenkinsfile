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
validate=$(curl -X POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' --header 'Authorization:Bearer urBlK3LPTwJaccy7RXSwtTfEUvvHHPrdnDrbUVatVkHY0HoHXpQNE9SJiVSM3-5GGz1eHrTo_ds0HQMf_C4UaezI4q3IkiUbq-Fx-62xvIOXtr_lQtGSzI3sBLVPitPZkXov2rzhbsVOl2YqBiyKsCWn5w0D323x5X8rm_jCvwU5MOPRTUgrPUab9YHATqHzoSK74tdTnT2DzRg-dHbIIKdiTyF1PsRAZEWC7xe1gZaChCf-piMVAkgaFqis9LOw7f2l6SC3laQ1zq3TaWHqTdcQ9h0pxwHgwXnwr42TBDWw4gaBHFPq1OMgIdAUza8A75nU-XIOVsmFOCeCt-yzyAUkD7KS1OBnHOH2FoNC7wOlwrxMio8xB5OUifDW31_cwEhd6ih7YUjCT2NbcD8Q3OfFobrFG4cwFPiaqRsyz4Z89MojefnVfLM42tty_RkEardrzNdKkoqNdnC-jJ0U6IYoArbIn1ZEAwhJSpC42MUSW7JZoHU9qJu9eMAKXWa-GQTrxcuXYCBjKt9-Mggh57jFYrfD0T6rjQKPr_jp3XyVTB-dTW2QLbVsn50yhMPvay3rfkKXJJ78y8o9IE9Lsav71OvmHAGpyXkIDhpXs_IWZxQMkTYfh68Os9h36_h4B8bpQEGCPD6soE_ZbsZzTnjjPdAivL4xX99fTIGf_XOSPSnjqJDfnxO9V60ibY-UyKEvAYraFAowjsZ7gs8r5Gdw1pW_-IMp2M-EMmjaSbNdb2LchT3ri0BnEVwxqd85a5_iqHxUr4SBX9ShF3ageezT1OVDrTBru5-wUqVfQ5QJdWTSfAhJaA7vcVz-MYfcxQw8dRvmWkuahqZPA0GAXa_rtcTwrPoxR4ab1gOgl9rrwUnQGkg8azW8585HC5b8UHf_MXXhkBYSXZe5AYGityROjOz1CgxQ3b_iRI8zJ0F_momFc5JIXmQsCRsOw3aT0BsiRXi-suMnKXrZccz6mza3j-7y93STPRi6qXtcuQOqjOF226BzCx_mKx8Je0XbmoFL9gMkUieieWDaRQCOlA_qjEeG9huB31prg9cNDa4280RMAzg6PBsoP8xdxgliVAIoVefDDuTP6u5uDbbQYWgEfAs1Qy7ZkobG5zX09ehmmI0TYofOSPxYCj5aXvbDZ5pUSUOeLG5na9Xu9QBMZmPhz_bhlpAnaL7cpdbeDQhjqriNuvELjAB8_6KwIoIoV1_6-hDo_Eh2KactG1M1KvqaWIluaET6tVOxMKGuP1x0BulJtdwfNEDT-pSCu83j1uiSUU4CydoA6hw-ibw0MTwvCp-3ZQrVTy4IdZLTS2lCbmi0HXu27pqq6Py_qYDvdlC4fpgPc9edIIS8vfo8_awRvdtmSMr31hY7Dg2dZA2_ic-Pv4gppCjiDtnMHxfnlGy2_gcoTGI57B_3JEVUS0VZl9HFRHJ6nlHx-ssWCoOCTO4D4BI-TVaSwMZ3JBW5' --header 'Content-Type:application/json' -d '{"JenkinsJobName":"$JOB_NAME","ValidateWithThreatRisk":false}')

curlCommand="curl --X --request POST 'https://deloitte-poc.threatmodeler.net/api/jenkins/validate' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{\"JenkinsJobName\":\"$JOB_NAME\",\"ValidateWithThreatRisk\":false}'"
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
