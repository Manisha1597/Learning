pipeline {
    agent any
    stages{
          stage('Creating vars file')
                {
                    steps{
                                  sh "/usr/bin/python3 create_yml.py ${currentBuild.number} ${JOB_NAME} $input1"
                                }

            }
     
        stage('Trigger playbook') {
            steps {
                 //copy inventory from /tmp to usecase folder with the build_number
                 sh "ansible-playbook -i inventory windows.yml --extra-vars job_name=${JOB_NAME} --extra-vars build_number=${currentBuild.number}"
    }
        }    
        stage('Post action') {
            steps {
                echo 'Completed'
            }
        }
    }
}
