from fastapi.testclient import TestClient
from app import app 
client = TestClient(app)
def test_largest_rectangle():
    response = client.post(
        "/largest-rectangle",
        json={
            "matrix": [
                [1, 1, 1, 0, 1, -9],
                [1, 1, 1, 1, 2, -9],
                [1, 1, 1, 1, 2, -9],
                [1, 0, 0, 0, 5, -9],
                [5, 0, 0, 0, 5]
            ]
        }
    )
    assert response.status_code == 200
    assert response.json()["number"] == 1
    assert response.json()["area"] == 8
