pipeline {
	agent any
	parameters{
		choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
		booleanParam(name: 'executeTests', defaultValue: true, description: '')
	}
	stages {
		stage("Checkout") {
			steps {
				checkout scm
			}
		}
		stage("Build") {
			steps {
				sh 'docker-compose build train-prediction-server'
			}
		}

		stage("deploy") {
			steps {
				sh "docker-compose up -d"
			}
		}
        stage("Check model update"){
            steps{
                script{
                    scmVar = checkout(scm)
                    def CHANGE = sh(script: "git diff ${scmVar.GIT_PREVIOUS_COMMIT} ${scmVar.GIT_COMMIT} train.py", returnStdout: true)
                    if (CHANGE.length() > 0){
                        sh "docker exec -i fastapis python train.py"
                    }
                }
        }
        }
		stage("Docker push Dockerhub"){
			steps{
				 withCredentials([[$class: 'UsernamePasswordMultiBinding',
                        credentialsId: 'docker-hub', 
                        usernameVariable: 'DOCKER_USER_ID', 
                        passwordVariable: 'DOCKER_USER_PASSWORD'
                        ]]){
				sh "docker tag train-prediction-server:latest ${DOCKER_USER_ID}/model-images:${BUILD_NUMBER}"
				sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
				sh "docker push ${DOCKER_USER_ID}/model-images:${BUILD_NUMBER}"
			}
			}
		}        
	}
}