pipeline {
    agent {
        node {
            label 'python'
        }
    }
    
//     environment {
//         // Define the credentials ID and repository URL
//         GIT_CREDENTIALS_ID = 'GH_TOKEN'
//         GIT_TOKEN = credentials('GH_TOKEN')
//         GIT_REPO_URL = 'https://${GIT_TOKEN}@github.com/marijaaab/final.git'
//     }
    
    stages {
            
        stage ("Build the image") {
            
            steps {
                
                script {
                    
                    sh "docker build -t final-test:latest ."
                    sh "docker image prune --force"
                    
                }
                
            }
            
        }
        
        stage ("Run the container") {
            
            steps {
                
                script {
                    
                    def containerExists = sh(returnStdout: true, script: "docker ps -a --format '{{.Names}}' | grep final-test-app").trim()
            
                    if (containerExists) {
                        sh "docker stop final-test-app"
                        sh "docker rm final-test-app"
                    }
                    
                    sh "docker run -d --name final-test-app -p 8001:8001 final-test:latest"
                    
                }
                
            }
            
        }
        
    }
    post { 
        success { 
            println("The image is built and container is up! Visit: " + "http://localhost:8001")
        }
    }
}
