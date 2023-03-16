import unittest
import sys
from imdb_scraper.search import create_connection, search_quotes

sys.path.append("..")


class TestSearch(unittest.TestCase):
    # Test cases for the search module.

    def setUp(self):
        # Set up the test environment.
        self.database = "quotes.db"
        self.conn = create_connection(self.database)

    def test_create_connection(self):
        # Test the create_connection function.
        self.assertIsNotNone(self.conn)

    def test_search_quotes(self):
        # Test the search_quotes function.
        movie_title = "tt0111161"
        character_name = "Andy"
        keywords = ["outside"]

        results = search_quotes(self.conn, movie_title=movie_title, keywords=keywords, character_name=character_name)

        # Test if the search results are returned as a list and if the list is not empty.
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

    def tearDown(self):
        # Clean up the test environment.
        self.conn.close()


if __name__ == "__main__":
    unittest.main()
