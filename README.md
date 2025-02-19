# 🏠 Smart Home API

A REST API for managing users, houses, rooms, and devices. Built with **Node.js, Express.js**, tested with **Jest & Supertest**, and automated using **GitHub Actions**.

---

## 🚀 Features

- **User Management** → Create and retrieve users.  
- **House Management** → Create houses and assign owners.  
- **Room Management** → Add rooms inside houses.  
- **Device Control** → Add smart devices to rooms and toggle them on/off.  
- **Validation & Error Handling** → Ensures proper input.  
- **Automated Testing** → Uses Jest and Supertest.  
- **CI/CD with GitHub Actions** → Runs tests on every push.  

---

## 📂 Project Structure

This project follows a modular structure:

```
Smart-Home-API/
├── src/
│   ├── controllers/       # API logic & validation
│   │   ├── userController.js
│   │   ├── houseController.js
│   │   ├── roomController.js
│   │   ├── deviceController.js
│   ├── routes/            # API endpoints
│   │   ├── userRoutes.js
│   │   ├── houseRoutes.js
│   │   ├── roomRoutes.js
│   │   ├── deviceRoutes.js
│   ├── tests/             # Automated tests
│   │   ├── user.test.js
│   │   ├── house.test.js
│   │   ├── room.test.js
│   │   ├── device.test.js
│   ├── server.js          # Main server setup
├── .gitignore             # Ignores node_modules & .env
├── package.json           # Dependencies
├── README.md              # Documentation
└── .github/workflows/     # GitHub Actions for automation
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/phylisscity/Smart-Home-API---Exercise-2.git
cd Smart-Home-API---Exercise-2
```

### 2️⃣ Install Dependencies  
```bash
npm install
```

### 3️⃣ Run the Server  
```bash
npm start
```
The API runs at **`http://localhost:5000`** (Port can be changed in `server.js` if needed).

### 4️⃣ Run Tests  
```bash
npm test
```
Runs unit tests using **Jest & Supertest**.

---

## 📌 API Endpoints  

### 👤 User Endpoints  
| Method | Endpoint     | Description          |
|--------|-------------|----------------------|
| POST   | `/users`    | Create a new user    |
| GET    | `/users/:id`| Retrieve user by ID  |

### 🏠 House Endpoints  
| Method | Endpoint     | Description            |
|--------|-------------|------------------------|
| POST   | `/houses`   | Create a new house     |
| GET    | `/houses/:id` | Retrieve house by ID  |

### 🛋️ Room Endpoints  
| Method | Endpoint          | Description            |
|--------|------------------|------------------------|
| POST   | `/rooms/:houseId` | Add a room to a house |
| GET    | `/rooms/:roomId`  | Retrieve room details |

### 🔌 Device Endpoints  
| Method  | Endpoint                  | Description             |
|---------|--------------------------|-------------------------|
| POST    | `/devices/:roomId`       | Add a device to a room  |
| PATCH   | `/devices/:deviceId/toggle` | Toggle device ON/OFF  |
| GET     | `/devices/:deviceId`     | Retrieve device details |

---

## 🛠️ Design Considerations

### 1️⃣ Why Use a Modular Structure?  
- Organizes code for better **maintainability**.  
- Each feature (**Users, Houses, Rooms, Devices**) has **separate routes and controllers**.  
- Easier to **add new features** without modifying everything.

### 2️⃣ Why Use Jest & Supertest for Testing?  
- **Jest** is **fast** and integrates well with **Node.js**.  
- **Supertest** allows **real HTTP requests** to test endpoints properly.

### 3️⃣ Why is `node_modules/` Not in the Repo?  
- The `node_modules/` folder contains **installed dependencies**.  
- Keeping it in the repo **bloats the project**.  
- Instead, running `npm install` installs dependencies automatically.

---

## ⚠️ Error Handling  

Every request is validated, and errors return structured responses.

### Example: Missing Fields in User Creation  

#### Request (Invalid)
```json
POST /users
{
  "username": "Alice"
}
```

#### Response
```json
{
  "error": "Email is required"
}
```

### Common Errors  
| Status Code | Meaning                | Example Scenario       |
|------------|------------------------|------------------------|
| **400**    | Bad Request (Invalid Input) | Missing required fields |
| **404**    | Not Found               | Invalid user/house ID  |
| **500**    | Internal Server Error   | Unexpected crash       |

---

## 🤖 Automated Testing with GitHub Actions  

GitHub Actions runs automated tests on every push.

### `.github/workflows/test.yml`
```yaml
name: Run API Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      - run: npm install
      - run: npm test
```
✅ **Ensures tests pass before merging changes.**
