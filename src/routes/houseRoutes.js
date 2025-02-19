const express = require('express');
const { createHouse, getHouse } = require('../controllers/houseController');

const router = express.Router();

// Route for creating a new house
router.post('/', createHouse);

// Route for retrieving house details by ID
router.get('/:houseId', getHouse);

module.exports = router;
