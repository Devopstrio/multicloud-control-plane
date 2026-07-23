import os
from pydantic import BaseModel, Field
from typing import List

class MultiCloudConfig(BaseModel):
    """
    Central Configuration Model for Multi-Cloud Control Plane.
    Manages provider API settings, region locks, and compliance standards.
    """
    app_name: str = Field("Multi-Cloud Governance Control Plane", description="Control Plane Application Name")
    environment: str = Field(default_factory=lambda: os.getenv("ENVIRONMENT", "production"))
    debug: bool = Field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
    
    # Supported Cloud Providers
    enabled_providers: List[str] = Field(["aws", "azure", "gcp"], description="Active Cloud Providers")
    
    # AWS Governance Settings
    aws_default_region: str = Field(default_factory=lambda: os.getenv("AWS_DEFAULT_REGION", "us-east-1"))
    aws_allowed_regions: List[str] = Field(["us-east-1", "us-west-2", "eu-west-1"])
    
    # Azure Governance Settings
    azure_subscription_id: str = Field(default_factory=lambda: os.getenv("AZURE_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000"))
    azure_allowed_locations: List[str] = Field(["eastus", "westus2", "westeurope"])
    
    # GCP Governance Settings
    gcp_project_id: str = Field(default_factory=lambda: os.getenv("GCP_PROJECT_ID", "devopstrio-multicloud-prod"))
    gcp_allowed_regions: List[str] = Field(["us-central1", "us-east4", "europe-west1"])

config = MultiCloudConfig()
