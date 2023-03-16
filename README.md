# IMDb Quote Scraper and Search

This project is a web application that scrapes IMDb movie quotes and stores them in a SQLite database. Users can search for quotes by movie ID, character name, and keywords. The project consists of a Flask web application, a scraper module for fetching and storing quotes, and a search module for querying the stored quotes.

## Features

- Scrape movie quotes from IMDb
- Store scraped quotes in a SQLite database
- Web-based interface for searching quotes by movie ID, character name, and keywords
- Unit tests for application, scraper, and search modules

## Installation

1. Clone the repository:

   git clone https://github.com/cwwp671/imdb_scraper.git

2. Install the required packages:

   pip install -r requirements.txt

## Usage

1. Scrape quotes for a specific movie by running the `scraper.py` script and providing the IMDb movie ID:

   python imdb_scraper/scraper.py

2. Start the Flask web application:

   python imdb_scraper/main.py

3. Open your browser and navigate to http://127.0.0.1:5000.

4. Use the web interface to search for quotes by movie ID, character name, and keywords.

## Running Tests

To run the test suite, execute the following command:

python -m unittest discover tests
 
 
