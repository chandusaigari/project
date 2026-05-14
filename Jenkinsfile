pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/chandusaigari/project'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
        stage('Verify Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
    post {
        success {
            echo '✅ Deployment Successful!'
            emailext(
                subject: "✅ Deployment Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """\
The deployment was successful!

Job: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Branch: ${env.GIT_BRANCH}
Deployed at: ${new Date()}

Next steps: Monitor application health and logs.
""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                mimeType: 'text/html'
            )
        }
        failure {
            echo '❌ Deployment Failed!'
            emailext(
                subject: "❌ Deployment Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """\
The deployment has failed.

Job: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Check the console output for details: ${env.BUILD_URL}console

Take immediate action to restore service.
""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                mimeType: 'text/html'
            )
        }
        always {
            cleanWs() // Clean workspace after build
        }
    }
}   
