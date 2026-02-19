# End-to-End CI/CD Pipeline using Jenkins, Docker & Kubernetes

## 📌 Project Overview

This project demonstrates a production-style CI/CD pipeline that automates build, containerization, Docker image push, and deployment of a Flask application to Kubernetes using Jenkins.

The pipeline integrates GitHub, Docker Hub, and Minikube to simulate real-world DevOps workflow.

---

## 🏗 Architecture

GitHub → Jenkins → Docker Build → Docker Hub → Kubernetes (Minikube)

---

## ⚙️ Tech Stack

- Jenkins (Pipeline Automation)
- Docker (Containerization)
- Docker Hub (Image Registry)
- Kubernetes (Minikube)
- Git & GitHub (Version Control)
- Flask (Sample Application)
- Linux (Ubuntu)

---

## 🔄 CI/CD Pipeline Flow

1. Developer pushes code to GitHub.
2. Jenkins automatically triggers pipeline.
3. Docker image is built.
4. Image is pushed to Docker Hub.
5. Kubernetes deployment is updated.
6. Application becomes accessible via NodePort.

---

## 📦 Docker Image

Docker Hub Repository:
https://hub.docker.com/r/abhishekmuramatti/flask-app

---

## 🚀 How to Run Locally

### 1️⃣ Start Minikube
```bash
minikube start

### 2️⃣ Apply Kubernetes Manifests
 kubectl apply -f k8s/deployment.yaml
 kubectl apply -f k8s/service.yaml

### 3️⃣ Access Service
minikube service flask-service --url


