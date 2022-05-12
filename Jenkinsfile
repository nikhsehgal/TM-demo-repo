pipeline {
    agent any
    stages {
        stage('Checkout'){
            steps {
                echo 'SCM stage'
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e63fe600-4939-4815-a2af-10b5ed155c21', url: 'https://github.com/nikhsehgal/TM-demo-repo.git']]])
                
            }
            
        }
        stage('Build'){
            steps{
               echo 'Building an Application '
               git branch: 'main', credentialsId: 'e63fe600-4939-4815-a2af-10b5ed155c21', url: 'https://github.com/nikhsehgal/TM-demo-repo.git'
              // bat '''batch.bat'''
              //sh './script.sh'
              //sh '''chmod +x script.sh , 
              //./script.sh'''
              //sh 'bash ./script.sh'
            }
        }   
        stage('ThreatModel Validation'){
            steps{
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
               echo 'ThreatModeler validation'
               // step <object of type org.jenkinsci.plugins.threatmodeler.ThreatModelerBuilder>
            }
        }    
        stage('Push'){
            steps{
                echo 'Push to Artifactory'
            }       
        }    
        
    }
}
