pipeline {
    agent {
        node {
            label 'python'
        }
    }
    
    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'final-test', description: 'Name of Docker image')
        string(name: 'CONTAINER_NAME', defaultValue: 'final-test-app', description: 'Name of Docker container')
        string(name: 'HOST_PORT', defaultValue: '8001', description: 'Host port for exposing the container')
        string(name: 'CONTAINER_PORT', defaultValue: '8001', description: 'Container port for the application')
    }
    
    stages {      
        
        stage ("Build Docker image") {  
            steps {   
                script { 
                    sh "docker build -t ${params.IMAGE_NAME}:latest ."
                }          
            }
        }
        
        stage ("Run Docker container") {
            steps {
                script {
                    def containerExists = sh(returnStdout: true, script: "docker ps -a --format '{{.Names}}' | grep ${params.CONTAINER_NAME}").trim()
                    if (containerExists) {
                        sh "docker stop ${params.CONTAINER_NAME}"
                        sh "docker rm ${params.CONTAINER_NAME}"
                        sh "docker image prune --force"  
                    }
                    sh "docker run -d --name ${params.CONTAINER_NAME} -p ${params.HOST_PORT}:${params.CONTAINER_PORT} ${params.IMAGE_NAME}:latest"
                }
            }
        }
    }
    
    post { 
        success { 
            println("The image is built and container is up! Visit: " + "http://localhost:${params.HOST_PORT}")
        }
    }
}
