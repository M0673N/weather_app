// Multibranch Pipeline with Webhook Trigger

pipeline {
    agent any

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
                        source .venv/Sctipts/activate
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
                            flake8 . --count --ignore=W503,E501 --max-line-length=127 \
                            --show-source --statistics --exclude=venv --max-complexity=10 --exit-zero 
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
                        sh '''
                        . .venv/bin/activate
                        python3 -m unittest test_app.py
                        '''
                    } else {
                        bat 'python -m unittest test_app.py'
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
                    withCredentials([
                        string(credentialsId: 'RENDER_API_KEY', variable: 'RENDER_API_KEY'), 
                        string(credentialsId: 'RENDER_DEPLOY_HOOK', variable: 'RENDER_DEPLOY_HOOK')
                    ]) {
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
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
