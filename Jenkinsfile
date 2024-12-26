pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'pip install flake8'
            }
        }

        stage('Lint') {
            steps {
                bat '''
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''
            }
        }

        stage('Test') {
            steps {
                // bat 'python -m unittest test_app.py'
                bat "echo 'heloooo'"
            }
        }
    }
}
