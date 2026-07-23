from src.adapters.aws_adapter import AWSAdapter

def test_aws_inventory():
    adapter = AWSAdapter()
    inventory = adapter.list_inventory()
    assert len(inventory) > 0
    assert inventory[0]["provider"] == "aws"

def test_aws_audit():
    adapter = AWSAdapter()
    audit = adapter.audit_security()
    assert audit["compliance_score"] >= 90.0
