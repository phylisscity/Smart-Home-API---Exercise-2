const express = require('express');
const { addRoom, getRoom } = require('../controllers/roomController');

const router = express.Router();

// Route for adding a new room to a house
router.post('/:houseId', addRoom);

// Route for retrieving room details by ID
router.get('/:roomId', getRoom);

module.exports = router;
