const request = require('supertest');
const app = require('../server');

describe('Device API Tests', () => {
    let server;
    let api;

    // Start the server before tests using a dynamically assigned port
    beforeAll((done) => {
        server = app.listen(0, () => {
            const port = server.address().port;
            api = request(`http://localhost:${port}`);
            done();
        });
    });

    // Close the server after tests to release the port
    afterAll((done) => {
        server.close(done);
    });

    // Test: Adding a device should return 201 and include a deviceId
    it('Should add a device to a room', async () => {
        const res = await api.post('/devices/testRoomId').send({ name: 'Smart Light', type: 'Light' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('deviceId');
    });

    // Test: Missing required fields should return a 400 error
    it('Should return 400 if device name or type is missing', async () => {
        const res = await api.post('/devices/testRoomId').send({ name: 'Smart Light' });
        expect(res.statusCode).toEqual(400);
    });

    // Test: Toggling device status should return 200
    it('Should toggle the device status', async () => {
        // First, create a device
        const deviceRes = await api.post('/devices/testRoomId').send({ name: 'Smart Light', type: 'Light' });
        const deviceId = deviceRes.body.deviceId; // Extract created device ID

        // Then, toggle the device status
        const toggleRes = await api.patch(`/devices/${deviceId}/toggle`);
        expect(toggleRes.statusCode).toEqual(200);
    });
});
