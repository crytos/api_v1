"""tests/test_basic.py"""
import unittest
from app import APP

class FlaskTestCase(unittest.TestCase):
    """Test for app.py"""

    # Ensure that Flask was set up correctly
    def test_index(self):
        """test get all requests"""
        tester = APP.test_client(self)
        response = tester.get('/api/v1/users/requests', content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
