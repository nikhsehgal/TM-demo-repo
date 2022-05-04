pipeline {
    agent any
    //tools {
       // ThreatModeler ThreatModeler
    //}
    stages {
        stage('Checkout'){
            steps {
                echo 'SCM stage'
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e63fe600-4939-4815-a2af-10b5ed155c21', url: 'https://github.com/nikhsehgal/TM-demo-repo.git']]])
                
            }
            
        }
        stage('Build'){
            steps{
               echo 'Building a Docker Application '
               // step <object of type org.jenkinsci.plugins.threatmodeler.ThreatModelerBuilder>
    
            }
        }   
        stage('ThreatModel Validation'){
            steps{
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
