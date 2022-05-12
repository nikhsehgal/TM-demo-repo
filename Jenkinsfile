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
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "exit 1"
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
