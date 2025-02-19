const express = require('express');
const { addDevice, toggleDevice, getDevice } = require('../controllers/deviceController'); // Ensure getDevice is included

const router = express.Router();

// Route for adding a new device to a room
router.post('/:roomId', addDevice);

// Route for retrieving device details by ID (This was broken)
router.get('/:deviceId', getDevice); // Ensure getDevice is imported correctly

// Route for toggling a device ON/OFF
router.patch('/:deviceId/toggle', toggleDevice);

module.exports = router;
