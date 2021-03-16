def test_get_list(client):
    response = client.get("/tenders/list?limit=20")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 20









