"""tests/test_basic.py"""
import unittest
from app import APP

class FlaskTestCase(unittest.TestCase):
    """Test for app.py"""

    # Getting a request that actually exists
    def test_get_one_request(self):
        """test get single request"""
        tester = APP.test_client(self)
        response = tester.get('/api/v1/users/requests/1')
        self.assertEqual(response.status_code, 200)

    # If a request is not found
    def test_one_request_not_found(self):
        """test single request not found"""
        tester = APP.test_client(self)
        response = tester.get('/api/v1/users/requests/12')
        self.assertIn(b"Request not found!", response.data)

if __name__ == '__main__':
    unittest.main()
