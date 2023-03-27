pipeline {
    agent any
    stages{
        stage('Pull from github'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t roie710/devops-integration .'
                }
            }
        }
        stage('Push image to Hub'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                   sh 'docker login -u javatechie -p ${dockerhubpwd}'

}
                   sh 'docker push roie710/devops-integration'
                }
            }
        }
    }
}