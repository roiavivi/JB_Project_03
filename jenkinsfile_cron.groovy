import com.cloudbees.groovy.cps.NonCPS

pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'eu-central-1'
    }
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'The branch to checkout from GitHub')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'devops-integration', description: 'The tag to use for the Docker image')
        string(name: 'IMAGE_VERSION', defaultValue: 'latest', description: 'The version for the Docker image')
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                git branch: "${params.BRANCH}", url: 'https://github.com/roiavivi/JB_Project_03.git'
            }
        }
        stage('Run Docker image') {
            steps {
                withCredentials([
                    [ $class: 'AmazonWebServicesCredentialsBinding',
                      credentialsId: 'aws-jenkins-demo',
                      accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                      secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                ]) {
                    runDockerImage(params.DOCKER_IMAGE_TAG, params.IMAGE_VERSION)
                }
            }
        }
    }
}

@NonCPS
def runDockerImage(tag, version) {
    def job = Jenkins.instance.getItemByFullName('CI')
    def lastCIBuild = job.getLastSuccessfulBuild()

    def imageTag = version == 'latest' ? "${tag}:${lastCIBuild.number}" : "${tag}:${version}"
    sh "docker run --env AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} --env AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} --env AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} roie710/${imageTag}"
}
