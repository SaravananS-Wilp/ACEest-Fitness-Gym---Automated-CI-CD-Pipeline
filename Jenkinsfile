pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fitness-app .'
            }
        }
    }
}