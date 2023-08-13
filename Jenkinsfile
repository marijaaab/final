pipeline {
    agent {
        node {
            label 'python'
        }
    }
    environment {
        CONTAINER_PORT = '8001'
    }

    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'final-test', description: 'Name of Docker image')
        string(name: 'IMAGE_VERSION', defaultValue: 'latest', description: 'Version of Docker image (example: v1 / 1.0.0 / latest ...')
        string(name: 'CONTAINER_NAME', defaultValue: 'final-test-app', description: 'Name of Docker container')
        string(name: 'HOST_PORT', defaultValue: '8001', description: 'Host port for exposing the container')
    }

    stages {
        stage ("Build Docker image") {
            steps {
                script {
                    sh "docker build -t ${params.IMAGE_NAME}:${params.IMAGE_VERSION} ."
                }
            }
        }

        stage ("Run Docker container") {
            steps {
                script {
                    def containerExistsOutput = sh(returnStdout: true, script: "docker ps -a  --format '{{.Names}}' | grep ${params.CONTAINER_NAME} || echo 'false'").trim()
                    def containerExists = containerExistsOutput == 'false' ? false : containerExistsOutput
                    println("Container exists? " + containerExists)
                    if (containerExists) {
                        def containerStatus = sh(returnStdout: true, script: "docker inspect -f '{{.State.Status}}' ${params.CONTAINER_NAME}").trim()
                        println("What is the status of the container? " + containerStatus)
                        def currentImageId = sh(returnStdout: true, script: "docker images -q ${params.IMAGE_NAME}:${params.IMAGE_VERSION}").trim()
                        println("Current image ID: " + currentImageId)
                        def containerImageId = sh(returnStdout: true, script: "docker inspect --format='{{.Image}}' ${params.CONTAINER_NAME} | cut -d ':' -f 2 | cut -c 1-12").trim()
                        println("New image ID: " + containerImageId)
                        if (currentImageId == containerImageId) {
                            println("The image is the same.")
                            if (containerStatus == "running") {
                                println("No changes detected in the image. Keeping the existing container running.")
                            } else {
                                println("There is a container with the same name, but it is not running. Let's remove it and start it again...")
                                sh "docker rm ${params.CONTAINER_NAME}"
                                sh "docker run -d --name ${params.CONTAINER_NAME} -p ${params.HOST_PORT}:${env.CONTAINER_PORT} ${params.IMAGE_NAME}:${params.IMAGE_VERSION}"
                            }
                        } else {
                            println("Two versions of the image are not the same. Let's stop and remove the container using the old image, and then deploy a new one...")
                            sh "docker stop ${params.CONTAINER_NAME}"
                            sh "docker rm ${params.CONTAINER_NAME}"
                            sh "docker image prune --force"
                            sh "docker run -d --name ${params.CONTAINER_NAME} -p ${params.HOST_PORT}:${env.CONTAINER_PORT} ${params.IMAGE_NAME}:${params.IMAGE_VERSION}"
                        }
                    } else {
                        sh "docker run -d --name ${params.CONTAINER_NAME} -p ${params.HOST_PORT}:${env.CONTAINER_PORT} ${params.IMAGE_NAME}:${params.IMAGE_VERSION}"
                    }
                }
            }
        }
    }
    
    post { 
        success { 
            println("The image is built and container is up! Visit: " + "http://localhost:${params.HOST_PORT}")
            addShortText(text: " ${params.IMAGE_NAME}:${params.IMAGE_VERSION} ", background: '#Ee98d3', borderColor: 'black', border: 1)
        }
    }
}
