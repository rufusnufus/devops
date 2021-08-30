pipeline {
    environment {
        registry = "nufusrufus/devops"
    }

    agent { 
        docker { 
            image 'python:3.9.6-alpine3.14'
            args '-u 0'
        } 
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install packages') {
            steps {
                sh 'apk add --no-cache gcc musl-dev'
            }
        }

        stage('List repo') {
            steps {
                sh 'ls -al'
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

        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":jenci-$BUILD_NUMBER"
                }
            }
        }

        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry('', 'dockerhub' ) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:jenci-$BUILD_NUMBER"
            }
        }
    }
}