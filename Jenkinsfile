pipeline {
    agent any

    stages {
        stage('reset') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('exists') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('checkout') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('prepare') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('clean') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('build') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
        stage('package') {
            steps {
                sh "./bob-packager.py -s ${STAGE_NAME}"
            }
        }
    }
}
