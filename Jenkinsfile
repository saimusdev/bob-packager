pipeline {
    agent any

    stages {
        stage('reset') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('exists') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('checkout') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('prepare') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('clean') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('build') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
        stage('package') {
            steps {
                echo "${STAGE_NAME}..."
                sh "./bob-packager.py -s= ${STAGE_NAME}"
            }
        }
    }
}
