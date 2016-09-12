import requests, json

data = {
    "publication_id": 999998,
    "budget_code": None,
}
requests.post("http://127.0.0.1:8080/index/exemption", json.dumps(data))