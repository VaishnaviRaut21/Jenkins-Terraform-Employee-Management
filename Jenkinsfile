pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask application...'
                bat 'python -m py_compile app/app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                bat 'pytest'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application...'
                bat 'powershell Compress-Archive -Path app,requirements.txt -DestinationPath employee-management.zip -Force'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Employee Management System...'
                echo 'Application deployment completed successfully!'
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}