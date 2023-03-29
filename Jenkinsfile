pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                try {
                    checkout([$class: 'GitSCM', branches: [[name: "${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
                } catch (err) {
                    echo "Error: ${err}"
                    currentBuild.result = 'FAILURE'
                    error "Failed to pull from GitHub"
                }
            }
        }
        stage('Build Docker image') {
            steps {
                try {
                    script {
                        docker.build("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}")
                    }
                } catch (err) {
                    echo "Error: ${err}"
                    currentBuild.result = 'FAILURE'
                    error "Failed to build Docker image"
                }
            }
        }
        stage('Push image to Hub') {
            steps {
                try {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', 'mycreds') {
                            docker.image("roie710/${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}").push()
                        }
                    }
                } catch (err) {
                    echo "Error: ${err}"
                    currentBuild.result = 'FAILURE'
                    error "Failed to push image to Hub"
                }
            }
        }
        stage('Clean All Docker Images') {
            steps {
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
