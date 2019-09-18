pipeline {
    agent any
    
    script_file = "./bob-packager.py"
    stages {
        return_code = 0
        stage('clone') {
            steps {
                return_code = sh ( 
                  script: "${script}",
                  args: ["-s", "${STAGE_NAME}"],
                  returnStatus: true,
                  returnStdout: true)
            }
        }
        stage('reset') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('exists') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('checkout') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('prepare') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('clean') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('build') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        stage('package') {
            steps {
                sh "${script_file} -s ${STAGE_NAME}"
            }
        }
        if(return_code != 0)
        {
          echo 'fail'
        }
        else
        {
          echo 'success'
        }
    }
}
