# Multi-Cloud Control Plane Architecture

The **Multi-Cloud Control Plane** provides a unified API, inventory aggregation, policy enforcement, and infrastructure control hub across Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

![Multi-Cloud Control Plane Architecture](images/architecture_diagram.jpg)

## Component Breakdown

1. **Central Control Plane API (`src/control_plane/api_server.py`)**
   - Serves unified endpoints for cross-cloud inventory retrieval and governance reports.
   - Aggregates resource state across all configured cloud providers.

2. **Cloud Provider Adapters (`src/adapters/`)**
   - `aws_adapter.py`: Interfaces with AWS APIs (EC2, S3, IAM, Security Groups).
   - `azure_adapter.py`: Interfaces with Azure Resource Manager (VMs, Storage Accounts, NSGs).
   - `gcp_adapter.py`: Interfaces with GCP Resource Manager (Compute Engine, GCS, VPC Firewalls).

3. **Unified Policy Enforcer (`src/governance/policy_enforcer.py`)**
   - Scans multi-cloud inventories against enterprise compliance guardrails.
   - Enforces mandatory encryption at rest, region locks, and tagging compliance.

4. **Multi-Cloud Infrastructure Modules (`terraform/`)**
   - Modular Landing Zone definitions for AWS VPC Hubs, Azure Resource Groups, GCP Virtual Networks, and Crossplane CRDs.
