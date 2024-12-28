pipeline {
    agent any 
    stages {
        stage('Install requirements.txt') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') { 
            steps {
                sh 'python3 -m unittest test_main.py'
            }
        }
    }
} 