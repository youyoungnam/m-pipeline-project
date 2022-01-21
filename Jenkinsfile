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
		stage("deploy") {
			steps {
				sh "docker-compose up -d"
			}
		}
	}
}