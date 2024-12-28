// Multibranch Pipeline with Webhook Trigger

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Assuming you have Python 3.10 installed
                script {
                    if (isUnix()) {
                        sh 'python3 -m pip install --upgrade pip'
                        sh 'pip3 install -r requirements.txt'
                        sh 'pip3 install flake8'
                    } else {
                        bat 'python -m pip install --upgrade pip'
                        bat 'pip install -r requirements.txt'
                        bat 'pip install flake8'
                    }
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                        '''
                    } else {
                        bat '''
                            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest test_app.py'
                    } else {
                        bat 'python -m unittest test_app.py'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
