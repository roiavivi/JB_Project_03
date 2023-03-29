pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
        string(name: 'IMAGE_VERSION', defaultValue: 'latest', description: 'The version for the Docker image')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "${params.BRANCH}"]], userRemoteConfigs: [[url: 'https://github.com/roiavivi/JB_Project_03.git']]])
            }
        }
        stage('Run Docker image') {
            steps {
                script {
                    sh "docker run -it roie710/${params.DOCKER_IMAGE_TAG}:${params.IMAGE_VERSION}"
                }
            }
        }
    }
}
