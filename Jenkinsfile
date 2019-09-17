pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh './bob-packager.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
