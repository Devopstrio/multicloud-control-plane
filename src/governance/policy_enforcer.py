from typing import List, Dict, Any, Optional

class PolicyEnforcer:
    """
    Unified Cross-Cloud Governance Policy Engine.
    Enforces organizational security guardrails (encryption at rest, region locks, mandatory tagging)
    across heterogeneous multi-cloud environments.
    """

    def __init__(self, allowed_regions: Optional[List[str]] = None):
        self.allowed_regions = allowed_regions or [
            "us-east-1", "us-central1", "eastus", "eu-west-1", "us-west-2"
        ]

    def enforce_policies(self, inventory: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Scans multi-cloud resource inventory against enterprise compliance policies.
        Returns detailed compliance metrics and policy violation objects.
        """
        violations: List[Dict[str, Any]] = []
        compliant_resources: List[str] = []

        for resource in inventory:
            res_id = resource.get("id", "unknown-resource")
            provider = resource.get("provider", "unknown-provider")
            encrypted = resource.get("encrypted", False)
            region = resource.get("region", "unknown")
            tags = resource.get("tags", {})

            res_violations = []

            # Rule 1: Mandatory Encryption at Rest
            if not encrypted:
                v = {
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "MANDATORY_ENCRYPTION_AT_REST",
                    "severity": "CRITICAL",
                    "description": "Resource lacks required cloud storage/disk encryption."
                }
                violations.append(v)
                res_violations.append(v)

            # Rule 2: Geographic Region Lock
            if region not in self.allowed_regions:
                v = {
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "UNAUTHORIZED_GEOGRAPHIC_REGION",
                    "severity": "HIGH",
                    "description": f"Resource deployed in non-approved region '{region}'."
                }
                violations.append(v)
                res_violations.append(v)

            # Rule 3: Mandatory Tagging Standard ('Env' tag required)
            if "Env" not in tags:
                v = {
                    "resource_id": res_id,
                    "provider": provider,
                    "rule": "MISSING_MANDATORY_TAG_ENV",
                    "severity": "MEDIUM",
                    "description": "Resource missing mandatory governance tag 'Env'."
                }
                violations.append(v)
                res_violations.append(v)

            if len(res_violations) == 0:
                compliant_resources.append(res_id)

        compliance_rate = round((len(compliant_resources) / len(inventory) * 100), 2) if inventory else 100.0

        return {
            "total_resources_audited": len(inventory),
            "compliant_resources": len(compliant_resources),
            "total_violations": len(violations),
            "overall_compliance_rate": compliance_rate,
            "violations": violations
        }
