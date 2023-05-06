pipeline {
    agent {
        node {
            label 'python'
        }
    }
    
    environment {
        // Define the credentials ID and repository URL
//         GIT_CREDENTIALS_ID = 'GH_TOKEN'
//         GIT_TOKEN = credentials('GH_TOKEN')
//         GIT_REPO_URL = 'https://${GIT_TOKEN}@github.com/marijaaab/final.git'
        IMAGE_NAME = 'final-test'
        CONTAINER_NAME = 'final-test-app'
        HOST_PORT = '8001'
        CONTAINER_PORT = '8001'
    }
    
    stages {
            
        stage ("Build the image") {
            
            steps {
                
                script {
                    
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                    sh "docker image prune --force"
                    
                }
                
            }
            
        }
        
        stage ("Run the container") {
            
            steps {
                
                script {
                    
                    def containerExists = sh(returnStdout: true, script: "docker ps -a --format '{{.Names}}' | grep ${CONTAINER_NAME}").trim()
            
                    if (containerExists) {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }
                    
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:latest"
                    
                }
                
            }
            
        }
        
    }
    post { 
        success { 
            println("The image is built and container is up! Visit: " + "http://localhost:${HOST_PORT}")
        }
    }
}
