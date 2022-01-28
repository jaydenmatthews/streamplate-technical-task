import requests
from restaurants import closest_venues

port = 5000
url = f"http://localhost:{port}/"

# HTTP Error Tests
def test_invalid_lat():
    payload = {
        'latitude' : "invalid",
        'longitude' : "-97.000",
        'limit' : 10
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 400
    
def test_invalid_long():
    payload = {
        'latitude' : "49.000",
        'longitude' : "invalid",
        'limit' : 10
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 400

def test_invalid_limit():
    payload = {
        'latitude' : "49.000",
        'longitude' : "-97.000",
        'limit' : "invalid"
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 400

def test_no_limit():
    payload = {
        'latitude' : "49.000",
        'longitude' : "-97.000",
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 200

def test_none_limit():
    payload = {
        'latitude' : "49.000",
        'longitude' : "-97.000",
        'limit' : None,
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 200

def test_basic():
    payload = {
        'latitude' : "49.000",
        'longitude' : "-97.000",
        'limit' : 3
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 200

def test_no_long():
    payload = {
        'latitude' : "49.000",
        'limit' : 3
    }
    r = requests.get(url + 'restaurants', params = payload)
    assert r.status_code == 400   