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
*   **Lab Setup**: Provisioned a minimal Ubuntu VM using UTM and `cloud-init`.
*   **Users & Permissions**: Managed users, groups, and file permissions (`chmod`, `chown`).
*   **Processes & Logs**: Monitored system processes (`ps`, `systemd`) and analyzed logs (`journalctl`).
*   **Networking**: Checked interfaces, open ports, and connectivity (`ip a`, `ss`, `curl`, `ping`).
*   **Bash Scripting**: Developed automation scripts to check directories and perform system maintenance.

### Phase 3: Docker & Containerization (Completed)
Hands-on practice with Docker, moving from basic containerization to multi-container orchestration.
*   **01-hello-world**: Basic Dockerfile and image building.
*   **02-web-api**: Containerizing a Flask web application and mapping ports.
*   **03-volumes**: Data persistence using Docker volumes.
*   **04-docker-compose**: Multi-container orchestration using Docker Compose (Flask + Redis).
*   **05-docker-exam**: Final practical exam. A Flask web app that logs visits to a persistent local file using volumes.

## 📂 Repository Structure

*   `python-labs/`: Exercises and scripts related to Python automation.
*   `linux-labs/`: Bash scripts for system administration and maintenance.
*   `docker-labs/`: Dockerfiles, Docker Compose configurations, and containerized applications.

## 🛠️ Tech Stack & Tools

*   **Languages**: Python 3, Bash
*   **Infrastructure**: Docker, Docker Compose, Linux (Ubuntu Server)
*   **Version Control**: Git & GitHub
*   **Environment**: Virtual Environments (`venv`), macOS, UTM

## 🚀 Upcoming Phases

*   **Phase 4**: Kubernetes (Pods, Deployments, Services, Helm, Gateway API)
*   **Phase 5**: AWS Cloud & Terraform (IaC, VPC, EKS with Pod Identity & Karpenter)
*   **Phase 6**: CI/CD with GitHub Actions (OIDC authentication, SHA-pinned actions)
*   **Phase 7**: Monitoring (kube-prometheus-stack) & Certifications (AWS SAA-C03, CKA)
*   **Capstone Project**: Full-stack deployment on AWS EKS with automated CI/CD and monitoring.