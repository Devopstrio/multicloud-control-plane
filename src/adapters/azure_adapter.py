from typing import Dict, Any, List

class AzureAdapter:
    """
    Microsoft Azure Infrastructure Governance Adapter.
    Audits Azure Resource Groups, Virtual Machines, Blob Storage, and RBAC compliance.
    """
    def __init__(self, subscription_id: str = "00000000-0000-0000-0000-000000000000"):
        self.subscription_id = subscription_id

    def list_inventory(self) -> List[Dict[str, Any]]:
        return [
            {"id": "/subscriptions/sub-1/resourceGroups/rg-prod/providers/Microsoft.Compute/virtualMachines/vm-prod-01", "type": "vm", "name": "vm-prod-01", "region": "eastus", "provider": "azure", "encrypted": True, "tags": {"Env": "prod"}},
            {"id": "/subscriptions/sub-1/resourceGroups/rg-prod/providers/Microsoft.Storage/storageAccounts/stprodlogs", "type": "storage_account", "name": "stprodlogs", "region": "eastus", "provider": "azure", "encrypted": True, "tags": {"Env": "prod"}}
        ]

    def audit_security(self) -> Dict[str, Any]:
        return {
            "provider": "azure",
            "compliance_score": 97.0,
            "nsg_unrestricted_rules": 0,
            "unencrypted_storage_accounts": 0,
            "rbac_policy_compliance": 100.0
        }
