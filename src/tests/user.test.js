const request = require('supertest');
const app = require('../server');

describe('User API Tests', () => {
    let server;
    let api;

    // Start the server before tests using a dynamic port
    beforeAll((done) => {
        server = app.listen(0, () => {
            const port = server.address().port;
            api = request(`http://localhost:${port}`);
            done();
        });
    });

    // Close the server after tests to free up resources
    afterAll((done) => {
        server.close(done);
    });

    // Test: Creating a user should return 201 and include a userId
    it('Should create a user successfully', async () => {
        const res = await api.post('/users').send({ username: 'Alice', email: 'alice@example.com' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('userId');
    });

    // Test: Missing email should return a 400 error
    it('Should return 400 if username or email is missing', async () => {
        const res = await api.post('/users').send({ username: 'Alice' });
        expect(res.statusCode).toEqual(400);
    });
});
