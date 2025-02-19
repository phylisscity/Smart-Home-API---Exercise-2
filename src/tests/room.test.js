const request = require('supertest');
const app = require('../server');

describe('Room API Tests', () => {
    let server;
    let api;

    // Start the server before running tests (assign a free port dynamically)
    beforeAll((done) => {
        server = app.listen(0, () => {
            const port = server.address().port;
            api = request(`http://localhost:${port}`);
            done();
        });
    });

    // Close the server after tests to free up the port
    afterAll((done) => {
        server.close(done);
    });

    // Test: Adding a room should return 201 and include a roomId
    it('Should add a room to a house', async () => {
        const res = await api.post('/rooms/testHouseId').send({ name: 'Living Room' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('roomId');
    });

    // Test: Missing required fields should return a 400 error
    it('Should return 400 if room name is missing', async () => {
        const res = await api.post('/rooms/testHouseId').send({});
        expect(res.statusCode).toEqual(400);
    });
});
