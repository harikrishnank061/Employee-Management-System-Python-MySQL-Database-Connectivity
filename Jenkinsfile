pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('github_s')  // Jenkins credential for SonarQube token
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
                    bat """
                        sonar-scanner ^
                          -Dsonar.projectKey=github-jenkins-sonar^
                          -Dsonar.sources=. ^
                          -Dsonar.language=py ^
                          -Dsonar.sourceEncoding=UTF-8 ^
                          -Dsonar.login=%SONAR_TOKEN%
                    """
                }
            }
        }
    }
}
