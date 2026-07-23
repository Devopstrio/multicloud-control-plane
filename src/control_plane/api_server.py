from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List

from src.adapters.aws_adapter import AWSAdapter
from src.adapters.azure_adapter import AzureAdapter
from src.adapters.gcp_adapter import GCPAdapter
from src.governance.policy_enforcer import PolicyEnforcer
from src.config import config

app = FastAPI(
    title="Multi-Cloud Control Plane API",
    description="Unified Enterprise Governance & Policy Hub for AWS, Azure, & GCP",
    version="1.0.0"
)

aws = AWSAdapter(region=config.aws_default_region)
azure = AzureAdapter(subscription_id=config.azure_subscription_id)
gcp = GCPAdapter(project_id=config.gcp_project_id)
enforcer = PolicyEnforcer()


@app.get("/healthz")
def health_check():
    return {
        "status": "healthy",
        "service": config.app_name,
        "enabled_providers": config.enabled_providers
    }


@app.get("/v1/inventory/unified")
def get_unified_inventory():
    """
    Returns aggregated resource inventory across AWS, Azure, and GCP.
    """
    aws_resources = aws.list_inventory()
    azure_resources = azure.list_inventory()
    gcp_resources = gcp.list_inventory()

    combined_inventory = aws_resources + azure_resources + gcp_resources
    return {
        "total_count": len(combined_inventory),
        "providers": {
            "aws": len(aws_resources),
            "azure": len(azure_resources),
            "gcp": len(gcp_resources)
        },
        "resources": combined_inventory
    }


@app.get("/v1/governance/audit")
def run_governance_audit():
    """
    Runs multi-cloud compliance and policy evaluation audit.
    """
    aws_inventory = aws.list_inventory()
    azure_inventory = azure.list_inventory()
    gcp_inventory = gcp.list_inventory()
    
    total_inventory = aws_inventory + azure_inventory + gcp_inventory
    policy_report = enforcer.enforce_policies(total_inventory)

    provider_audits = {
        "aws": aws.audit_security(),
        "azure": azure.audit_security(),
        "gcp": gcp.audit_security()
    }

    return {
        "overall_status": "COMPLIANT" if policy_report["total_violations"] == 0 else "NON_COMPLIANT",
        "policy_evaluation": policy_report,
        "provider_scores": provider_audits
    }
