// Temporary in-memory storage for rooms
const rooms = {};

// Add a new room to a house
exports.addRoom = (req, res) => {
    const { houseId } = req.params; // Extract house ID from request
    const { name } = req.body; // Extract room name from request body

    // Validate input fields
    if (!name) {
        return res.status(400).json({ error: 'Room name is required' });
    }

    // Generate a unique room ID
    const roomId = Math.random().toString(36).substr(2, 9);

    // Store room in temporary storage
    rooms[roomId] = { name, houseId };

    res.status(201).json({ message: 'Room added successfully', roomId });
};

// Retrieve room details by ID
exports.getRoom = (req, res) => {
    const { roomId } = req.params;

    // Check if the room exists
    if (!rooms[roomId]) {
        return res.status(404).json({ error: 'Room not found' });
    }

    res.json(rooms[roomId]);
};
