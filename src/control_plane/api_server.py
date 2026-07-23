from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List

from src.adapters.aws_adapter import AWSAdapter
from src.adapters.azure_adapter import AzureAdapter
from src.adapters.gcp_adapter import GCPAdapter
from src.governance.policy_enforcer import PolicyEnforcer
from src.config import config

app = FastAPI(
    title="Multi-Cloud Control Plane API",
    description="Unified Enterprise Control Plane & Governance Hub for AWS, Azure, & GCP",
    version="1.0.0"
)

# Initialize Provider Adapters
aws = AWSAdapter(region=config.aws_default_region)
azure = AzureAdapter(subscription_id=config.azure_subscription_id)
gcp = GCPAdapter(project_id=config.gcp_project_id)
enforcer = PolicyEnforcer()


class HealthResponse(BaseModel):
    status: str
    service: str
    enabled_providers: List[str]


class UnifiedInventoryResponse(BaseModel):
    total_count: int
    providers: Dict[str, int]
    resources: List[Dict[str, Any]]


class AuditResponse(BaseModel):
    overall_status: str
    policy_evaluation: Dict[str, Any]
    provider_scores: Dict[str, Any]


@app.get("/healthz", response_model=HealthResponse)
def health_check():
    """
    Health check endpoint returning control plane status and active cloud providers.
    """
    return HealthResponse(
        status="healthy",
        service=config.app_name,
        enabled_providers=config.enabled_providers
    )


@app.get("/v1/inventory/unified", response_model=UnifiedInventoryResponse)
def get_unified_inventory():
    """
    Retrieves consolidated resource inventory across AWS, Azure, and GCP.
    """
    try:
        aws_resources = aws.list_inventory()
        azure_resources = azure.list_inventory()
        gcp_resources = gcp.list_inventory()

        combined = aws_resources + azure_resources + gcp_resources
        return UnifiedInventoryResponse(
            total_count=len(combined),
            providers={
                "aws": len(aws_resources),
                "azure": len(azure_resources),
                "gcp": len(gcp_resources)
            },
            resources=combined
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to aggregate multi-cloud inventory: {str(e)}")


@app.get("/v1/governance/audit", response_model=AuditResponse)
def run_governance_audit():
    """
    Executes real-time multi-cloud compliance and policy evaluation audit.
    """
    try:
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

        overall_status = "COMPLIANT" if policy_report["total_violations"] == 0 else "NON_COMPLIANT"

        return AuditResponse(
            overall_status=overall_status,
            policy_evaluation=policy_report,
            provider_scores=provider_audits
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Governance audit failed: {str(e)}")
