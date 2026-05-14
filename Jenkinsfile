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
                to: '$DEFAULT_RECIPIENTS',
                subject: "✅ Deployment Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """\
                    <p>The deployment was successful!</p>
                    <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                    <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Build URL:</strong> <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>
                    <p><strong>Branch:</strong> ${env.GIT_BRANCH}</p>
                    <p><strong>Deployed at:</strong> ${new Date()}</p>
                    <p>Next steps: Monitor application health and logs.</p>
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                mimeType: 'text/html'
            )
        }
        failure {
            echo '❌ Deployment Failed!'
            emailext(
                to: '$DEFAULT_RECIPIENTS',
                subject: "❌ Deployment Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """\
                    <p>The deployment has failed.</p>
                    <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                    <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Build URL:</strong> <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>
                    <p>Check the console output for details: <a href='${env.BUILD_URL}console'>Console Log</a></p>
                    <p>Take immediate action to restore service.</p>
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
