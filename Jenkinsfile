pipeline {
    // agent any This specifies that Jenkins can use any available agent to run the pipeline
     agent {
                docker {
                    image 'yahorprys/my-custom-jenkins-image:latest' // Specify your Docker image
                }
            }
    stages {
        stage('Check Python') {
            steps {
                sh 'python3 --version'  // Check Python version
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'python3 --version'
                sh 'pwd'
                sh 'ls -la'
                sh 'pytest_homework.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        unstable {
            echo 'Pipeline is unstable!'
        }

        changed {
            echo 'Pipeline state changed!'
        }
    }
}
