pipeline {

    agent any

    environment {
        COMPOSE_FILE     = "docker-compose.yml"
        BACKEND_IMAGE    = "myapp-backend"
        FRONTEND_IMAGE   = "myapp-frontend"
        IMAGE_TAG        = "${env.BUILD_NUMBER}"
    }

    options {
        timeout(time: 20, unit: "MINUTES")
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: "10"))
    }

    stages {

        // ── 1. checkout ───────────────────────────────────────────────────────
        stage("Checkout") {
            steps {
                checkout scm
                echo "Branch: ${env.BRANCH_NAME} | Build: ${env.BUILD_NUMBER}"
            }
        }

        // ── 2. lint / basic checks ────────────────────────────────────────────
        stage("Lint") {
            steps {
                sh """
                    pip install --quiet flake8
                    flake8 backend/app.py --max-line-length=120 --ignore=E501
                """
            }
        }

        // ── 3. build images ───────────────────────────────────────────────────
        stage("Build") {
            parallel {
                stage("Build Backend") {
                    steps {
                        sh "docker build -t ${BACKEND_IMAGE}:${IMAGE_TAG} ./backend"
                        sh "docker tag ${BACKEND_IMAGE}:${IMAGE_TAG} ${BACKEND_IMAGE}:latest"
                    }
                }
                stage("Build Frontend") {
                    steps {
                        sh "docker build -t ${FRONTEND_IMAGE}:${IMAGE_TAG} ./frontend"
                        sh "docker tag ${FRONTEND_IMAGE}:${IMAGE_TAG} ${FRONTEND_IMAGE}:latest"
                    }
                }
            }
        }

        // ── 4. test ───────────────────────────────────────────────────────────
        stage("Test") {
            steps {
                sh """
                    docker compose -f ${COMPOSE_FILE} up -d --build
                    sleep 15
                    curl -f http://localhost:5000/api/health || exit 1
                    curl -f http://localhost:80            || exit 1
                    echo "All health checks passed"
                """
            }
            post {
                always {
                    sh "docker compose -f ${COMPOSE_FILE} down --remove-orphans"
                }
            }
        }

        // ── 5. deploy (main branch only) ──────────────────────────────────────
        stage("Deploy") {
            when { branch "main" }
            steps {
                sh """
                    docker compose -f ${COMPOSE_FILE} pull  || true
                    docker compose -f ${COMPOSE_FILE} up -d --build --remove-orphans
                    echo "Deployed build ${IMAGE_TAG}"
                """
            }
        }

    }

    // ── post actions ──────────────────────────────────────────────────────────
    post {
        success {
            echo "Pipeline SUCCESS - Build ${env.BUILD_NUMBER}"
        }
        failure {
            echo "Pipeline FAILED  - Build ${env.BUILD_NUMBER}"
            sh "docker compose -f ${COMPOSE_FILE} down --remove-orphans || true"
        }
        cleanup {
            // remove dangling images to save disk
            sh "docker image prune -f || true"
        }
    }
}