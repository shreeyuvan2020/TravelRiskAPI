from fastapi.testclient import TestClient
from main import app
from main import TravelRequest, MultipleTravelRequest
client = TestClient(app)

def test_weather_risk():
    test_data = {
    "destinations": [
        {"season": "Summer", "county": "Los Angeles", "state": "CA"},
        {"season": "Winter", "county": "Miami-Dade", "state": "FL"}
    ]
}

    response = client.post("/custom_travel_risks", json=test_data)
    # Assert the response body matches the expected data
    assert response.status_code == 200
    print(response.json())