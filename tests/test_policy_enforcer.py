from src.governance.policy_enforcer import PolicyEnforcer

def test_policy_enforcer_clean():
    enforcer = PolicyEnforcer()
    sample_inventory = [
        {"id": "res-1", "provider": "aws", "encrypted": True, "region": "us-east-1", "tags": {"Env": "prod"}}
    ]
    report = enforcer.enforce_policies(sample_inventory)
    assert report["total_violations"] == 0
    assert report["overall_compliance_rate"] == 100.0

def test_policy_enforcer_violation():
    enforcer = PolicyEnforcer()
    sample_inventory = [
        {"id": "res-unencrypted", "provider": "gcp", "encrypted": False, "region": "us-central1", "tags": {}}
    ]
    report = enforcer.enforce_policies(sample_inventory)
    assert report["total_violations"] >= 1
    assert report["overall_compliance_rate"] < 100.0
