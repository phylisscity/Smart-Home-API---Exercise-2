const express = require('express');
const { createUser, getUser } = require('../controllers/userController');

const router = express.Router();

// Route for creating a new user
router.post('/', createUser); 

// Route for retrieving user details by ID
router.get('/:userId', getUser);

module.exports = router;
