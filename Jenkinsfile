pipeline {
    agent { 
        docker { 
            image 'python:3.9.6-alpine3.14' 
        } 
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app_python/requirements.txt'
            }
        }

        stage('Linting') {
            steps{
                sh 'flake8 app_python'
            }
        }

        stage('Unit Testing') {
            steps{
                sh 'pytest app_python/tests'
            }
        }
    }
}