pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('Github')  // Jenkins credential for SonarQube
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/harikrishnank061/Employee-Management-System-Python-MySQL-Database-Connectivity'
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
                          -Dsonar.sourceEncoding=UTF-8 \
                          -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
}
