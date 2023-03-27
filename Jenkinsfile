pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
        string(name: 'DOCKERHUB_USER', description: 'Docker Hub username')
        password(name: 'DOCKERHUB_PWD', description: 'Docker Hub password')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    sh "docker build -t roie710/${params.DOCKER_IMAGE_TAG} ."
                }
            }
        }
//         stage('Push image to Hub') {
//             steps {
//                 script {
//                     withCredentials([string(credentialsId: 'DOCKERHUB_PWD', variable: 'dockerhubpwd'),
//                                      string(credentialsId: 'DOCKERHUB_USER', variable: 'dockerhubuser')]) {
//                         sh "docker login -u ${params.DOCKERHUB_USER} -p ${dockerhubpwd}"
//                         sh "docker push roie710/${params.DOCKER_IMAGE_TAG}"
//                     }
//                 }
//             }
//         }
    }
}
