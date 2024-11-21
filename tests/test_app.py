import unittest
from app import app

class TestHomeRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API Flask funcionando!"})

class TestSumRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_sum_route(self):
        response = self.app.get('/sum/10/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"sum": 15})

class TestStatusRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json)
        self.assertEqual(response.json["status"], "OK")

if __name__ == "__main__":
    unittest.main()