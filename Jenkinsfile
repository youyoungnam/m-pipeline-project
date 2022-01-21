pipeline{
    agent any
    stages {
        stage("checkout"){
            steps{
                checkout scm
            }
        }
        stage("Build"){
            steps{
                sh "docker-compose build train-prediction-server"
            }
        }
        stage("check model update"){
            steps{
                script{
                    def CHANGE = sh(script: "git diff ${GIT_PREVIOUS_SUCCESSFUL_COMMIT} ${GIT_COMMIT} train.py", returnStdout: true)
                    if(CHANGE.length() > 0){
                        sh "docker exec -i fastapis python train.py"
                    }
                }
            }
        }
        stage("deploy"){
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}