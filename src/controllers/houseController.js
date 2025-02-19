// Temporary in-memory storage for houses
const houses = {};

// Create a new house
exports.createHouse = (req, res) => {
    const { name, owner } = req.body; // Extract house name and owner

    // Validate input fields
    if (!name || !owner) {
        return res.status(400).json({ error: 'House name and owner are required' });
    }

    // Generate a unique house ID
    const houseId = Math.random().toString(36).substr(2, 9);

    // Store house in temporary storage
    houses[houseId] = { name, owner };

    res.status(201).json({ message: 'House created successfully', houseId });
};

// Retrieve house details by ID
exports.getHouse = (req, res) => {
    const { houseId } = req.params;

    // Check if the house exists
    if (!houses[houseId]) {
        return res.status(404).json({ error: 'House not found' });
    }

    res.json(houses[houseId]);
};
