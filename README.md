ABOUT

This project create as a POC of full CI pipeline.
In this POC we created EC2 instance monitoring application which will track our running
instances for every 5 minutes also, it will test application with Pylint & Sonarqube.

Installation:

1. Run Sonrqube server:


    docker run -d --name sonarqube --restart=always -p 9000:9000 -p 9092:9092 sonarqube


2. Create two piplines: 
- CI Pipeline (convert our app to a docker image test it and push it to DockerHub )
- cron Pipeline (pull the docker image and run the app to scan AWS EC2 for running instances)

CI Pipeline 

    Pull from GitHub: This stage uses the GitSCM plugin to checkout a specified branch from a GitHub repository.
    Build Docker image: This stage builds a Docker image using the Docker plugin, 
    with a specified tag that includes the Jenkins build number.
    Push image to Hub: 
    This stage pushes the Docker image to Docker Hub using the Docker plugin and a specified Docker Hub registry URL and credentials.

    In addition, the pipeline includes a "parameters" section that allows the user to specify the branch to checkout from GitHub and the Docker image tag to use. 
    The pipeline also includes a "post" section that ensures the workspace is cleaned up after the pipeline is run, regardless of success or failure.

cron Pipeline

    Pull from GitHub: This stage uses the Git plugin to checkout a specified branch from a GitHub repository.
    Run Docker image: This stage runs a Docker image using a custom Groovy function called runDockerImage(), 
    which takes in the Docker image tag and version as parameters. The withCredentials block provides AWS access key and secret access key for the Docker container.

    In addition, the pipeline includes a "parameters" section that allows the user to specify the branch to checkout from GitHub, 
    the Docker image tag to use, and the version for the Docker image. The pipeline also includes a "triggers" section that schedules the pipeline to run every 5 minutes, 
    and a "post" section that ensures the workspace is cleaned up after the pipeline is run, 
    regardless of success or failure.

    The runDockerImage() function uses the Jenkins instance object to get the current Jenkins instance, 
    and uses it to retrieve the CI job (assuming there is a job named CI in the Jenkins instance). 
    It then retrieves the last successful build of the CI job and uses its build number to generate the Docker image tag, 
    which includes the build number if the version is set to latest. Finally, 
    it runs the Docker image with the specified tag and AWS credentials. 
    The @NonCPS annotation is used to mark the function as non-continuation-passing-style (CPS) code, 
    which allows it to run outside the Jenkins script context and avoid certain restrictions.

    


