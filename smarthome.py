import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# -------------------------------
# In-Memory Data Storage (Stub)
# -------------------------------
users_db = {}     # Stores user data
houses_db = {}    # Stores house data
rooms_db = {}     # Stores room data (grouped by house_id)
devices_db = {}   # Stores devices data (grouped by room_id)



class RESTfulAPIHandler(BaseHTTPRequestHandler):
    
    """
    Handles all incoming HTTP requests for our SmartHome API.
    Supports basic CRUD operations for Users, Houses, Rooms, and Devices.
    """

    def _send_response(self, response_data, status=200):
        """ Helper function to send JSON responses."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=4).encode("utf-8"))



    # -------------------------------
    #  Handle POST Requests (Create)
    # -------------------------------
    def do_POST(self):
        """Handles creating Users, Houses, Rooms, and Devices."""
        
        content_length = int(self.headers['Content-Length'])  # Get request body size
        post_data = self.rfile.read(content_length)  # Read the request body
        data = json.loads(post_data)  # Convert JSON string into a Python dictionary

        #  Create a new User
        if self.path == "/users/":
            user_id = len(users_db) + 1
            users_db[user_id] = data
            self._send_response({"user_id": user_id, "message": "User created!"}, 201)

        #  Create a new House
        elif self.path == "/houses/":
            house_id = len(houses_db) + 1
            houses_db[house_id] = data
            self._send_response({"house_id": house_id, "message": "House created!"}, 201)

        #  Add a new Room to a House
        elif self.path.startswith("/houses/") and "/rooms/" in self.path:
            house_id = int(self.path.split("/")[2])

            if house_id not in houses_db:
                self._send_response({"error": "House not found"}, 404)
                return

            room_id = len(rooms_db) + 1
            if house_id not in rooms_db:
                rooms_db[house_id] = []  # Initialize empty room list for this house

            rooms_db[house_id].append({"room_id": room_id, **data})
            self._send_response({"room_id": room_id, "message": "Room added!"}, 201)

        #  Add a new Smart Device to a Room
        elif self.path.startswith("/rooms/") and "/devices/" in self.path:
            room_id = int(self.path.split("/")[2])

            if room_id not in rooms_db:
                self._send_response({"error": "Room not found"}, 404)
                return

            device_id = len(devices_db) + 1
            if room_id not in devices_db:
                devices_db[room_id] = []  # Initialize empty device list for this room

            devices_db[room_id].append({"device_id": device_id, **data})
            self._send_response({"device_id": device_id, "message": "Device added!"}, 201)




    # -------------------------------
    #  Handle GET Requests (Retrieve)
    # -------------------------------
    def do_GET(self):
        """Handles retrieving Users, Houses, Rooms, and Devices."""

        #  Retrieve User details
        if self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[2])

            if user_id not in users_db:
                self._send_response({"error": "User not found"}, 404)
                return

            self._send_response({"user_id": user_id, **users_db[user_id]})

        #  Retrieve House details
        elif self.path.startswith("/houses/") and "/rooms/" not in self.path:
            house_id = int(self.path.split("/")[2])

            if house_id not in houses_db:
                self._send_response({"error": "House not found"}, 404)
                return

            self._send_response({"house_id": house_id, **houses_db[house_id]})

        #  List all Rooms in a House
        elif self.path.startswith("/houses/") and "/rooms/" in self.path:
            house_id = int(self.path.split("/")[2])

            if house_id not in houses_db:
                self._send_response([])  # Instead of 404, return an empty list
                return

            self._send_response(rooms_db.get(house_id, []))

        #  List all Smart Devices in a Room
        elif self.path.startswith("/rooms/") and "/devices/" in self.path:
            room_id = int(self.path.split("/")[2])

            if room_id not in rooms_db:
                self._send_response([])  # Instead of 404, return an empty list
                return

            self._send_response(devices_db.get(room_id, []))




# -------------------------------
#  Run the API Server
# -------------------------------
if __name__ == "__main__":
    #  Running the API server locally on port 8000
    # You can access the API by making requests to http://localhost:8000/
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RESTfulAPIHandler)
    print(" SmartHome API is now running on port 8000...")
    print(" Stop the server with Ctrl + C, then run tests with: `pytest test_smarthome.py`")
    httpd.serve_forever()
