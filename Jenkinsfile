pipeline {
    agent any

    environment {
        // Jenkins credentials ID for SonarQube token
        SONAR_TOKEN = credentials('Github')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull your GitHub code
                git 'https://github.com/harikrishnank061/Employee-Management-System-Python-MySQL-Database-Connectivity'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube_server') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=employee-management \
                      -Dsonar.sources=. \
                      -Dsonar.language=py \
                      -Dsonar.python.version=3 \
                      -Dsonar.sourceEncoding=UTF-8 \
                      -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
}
