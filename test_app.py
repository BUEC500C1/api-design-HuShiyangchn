def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'ok'