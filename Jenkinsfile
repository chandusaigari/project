pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/chandusaigari/project'
                    credentialsId:'git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chandu0303/web:v1  .'
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
                sh 'docker ps -a'
            }
        }
    }
    post {
    success {
        emailext(
            to: 'chandusaigari6@gmail.com',
            subject: "✅ Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: 'Deployment succeeded!',
            mimeType: 'text/html'
        )
    }
    failure {
        emailext(
            to: 'chandusaigari6@gmail.com',
            subject: "❌ Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: 'Check console log.',
            mimeType: 'text/html'
        )
    }
 }   
}    

    
