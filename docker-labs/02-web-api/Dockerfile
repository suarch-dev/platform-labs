# 1. Base image
FROM python:3.14-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy only the requirements file first
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY web_app.py .

# 6. Document the port
EXPOSE 5000

# 7. Run the application
CMD ["python", "web_app.py"]