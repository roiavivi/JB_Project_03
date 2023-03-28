pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t roie710/${params.DOCKER_IMAGE_TAG} .'
            }
        }
//         stage('Push image to Hub') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'mycreds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
//                     sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
//                     sh "docker push roie710/${params.DOCKER_IMAGE_TAG}"
//                 }
//             }
//         }
    }
}
