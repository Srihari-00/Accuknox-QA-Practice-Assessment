# Accuknox-QA-Practice-Assessment
Accuknox-QA-Trainee-Practice-Assessment

# Wisecow Application - Containerization and Deployment on Kubernetes

## Overview
This project demonstrates the containerization and deployment of the **Wisecow Application** on a Kubernetes environment. The implementation includes Dockerization, Kubernetes manifests, a CI/CD pipeline with GitHub Actions, and optional TLS security for secure communication.

---

## Features
- **Dockerized Application**: The Wisecow application is packaged into a Docker container for portability.
- **Kubernetes Deployment**: The app is deployed as a scalable service using Kubernetes.
- **CI/CD Pipeline**: Automates the build, push, and deployment process using GitHub Actions.
- **TLS Security (Optional)**: Ensures secure communication with HTTPS.

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Docker
- Kubernetes (minikube, k3s, or a cloud provider like AWS EKS/GCP GKE)
- kubectl CLI
- Git
- Python (for local development)
- Optional: Cert-Manager for TLS setup

---

## Project Structure

. ├── Dockerfile # Dockerfile to build the application container ├── deployment.yaml # Kubernetes Deployment manifest ├── service.yaml # Kubernetes Service manifest ├── .github/workflows/deploy.yml # GitHub Actions CI/CD workflow ├── app/ # Application source code (Wisecow) └── README.md # Documentation (this file)


---

## Setup Instructions

### Step 1: Clone the Repository
  - git clone https://github.com/your-username/wisecow.git
  - cd wisecow

Step 2: Dockerize the Application
1. Build the Docker image:
  - docker build -t your-dockerhub-username/wisecow:latest .
2. Test the container locally (optional)
  - docker run -p 5000:5000 your-dockerhub-username/wisecow:latest
3.  Push the Docker Image to DockerHub
  - docker push your-dockerhub-username/wisecow:latest

Step 4: Deploy to Kubernetes
1. Apply the deployment manifest:
     - kubectl apply -f deployment.yaml
2. Apply the service manifest:
     - kubectl apply -f service.yaml
3. Verify the Deployment
     - kubectl get pods
     - kubectl get services

Step 5: Set Up CI/CD Pipeline
  1. Add the following secrets to your GitHub repository:
    - DOCKER_USERNAME: Your DockerHub username.
    - DOCKER_PASSWORD: Your DockerHub password.
  2. Push changes to the repository to trigger the pipeline.

CI/CD Workflow Details: 
The GitHub Actions workflow performs the following steps:
1. Builds and pushes the Docker image to DockerHub.
2. Deploys the updated image to the Kubernetes cluster automatically.

