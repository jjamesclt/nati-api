# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenSSL for certificate generation
RUN apt-get update && apt-get install -y openssl && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Ensure script has execution permissions
RUN chmod +x /app/generate-csr.sh

# Create cert directory
RUN mkdir -p /certs

# Default port for Flask with HTTPS (internal)
EXPOSE 5000

# Command to run the app
CMD ["python", "run.py"]
