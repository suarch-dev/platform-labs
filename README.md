# Platform Labs

Welcome to my personal infrastructure and automation lab. This repository serves as a continuous learning workspace where I document my progress, practice new technologies, and build foundational scripts as I transition into a Cloud/DevOps/Platform Engineering role.

## 🎯 Current Progress

### Phase 1: Python for DevOps (Completed)
Development of fundamental automation scripts and API integrations.
*   **01-basics**: Variables, data types, loops, and control flow.
*   **02-flow_control**: Conditional logic and lists.
*   **03-loops**: Iteration and functions.
*   **04-apis**: Consuming REST APIs using `requests` (GET/POST) and handling JSON data.
*   **05-systems**: Interacting with the OS using `subprocess`, parsing system outputs, and error handling (`try/except`).
*   *Note: The final project of this phase (Telegram Alert Bot) has been moved to its own dedicated repository.*

### Phase 2: Linux Administration & Bash Scripting (Completed)
Hands-on practice managing a headless Ubuntu Server via SSH, focusing on system administration and automation.
*   **01-user-management**: Creating users and managing groups (`adduser`, `usermod`).
*   **02-file-permissions**: Managing file access (`chmod`, `chown`).
*   **03-processes-and-logs**: Monitoring processes and reading systemd logs (`ps`, `systemctl`, `journalctl`).
*   **04-networking**: Network interfaces, open ports, and connectivity (`ip a`, `ss`, `curl`, `ping`).
*   **05-bash-scripts**: Automation scripts for directory checks and system maintenance.

### Phase 3: Docker & Containerization (Completed)
Hands-on practice with Docker, moving from basic containerization to multi-container orchestration.
*   **01-hello-world**: Basic Dockerfile and image building.
*   **02-web-api**: Containerizing a Flask web application and mapping ports.
*   **03-volumes**: Data persistence using Docker volumes.
*   **04-docker-compose**: Multi-container orchestration using Docker Compose (Flask + Redis).
*   **05-docker-exam**: Final practical exam. A Flask web app that logs visits to a persistent local file using volumes.

### Phase 4: Kubernetes (Completed)
Deploying and managing containerized applications using a local `k3s` cluster.
*   **01-fundamentals**: Basic Deployments, Services, and ConfigMaps.
*   **02-gateway-api**: Modern ingress routing using NGINX Gateway Fabric.
*   **03-kustomize**: Managing configurations and name prefixes using Kustomize.
*   **04-exam-app**: Final practical exam. A multi-resource deployment demonstrating namespace isolation, resource limits, and Gateway API routing.

## 📂 Repository Structure

*   `01-python-labs/`: Exercises and scripts related to Python automation.
*   `02-docker-labs/`: Dockerfiles, Docker Compose configurations, and containerized applications.
*   `03-linux-labs/`: Documentation and Bash scripts for system administration.
*   `04-kubernetes-labs/`: Kubernetes manifests, Helm, and Kustomize configurations.

## 🛠️ Tech Stack & Tools

*   **Languages**: Python 3, Bash
*   **Infrastructure**: Docker, Docker Compose, Linux (Ubuntu Server)
*   **Orchestration**: Kubernetes (k3s), Helm, Kustomize, Gateway API
*   **Version Control**: Git & GitHub
*   **Environment**: Virtual Environments (`venv`), macOS, UTM

## 🚀 Upcoming Phases (Market-Aligned Roadmap)

*   **Phase 5**: AWS Cloud & Terraform (IaC, VPC, EKS with Pod Identity & Karpenter)
*   **Phase 6**: CI/CD with GitHub Actions (OIDC authentication, SHA-pinned actions)
*   **Phase 7**: Monitoring (`kube-prometheus-stack`) & Certifications (AWS SAA-C03, CKA)
*   **Capstone Project**
