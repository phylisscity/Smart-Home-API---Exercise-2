const request = require('supertest'); // Supertest is used to simulate API requests
const app = require('../server'); // Import the main server

describe('House API Tests', () => {
    let server;
    let api;

    // Start the server before running tests (assign a free port dynamically)
    beforeAll((done) => {
        server = app.listen(0, () => { // `0` allows the OS to assign an available port
            const port = server.address().port; // Retrieve the assigned port
            api = request(`http://localhost:${port}`); // Update API request target to the assigned port
            done();
        });
    });

    // Close the server after all tests to free up the port
    afterAll((done) => {
        server.close(done);
    });

    // Test: Creating a house should return 201 and include a houseId
    it('Should create a house successfully', async () => {
        const res = await api.post('/houses').send({ name: 'Dream Home', owner: 'John Doe' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('houseId');
    });

    // Test: Missing required fields should return a 400 error
    it('Should return 400 if house name or owner is missing', async () => {
        const res = await api.post('/houses').send({ name: 'Dream Home' });
        expect(res.statusCode).toEqual(400);
    });
});
