pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/SaravananS-Wilp/ACEest-Fitness-Gym---Automated-CI-CD-Pipeline'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fitness-app .'
            }
        }
    }
}