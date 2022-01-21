pipeline {
	agent any
	parameters {
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
        stage("Check dockerfile update"){
            steps{
                script{
                    def CHANGE = sh(script: "git diff ${GIT_PREVIOUS_SUCCESSFUL_COMMIT} ${GIT_COMMIT} train.py", returnStdout: true)
                    if (CHANGE.length() > 0){
                        sh "gogo"
                    }
                }
        }
        }
		stage("deploy") {
			steps {
				sh "docker-compose up -d"
			}
		}
	}
}