pipeline {
    agent any  // This specifies that Jenkins can use any available agent to run the pipeline

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'ls -la'
                sh 'python3 pytest_homework.py'
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
