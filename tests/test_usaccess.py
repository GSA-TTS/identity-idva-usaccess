""" USAccess API unit tests """
from fastapi.testclient import TestClient
from usaccess.main import app

client = TestClient(app)


def test_successful_response():
    """Test successful 200 response from USPS Microservice"""
    response = client.post("/test")
    assert response.status_code == 200
