pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                script{
                    try {
                        checkout([$class: 'GitSCM', branches: [[name: "${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
                    } catch (err) {
                        echo "Error: ${err}"
                        currentBuild.result = 'FAILURE'
                        error "Failed to pull from GitHub"
                    }
                }
            }
        }
        stage('Apply SonarQube') {
            steps {
                script{
                    try {sh """
                        chmod +x docker-compose.yml
                        docker compose up -d
                    """
                    } catch (err) {
                        echo "Error: ${err}"
                        currentBuild.result = 'FAILURE'
                        error "Failed to build Docker image"
                    }
                }
            }
        }
        stage('Build Docker image') {
            steps {
                script{
                    try {
                         docker.build("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}")
                    } catch (err) {
                        echo "Error: ${err}"
                        currentBuild.result = 'FAILURE'
                        error "Failed to build Docker image"
                    }
                }
            }
        }
        stage('Push image to Hub') {
            steps {
                script{
                    try {
                        docker.withRegistry('https://registry.hub.docker.com', 'mycreds') {
                        docker.image("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}").push()
                            }
                    } catch (err) {
                        echo "Error: ${err}"
                        currentBuild.result = 'FAILURE'
                        error "Failed to push image to Hub"
                    }
                }
            }
        }
        stage('Clean All Docker Images') {
            steps {
                script{
                    try {
                        sh 'docker rmi -f $(docker images -a -q)'
                    } catch (err) {
                        echo "Error: ${err}"
                        currentBuild.result = 'FAILURE'
                        error "Failed to clean all Docker images"
                    }
                }
            }
        }
    }
}
