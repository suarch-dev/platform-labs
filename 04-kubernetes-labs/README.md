# Kubernetes Labs

This directory documents my hands-on practice with Kubernetes, using a local `k3s` cluster provisioned on a headless Ubuntu Server (UTM).

## 📂 Projects

*   **01-fundamentals**: Basic Deployments, Services, and ConfigMaps (Nginx web server).
*   **02-gateway-api**: Replacing traditional Ingress with the modern Gateway API (NGINX Gateway Fabric).
*   **03-kustomize**: Managing configurations and name prefixes using Kustomize.
*   **04-exam-app**: Final practical exam. A multi-resource deployment demonstrating namespace isolation, custom ConfigMaps, resource limits, and Gateway API routing.

## 🛠️ Core Commands Mastered
*   `kubectl apply -f <file>`: Deploying resources.
*   `kubectl get pods/deployments/svc`: Listing resources.
*   `kubectl describe pod <name>`: Debugging pod events.
*   `kubectl logs <name>`: Viewing container logs.
*   `kubectl exec -it <name> -- <command>`: Executing commands inside a container.
*   `helm install/uninstall`: Managing packages.
