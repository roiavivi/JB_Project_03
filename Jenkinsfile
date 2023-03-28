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
                script {
                    docker.build("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}")
                }
            }
        }
        stage('Push image to Hub') {
            steps {
                script {
                        docker.withRegistry('https://registry.hub.docker.com', 'mycreds') {
                            docker.image("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}").push()
                            docker.image("roie710/${params.DOCKER_IMAGE_TAG}:latest").push()
                        }
                }
            }
        }
    }
}
