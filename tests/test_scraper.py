import unittest
import os
from imdb_scraper.scraper import create_connection, get_quotes, main
from imdb_scraper.search import search_quotes


class TestScraper(unittest.TestCase):
    # Test cases for the scraper module.

    def setUp(self):
        # Set up the test environment.
        self.test_db = "test_quotes.db"
        self.movie_id = "tt0111161"

    def test_create_connection(self):
        # Test the create_connection function.
        conn = create_connection(self.test_db)
        self.assertIsNotNone(conn)
        conn.close()

        # Clean up by removing the test database file.
        os.remove(self.test_db)

    def test_get_quotes(self):
        # Test the get_quotes function.
        url = f"https://www.imdb.com/title/{self.movie_id}/quotes"
        quotes = get_quotes(url)

        # Test if the quotes are returned as a list and if the list is not empty.
        self.assertIsInstance(quotes, list)
        self.assertGreater(len(quotes), 0)

    def test_main(self):
        # Test the main function of the scraper module.
        main(self.movie_id)
        conn = create_connection("quotes.db")

        # Test if the scraped quotes are stored in the database.
        results = search_quotes(conn, movie_title=self.movie_id)
        self.assertGreater(len(results), 0)
        conn.close()


if __name__ == "__main__":
    unittest.main()
