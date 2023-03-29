pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
    }

    stages {
        stage('Pull from GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: params.BRANCH]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
            }
        }

        stage('Build Docker image') {
            environment {
                DOCKER_IMAGE_NAME = "roie710/${params.DOCKER_IMAGE_TAG}"
                DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
                DOCKER_IMAGE_LATEST_TAG = "latest"
            }

            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_LATEST_TAG}")
                }
            }
        }

        stage('Push image to Hub') {
            environment {
                DOCKER_REGISTRY = "https://registry.hub.docker.com"
                DOCKER_CREDENTIALS_ID = "mycreds"
            }

            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push()
                        docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_LATEST_TAG}").push()
                    }
                }
            }
        }

        stage('Clean All Docker Images') {
            steps {
                sh 'docker rmi -f $(docker images -a -q)'
            }
        }
    }
}
