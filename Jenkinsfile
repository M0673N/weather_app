// Multibranch Pipeline with Webhook Trigger

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Install dependencies
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
                    def lintCommand = "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
                    if (isUnix()) {
                        sh "${lintCommand}"
                        sh "${lintCommand.replace('--count', '--exit-zero --max-complexity=10 --max-line-length=127')}"
                    } else {
                        bat "${lintCommand}"
                        bat "${lintCommand.replace('--count', '--exit-zero --max-complexity=10 --max-line-length=127')}"
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

        stage('Deploy to Render') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'RENDER_API_KEY', variable: 'RENDER_API_KEY'), 
                        string(credentialsId: 'RENDER_DEPLOY_HOOK', variable: 'RENDER_DEPLOY_HOOK')
                    ]) {

                        // Trigger the deploy via the Render API
                        def response = bat(script: """
                            curl -X POST https://api.render.com/v1/services/${env.RENDER_DEPLOY_HOOK}/deploys ^
                            -H "Authorization: Bearer ${env.RENDER_API_KEY}" ^
                            -H "Content-Type: application/json" ^
                            -d "{}"
                        """, returnStdout: true).trim()

                        echo "Response from Render: ${response}"

                        // Alternative JSON parsing using JsonSlurper
                        import groovy.json.JsonSlurper
                        def jsonSlurper = new JsonSlurper()
                        def jsonResponse = jsonSlurper.parseText(response)
                        def deployId = jsonResponse.id

                        // Poll for deployment status
                        def status = ''
                        def maxRetries = 50 // Set a maximum number of retries
                        def retryCount = 0

                        while (retryCount < maxRetries) {
                            sleep(10) // Wait for 10 seconds before checking again

                            // Check the status of the deployment
                            def statusResponse = bat(script: """
                                curl -X GET https://api.render.com/v1/deploys/${deployId} ^
                                -H "Authorization: Bearer ${env.RENDER_API_KEY}" ^
                                -H "Content-Type: application/json"
                            """, returnStdout: true).trim()

                            echo "Status response from Render: ${statusResponse}"
                            def jsonStatusResponse = jsonSlurper.parseText(statusResponse)
                            status = jsonStatusResponse.state

                            if (status == 'finished') {
                                echo "Deployment finished successfully."
                                break
                            } else if (status == 'failed') {
                                error("Deployment failed.")
                            }

                            retryCount++
                        }

                        if (status != 'finished') {
                            error("Deployment did not finish in expected time.")
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
