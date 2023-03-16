import json
import sys
import unittest
from imdb_scraper.app import app

sys.path.append("..")


class TestApp(unittest.TestCase):
    # Test cases for the Flask application.

    def setUp(self):
        # Set up a test client for the Flask application.
        self.app = app.test_client()

    def test_index(self):
        # Test the index route.
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        # Test the search route.
        # Send a POST request to the search route with example data.
        response = self.app.post(
            '/search',
            data=dict(movie_title="tt0111161", character_name="Andy", keywords="hope")
        )
        self.assertEqual(response.status_code, 200)

        # Load the JSON response data.
        data = json.loads(response.data)

        # Test if the response data is a list and contains at least one result.
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        # Test if the result contains both character and quote keys.
        self.assertIn('character', data[0])
        self.assertIn('quote', data[0])


if __name__ == "__main__":
    unittest.main()
