from src.adapters.gcp_adapter import GCPAdapter

def test_gcp_inventory():
    adapter = GCPAdapter()
    inventory = adapter.list_inventory()
    assert len(inventory) > 0
    assert inventory[0]["provider"] == "gcp"

def test_gcp_audit():
    adapter = GCPAdapter()
    audit = adapter.audit_security()
    assert audit["compliance_score"] >= 90.0
