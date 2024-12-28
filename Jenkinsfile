pipeline {
    agent any 
    stages {
        stage('Istall requirements.txt') { 
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') { 
            steps {
                sh 'python -m unittest test_main.py'
            }
        }
    }
} 