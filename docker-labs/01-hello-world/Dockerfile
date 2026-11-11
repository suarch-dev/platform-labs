# 1. Use the official Python slim image as the base
FROM python:3.14-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local app.py into the container's working directory
COPY app.py .

# 4. Execute the script when the container starts
CMD ["python", "app.py"]