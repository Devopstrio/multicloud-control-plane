import os
from pydantic import BaseModel
from typing import List

class MultiCloudConfig(BaseModel):
    app_name: str = "Multi-Cloud Governance Control Plane"
    environment: str = os.getenv("ENVIRONMENT", "production")
    
    # Supported Cloud Providers
    enabled_providers: List[str] = ["aws", "azure", "gcp"]
    
    # AWS Settings
    aws_default_region: str = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    
    # Azure Settings
    azure_subscription_id: str = os.getenv("AZURE_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")
    
    # GCP Settings
    gcp_project_id: str = os.getenv("GCP_PROJECT_ID", "devopstrio-multicloud-prod")

config = MultiCloudConfig()
