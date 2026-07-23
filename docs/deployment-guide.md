# Deployment Guide: Multi-Cloud Control Plane

This guide covers deployment options for the Multi-Cloud Control Plane platform.

## 1. Local Development Setup

```bash
# Clone repository
git clone https://github.com/Devopstrio/multicloud-control-plane.git
cd multicloud-control-plane

# Install dependencies
pip install -r requirements.txt

# Launch Control Plane API
uvicorn src.control_plane.api_server:app --reload --port 8000
```

## 2. Docker Container Deployment

```bash
# Start container stack
docker-compose up -d --build

# Verify API health
curl http://localhost:8000/healthz
```

## 3. Terraform Multi-Cloud Landing Zone Provisioning

```bash
# Deploy AWS Landing Zone Hub
cd terraform/aws
terraform init && terraform apply -auto-approve

# Deploy Azure Landing Zone Hub
cd ../azure
terraform init && terraform apply -auto-approve

# Deploy GCP Landing Zone Hub
cd ../gcp
terraform init && terraform apply -auto-approve
```
