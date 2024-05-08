from fastapi.testclient import TestClient
import json
from main import app


client = TestClient(app)

def test_post_data_success():
    data = {"feature_1" : 0.5, "feature_2" : "parameter"}
    r = client.post("/data/", data=json.dumps(data))
    print(r.json())
    assert r.status_code == 200

def test_post_data_failure():
    data = {"feature_1" : -2, "feature_2" : "parameter"}
    r = client.post("/data/", data=json.dumps(data))
    print(r.json())
    assert r.status_code == 400