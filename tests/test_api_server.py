from fastapi.testclient import TestClient
from src.control_plane.api_server import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "aws" in data["enabled_providers"]

def test_unified_inventory_endpoint():
    response = client.get("/v1/inventory/unified")
    assert response.status_code == 200
    data = response.json()
    assert data["total_count"] >= 3
    assert "resources" in data

def test_governance_audit_endpoint():
    response = client.get("/v1/governance/audit")
    assert response.status_code == 200
    data = response.json()
    assert data["overall_status"] in ["COMPLIANT", "NON_COMPLIANT"]
    assert "policy_evaluation" in data
