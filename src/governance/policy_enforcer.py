from typing import List, Dict, Any

class PolicyEnforcer:
    """
    Unified Cross-Cloud Governance Policy Engine.
    Enforces compliance policies (encryption, tagging, region restrictions) across AWS, Azure, & GCP.
    """

    def __init__(self, allowed_regions: List[str] = None):
        self.allowed_regions = allowed_regions or ["us-east-1", "us-central1", "eastus", "eu-west-1"]

    def enforce_policies(self, inventory: List[Dict[str, Any]]) -> Dict[str, Any]:
        violations = []
        compliant_resources = []

        for resource in inventory:
            res_id = resource.get("id")
            provider = resource.get("provider")
            encrypted = resource.get("encrypted", False)
            region = resource.get("region")
            tags = resource.get("tags", {})

            # Rule 1: Mandatory Encryption at Rest
            if not encrypted:
                violations.append({
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "MANDATORY_ENCRYPTION_AT_REST",
                    "severity": "CRITICAL"
                })

            # Rule 2: Region Restrictions
            if region not in self.allowed_regions:
                violations.append({
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "UNAUTHORIZED_GEOGRAPHIC_REGION",
                    "severity": "HIGH"
                })

            # Rule 3: Environment Tag Requirement
            if "Env" not in tags:
                violations.append({
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "MISSING_MANDATORY_TAG_ENV",
                    "severity": "MEDIUM"
                })

            if len([v for v in violations if v["resource_id"] == res_id]) == 0:
                compliant_resources.append(res_id)

        compliance_rate = round((len(compliant_resources) / len(inventory) * 100), 2) if inventory else 100.0

        return {
            "total_resources_audited": len(inventory),
            "compliant_resources": len(compliant_resources),
            "total_violations": len(violations),
            "overall_compliance_rate": compliance_rate,
            "violations": violations
        }
