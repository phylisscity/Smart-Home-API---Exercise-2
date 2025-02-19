// Temporary in-memory storage for users (simulates a database)
const users = {};

// Create a new user
exports.createUser = (req, res) => {
    const { username, email } = req.body; // Extract username and email from request

    // Validate input fields
    if (!username || !email) {
        return res.status(400).json({ error: 'Username and email are required' });
    }

    // Generate a unique user ID (random string)
    const userId = Math.random().toString(36).substr(2, 9);

    // Store user in temporary storage
    users[userId] = { username, email };

    res.status(201).json({ message: 'User created successfully', userId });
};

// Retrieve user details by ID
exports.getUser = (req, res) => {
    const { userId } = req.params; // Extract user ID from request parameters

    // Check if the user exists
    if (!users[userId]) {
        return res.status(404).json({ error: 'User not found' });
    }

    res.json(users[userId]); // Return user details
};
