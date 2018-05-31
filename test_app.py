"""tests_app.py"""
import unittest
import json
from app import APP

class FlaskTestCase(unittest.TestCase):
    """Test for app.py"""

    def test_get_one_request(self):
        """test get one request"""

        tester = APP.test_client(self)

        response = tester.put(
            '/api/v1/users/requests/1',
            data=json.dumps({"request":"helo"}), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Request modified succesfully", response.data)

    def test_failed_get_one_request(self):
        """test not found request to modify"""

        tester = APP.test_client(self)

        response = tester.put(
            '/api/v1/users/requests/23',
            data=json.dumps({"request":"helo"}), content_type="application/json"
        )

        self.assertIn(b"Request not found!", response.data)

if __name__ == '__main__':
    unittest.main()
