from src.adapters.azure_adapter import AzureAdapter

def test_azure_inventory():
    adapter = AzureAdapter()
    inventory = adapter.list_inventory()
    assert len(inventory) > 0
    assert inventory[0]["provider"] == "azure"

def test_azure_audit():
    adapter = AzureAdapter()
    audit = adapter.audit_security()
    assert audit["compliance_score"] >= 90.0
