pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout the repository
                checkout scm
                
                // Install dependencies (assuming Python 3.10 is already installed on the Windows machine)
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'pip install flake8'
            }
        }

        stage('Lint with flake8') {
            steps {
                bat '''
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''

                // Run Tests
                // bat 'python -m unittest test_app.py'
                bat "echo 'heloooo'"
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
