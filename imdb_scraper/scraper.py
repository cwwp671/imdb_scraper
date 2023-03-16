import requests
import sqlite3
from bs4 import BeautifulSoup
from sqlite3 import Error


def create_connection(database):
    # Create a connection to the SQLite database.
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    # Create the quotes table if it does not exist.
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            movie_id TEXT NOT NULL,
                            character TEXT NOT NULL,
                            quote TEXT NOT NULL
                          );''')
    except Error as e:
        print(e)


def insert_quote(conn, quote):
    # Insert a quote into the quotes table.
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO quotes (movie_id, character, quote) VALUES (?, ?, ?)",
                       (quote['movie_id'], quote['character'], quote['quote']))
        conn.commit()
    except Error as e:
        print(e)


def get_quotes(url):
    # Fetch quotes from the given URL and return a list of cleaned quotes.
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='sodatext')
    clean_quotes = []

    for quote in quotes:
        quote_text = quote.get_text(strip=True)
        character = quote.find('span', class_='character').get_text(strip=True)
        clean_quotes.append({'character': character, 'quote': quote_text})

    return clean_quotes


def main(movie_id):
    # Scrape quotes from the specified IMDb movie ID and store them in the database.
    url = f"https://www.imdb.com/title/{movie_id}/quotes"
    quotes = get_quotes(url)

    if not quotes:
        print("No quotes found")
        return

    database = "quotes.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        for quote in quotes:
            quote['movie_id'] = movie_id
            insert_quote(conn, quote)
        conn.close()
    else:
        print("Error! Cannot establish a database connection.")


if __name__ == "__main__":
    # Replace this with the IMDb movie ID of the movie you want to scrape.
    movie_id = "tt0111161"
    main(movie_id)
