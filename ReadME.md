# 🏡 Smart Home API

## Overview
This project implements a **RESTful API** for managing **Users, Houses, Rooms, and Devices** using Python’s built-in `http.server`. It allows structured interactions via **JSON-based requests** and demonstrates basic API design with **unit testing** and **CI/CD automation**.

## Features
- ✅ **User Management:** Create and retrieve users.  
- ✅ **House Management:** Add and view house details.  
- ✅ **Room Management:** Assign rooms to houses.  
- ✅ **Device Management:** Add smart devices to rooms.  
- ✅ **Error Handling:** Returns structured responses for missing resources.  
- ✅ **Automated Testing:** Uses `pytest` for validation.  
- ✅ **CI/CD Integration:** GitHub Actions for automated testing.  

## Installation & Usage
### Prerequisites
Ensure you have Python installed (version 3.7+ recommended).

### Running the API Server
```sh
python smarthome.py
```
📢 **API will run on:** `http://localhost:8000`

### Running Tests
```sh
pytest test_smarthome.py
```
📢 **Note:** Stop the API (`Ctrl + C`) before running tests.

## API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| `POST` | `/users/`              | Create a user |
| `GET`  | `/users/{id}`          | Get user details |
| `POST` | `/houses/`             | Create a house |
| `GET`  | `/houses/{id}`         | Get house details |
| `POST` | `/houses/{id}/rooms/`  | Add a room to a house |
| `GET`  | `/houses/{id}/rooms/`  | List rooms in a house |
| `POST` | `/rooms/{id}/devices/` | Add a device to a room |
| `GET`  | `/rooms/{id}/devices/` | List devices in a room |

## Configuration
Modify these values in `smarthome.py` as needed:
```python
PORT = 8000  # Change the API's running port
```

## Example Output
Upon running, the API logs its activity:
```
🚀 SmartHome API is now running on port 8000...
POST request received: New user created.
GET request received: Fetching house details.
```

## Project Structure
```
📦 Smart-Home-API---Exercise-2
├── 📄 smarthome.py       # API Implementation
├── 📄 test_smarthome.py  # Unit tests
├── 📄 README.md          # Documentation
└── 📂 .github/workflows/ # GitHub Actions for CI/CD
```

## Notes
- **If an endpoint doesn’t work**, ensure the server is running.  
- **To test new cases**, update `test_smarthome.py`.  
- **For large-scale deployments**, consider replacing `http.server` with **Flask or FastAPI**.  

