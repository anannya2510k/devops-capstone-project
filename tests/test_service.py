from service import app


def test_home():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.get("/", base_url="https://localhost")
    assert response.status_code == 200
