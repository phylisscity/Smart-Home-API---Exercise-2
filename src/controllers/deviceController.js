// Temporary in-memory storage for devices
const devices = {};

// Function to add a device
exports.addDevice = (req, res) => {
    const { roomId } = req.params;
    const { name, type } = req.body;

    if (!name || !type) {
        return res.status(400).json({ error: 'Device name and type are required' });
    }

    const deviceId = Math.random().toString(36).substr(2, 9);
    devices[deviceId] = { name, type, status: 'OFF', roomId };

    res.status(201).json({ message: 'Device added successfully', deviceId });
};

// Function to get a device by ID (This was missing)
exports.getDevice = (req, res) => {
    const { deviceId } = req.params;

    if (!devices[deviceId]) {
        return res.status(404).json({ error: 'Device not found' });
    }

    res.json(devices[deviceId]);
};

// Function to toggle device ON/OFF
exports.toggleDevice = (req, res) => {
    const { deviceId } = req.params;

    if (!devices[deviceId]) {
        return res.status(404).json({ error: 'Device not found' });
    }

    devices[deviceId].status = devices[deviceId].status === 'OFF' ? 'ON' : 'OFF';

    res.json({ message: `Device toggled successfully! Current status: ${devices[deviceId].status}` });
};
