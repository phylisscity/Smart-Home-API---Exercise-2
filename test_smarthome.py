import json
import pytest
import threading
from http.server import HTTPServer
from urllib.request import urlopen, Request
from smarthome import RESTfulAPIHandler


# -------------------------------
# Important: Start the API Server First! 
# -------------------------------
# Before running these tests, make sure the API server is up and running.
# Open a terminal and start the server with:
#
#     python smarthome.py
#
# If the API server isn’t running, these tests will fail because they can't connect.
# -------------------------------

# -------------------------------
# 🌍 Localhost Testing:
# -------------------------------
# We’re testing this API locally using `http://localhost:8001/`meaning this API is only available on your machine while the server is running.
# In a real-world project, you’d replace this with a live API (e.g., `https://api.example.com`).
# -------------------------------



# -------------------------------
# Setting Up the API Test Server
# -------------------------------
@pytest.fixture(scope="module")
def api_server():
    """Start a local test server before running tests."""
    
    # Start the API server in a separate thread so tests can run alongside it
    server = HTTPServer(('', 8001), RESTfulAPIHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True  # This keeps the thread from blocking everything else
    server_thread.start()
    
    yield  # This allows the tests to run while the server is active
    
    # Shutdown server after tests complete
    server.shutdown()
    server_thread.join()




# -------------------------------
#  User API Tests
# -------------------------------
def test_create_user(api_server):
    """Test adding a user to the system"""
    
    data = json.dumps({"name": "Alice", "email": "alice@example.com"}).encode("utf-8")
    req = Request("http://localhost:8001/users/", data=data, method="POST", headers={"Content-Type": "application/json"})
    
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 201
    assert "user_id" in response_data
    assert response_data["message"] == "User created!"


def test_get_existing_user(api_server):
    """Test retrieving a user that exists"""
    
    req = Request("http://localhost:8001/users/1", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert response_data["user_id"] == 1


def test_get_nonexistent_user(api_server):
    """Test what happens when trying to get a user that doesn’t exist"""
    
    req = Request("http://localhost:8001/users/999", method="GET")

    try:
        response = urlopen(req)
    except Exception as e:
        assert "HTTP Error 404" in str(e)




# -------------------------------
#  House API Tests
# -------------------------------
def test_create_house(api_server):
    """Test adding a house to the system"""
    
    data = json.dumps({"owner_id": 1, "address": "123 Main St"}).encode("utf-8")
    req = Request("http://localhost:8001/houses/", data=data, method="POST", headers={"Content-Type": "application/json"})
    
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 201
    assert "house_id" in response_data
    assert response_data["message"] == "House created!"


def test_get_existing_house(api_server):
    """Test retrieving a house that exists"""
    
    req = Request("http://localhost:8001/houses/1", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert response_data["house_id"] == 1


def test_get_nonexistent_house(api_server):
    """Test what happens when trying to get a house that doesn’t exist"""
    
    req = Request("http://localhost:8001/houses/999", method="GET")

    try:
        response = urlopen(req)
    except Exception as e:
        assert "HTTP Error 404" in str(e)





# -------------------------------
# Room API Tests
# -------------------------------
def test_create_room(api_server):
    """Test adding a room to a house"""
    
    data = json.dumps({"room_name": "Living Room"}).encode("utf-8")
    req = Request("http://localhost:8001/houses/1/rooms/", data=data, method="POST", headers={"Content-Type": "application/json"})
    
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 201
    assert "room_id" in response_data
    assert response_data["message"] == "Room added!"


def test_get_all_rooms_in_house(api_server):
    """Test retrieving all rooms for a specific house"""
    
    req = Request("http://localhost:8001/houses/1/rooms/", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert isinstance(response_data, list)


def test_get_rooms_in_nonexistent_house(api_server):
    """Test retrieving rooms from a house that doesn't exist"""
    
    req = Request("http://localhost:8001/houses/999/rooms/", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert response_data == []  # Should return an empty list, not an error




# -------------------------------
#  Device API Tests
# -------------------------------
def test_add_device_to_room(api_server):
    """Test adding a smart device to a room"""
    
    data = json.dumps({"device_name": "Smart Light"}).encode("utf-8")
    req = Request("http://localhost:8001/rooms/1/devices/", data=data, method="POST", headers={"Content-Type": "application/json"})
    
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 201
    assert "device_id" in response_data
    assert response_data["message"] == "Device added!"


def test_get_all_devices_in_room(api_server):
    """Test retrieving all devices in a room"""
    
    req = Request("http://localhost:8001/rooms/1/devices/", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert isinstance(response_data, list)


def test_get_devices_in_nonexistent_room(api_server):
    """Test retrieving devices from a room that doesn’t exist"""
    
    req = Request("http://localhost:8001/rooms/999/devices/", method="GET")
    response = urlopen(req)
    response_data = json.loads(response.read())

    assert response.getcode() == 200
    assert response_data == []  # Should return an empty list




# -------------------------------
# Running the Tests
# -------------------------------
if __name__ == "__main__":
    pytest.main()
