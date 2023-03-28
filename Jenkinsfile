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
                def tag = "${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}"
                def image = docker.build("roie710/${params.DOCKER_IMAGE_TAG}")
                // Tag the Docker image with the Jenkins build number
                image.tag("roie710/${tag}")
            }
        }
    }
        stage('Push image to Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'mycreds') {
                        // Push the Docker image with the Jenkins build number as the tag
                        def tag = "${params.DOCKER_IMAGE_TAG}:${BUILD_NUMBER}"
                        docker.image("roie710/${tag}").push()
                    }
                }
            }
        }
    }
}
