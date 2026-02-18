pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app:latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
            }
        }

        stage('Restart Pods') {
            steps {
                bat 'kubectl delete pod --all'
            }
        }
    }
}
