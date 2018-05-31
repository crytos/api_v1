"""tests_app.py"""
import unittest
import json
from app import APP

class FlaskTestCase(unittest.TestCase):
    """Test for app.py"""

    def test_create_new_request(self):
        """test get one request"""

        tester = APP.test_client(self)

        response = tester.post(
            '/api/v1/users/requests',
            data=json.dumps({'request':'Request5', 'status':'pending', 'user':'josh'}),
            content_type="application/json", follow_redirects=False)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Request added!", response.data)

    def test_create_new_request_invalid(self):
        """test invalid sent request"""

        tester = APP.test_client(self)

        response = tester.post(
            '/api/v1/users/requests',
            data=json.dumps({'request':'', 'status':'pending', 'user':''}),
            content_type="application/json", follow_redirects=False)

        self.assertIn(b"Invalid request", response.data)

if __name__ == '__main__':
    unittest.main()
