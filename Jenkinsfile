// Multibranch Pipeline with Webhook Trigger

pipeline {
    agent any

    environment {
        RENDER_API_KEY = credentials('RENDER_API_KEY')
        RENDER_DEPLOY_HOOK = credentials('RENDER_DEPLOY_HOOK_WEATHER_APP')
    }

    stages {
        stage('Build') {
            steps {
                // Assuming you have Python 3.10 installed
                script {
                    if (isUnix()) {
                        sh'''
                            python3 -m venv .venv
                            . .venv/bin/activate
                            python3 -m pip install --upgrade pip
                            pip3 install -r requirements.txt
                            pip3 install flake8
                        '''
                    } else {
                        bat '''
                            python -m venv .venv
                            call .venv/Scripts/activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                            pip install flake8
                        '''
                    }
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . .venv/bin/activate
                            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=.venv
                            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=.venv
                        '''
                    } else {
                        bat '''
                            call .venv/Scripts/activate
                            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=.venv
                            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=.venv
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . .venv/bin/activate
                            python3 -m unittest test_app.py
                        '''
                    } else {
                        bat '''
                            call .venv/Scripts/activate
                            python -m unittest test_app.py
                        '''
                    }
                }
            }
        }

        stage('Deploy to Render') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Trigger the redeploy via the Render API
                    if (isUnix()) {
                        sh """
                            curl -X POST https://api.render.com/v1/services/${env.RENDER_DEPLOY_HOOK}/deploys \
                            -H "Authorization: Bearer ${env.RENDER_API_KEY}" \
                            -H "Content-Type: application/json" \
                            -d "{}"
                        """
                    } else {
                        bat """
                            curl -X POST https://api.render.com/v1/services/${env.RENDER_DEPLOY_HOOK}/deploys ^
                            -H "Authorization: Bearer ${env.RENDER_API_KEY}" ^
                            -H "Content-Type: application/json" ^
                            -d "{}"
                        """
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
