pipeline {
    agent none
        stages {
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
