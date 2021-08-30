pipeline {
    environment {
        registry = "nufusrufus/devops"
        app_dir = "app_python"
    }

    agent { 
        docker { 
            image 'python:3.9.6-alpine3.14'
            args '-u 0 -v $HOME/.cache:/root/.cache -v /var/run/docker.sock:/var/run/docker.sock'
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
                sh 'apk add gcc musl-dev docker'
            }
        }

        stage('Install Dependencies') {
            steps {
                withPythonEnv('python') {
                    sh 'pip install -r $app_dir/requirements.txt'
                }
            }
        }

        stage('Linting') {
            steps {
                withPythonEnv('python') {
                    sh 'flake8 $app_dir'
                }
            }
        }

        stage('Unit Testing') {
            steps {
                withPythonEnv('python') {
                    sh 'pytest $app_dir/tests'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                dir("${app_dir}") {
                    script {
                        def image = docker.build('$registry:jenci-$BUILD_NUMBER')
                        docker.withRegistry('', 'dockerhub') {
                            image.push()
                        }
                    }
                }
            }
        }  
    }
}