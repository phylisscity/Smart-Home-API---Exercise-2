// Import required modules
const express = require('express'); // Framework for handling API requests
const cors = require('cors'); // Middleware for handling cross-origin requests

// Import API routes for different entities
const userRoutes = require('./routes/userRoutes'); 
const houseRoutes = require('./routes/houseRoutes'); 
const roomRoutes = require('./routes/roomRoutes'); 
const deviceRoutes = require('./routes/deviceRoutes'); 

// Initialize the Express application
const app = express();
app.use(express.json()); // Enables JSON parsing for incoming requests
app.use(cors()); // Allows API access from different frontend applications

// Define API routes for each module
app.use('/users', userRoutes); // Routes for user management
app.use('/houses', houseRoutes); // Routes for handling houses
app.use('/rooms', roomRoutes); // Routes for managing rooms inside houses
app.use('/devices', deviceRoutes); // Routes for controlling smart devices

// Start the server only if not in a test environment (prevents conflicts in testing)
if (process.env.NODE_ENV !== 'test') {
    const PORT = process.env.PORT || 5000; // Set server port (default: 5000)
    app.listen(PORT, () => console.log(`Server running on port ${PORT}`)); // Log server status
}

// Export app for testing purposes
module.exports = app;
