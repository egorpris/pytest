pipeline {
    agent any // This specifies that Jenkins can use any available agent to run the pipeline
    stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }
            stage('Setup Python Environment') {
            steps {
                script {
                    sh 'sudo apt install python3.11-venv'
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r req.txt
                    '''
                }
            }
        }
            stage('Run Tests') {
                steps {
                    echo 'Running tests...'
                    sh 'python --version'
                    sh 'python3 --version'
                    sh 'pwd'
                    sh 'ls -la'
                    sh '''
                    . venv/bin/activate
                    python3 pytest_homework.py
                    '''
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
    }
}            
