# Docker Labs: Containerization & Orchestration

This repository documents my hands-on practice and progression with Docker, moving from basic containerization to multi-container orchestration. 

## 📂 Repository Structure

*   **01-hello-world**: Basic Dockerfile and image building.
*   **02-web-api**: Containerizing a Flask web application and mapping ports.
*   **03-volumes**: Data persistence using Docker volumes.
*   **04-docker-compose**: Multi-container orchestration using Docker Compose (Flask + Redis).
*   **05-docker-exam**: Final practical exam. A Flask web app that logs visits to a persistent local file using volumes.

## 🛠️ Tech Stack
*   Docker & Docker Compose
*   Python 3 (Flask, Redis)
*   YAML

## 🚀 How to Use
Each folder contains its own `Dockerfile` and/or `docker-compose.yml`. Navigate into any project folder and run `docker compose up` (or `docker build` and `docker run` depending on the exercise) to see it in action.