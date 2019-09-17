pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                ./bob-packager.py
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
