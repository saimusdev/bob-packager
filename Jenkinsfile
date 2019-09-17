pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout..'
                sh './bob-packager.py -s checkout'
            }
        }
        stage('Reset') {
            steps {
                echo 'Reset..'
                sh './bob-packager.py -s reset'
            }
        }
    }
}
