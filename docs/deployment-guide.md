# Deployment Guide: Multi-Cloud Control Plane

This document provides step-by-step instructions to deploy the Multi-Cloud Control Plane service locally, via Docker, and onto cloud infrastructure using Terraform.

## 1. Local Development Setup

```bash
# Clone repository
git clone https://github.com/Devopstrio/multicloud-control-plane.git
cd multicloud-control-plane

# Create Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run pytest suite
python -m pytest -v tests/

# Launch Control Plane API Server
uvicorn src.control_plane.api_server:app --reload --host 0.0.0.0 --port 8000
```

## 2. Docker & Container Orchestration

```bash
# Build and run container stack
docker-compose up -d --build

# Verify container health status
docker-compose ps
curl http://localhost:8000/healthz
```

## 3. Terraform Infrastructure Provisioning

```bash
# Deploy AWS Landing Zone Network Hub
cd terraform/aws
terraform init
terraform plan
terraform apply -auto-approve

# Deploy Azure Landing Zone Hub
cd ../azure
terraform init
terraform apply -auto-approve

# Deploy GCP Landing Zone Hub
cd ../gcp
terraform init
terraform apply -auto-approve
```
