import sqlite3
from sqlite3 import Error


def create_connection(database):
    # Create a connection to the SQLite database.
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn


def search_quotes(conn, movie_title=None, keywords=None, character_name=None):
    #
    # Search for quotes in the database based on the provided parameters.
    #
    # Args:
    #     conn: A connection to the SQLite database.
    #     movie_title: The IMDb movie ID to search for (optional).
    #     keywords: A list of keywords to search for in the quotes (optional).
    #     character_name: The name of the character to search for (optional).
    #
    # Returns:
    #     A list of matching quotes as tuples with the format (id, movie_id, character, quote).
    #
    cursor = conn.cursor()
    query = "SELECT * FROM quotes WHERE 1"
    params = []

    if movie_title:
        query += " AND movie_id = ?"
        params.append(movie_title)

    if character_name:
        query += " AND character LIKE ?"
        params.append(f"%{character_name}%")

    if keywords:
        for keyword in keywords:
            query += " AND quote LIKE ?"
            params.append(f"%{keyword}%")

    cursor.execute(query, params)
    return cursor.fetchall()


def main():
    # Search for quotes in the database based on the specified criteria and print the results.
    database = "quotes.db"
    conn = create_connection(database)

    if conn is not None:
        movie_title = "tt0111161"  # Replace this with the IMDb movie ID you want to search
        keywords = ["hope", "fear"]  # Replace these with the keywords you want to search
        character_name = "Andy"  # Replace this with the character name you want to search

        results = search_quotes(conn, movie_title=movie_title, keywords=keywords, character_name=character_name)

        for result in results:
            print(f"{result[2]}: {result[3]}")

        conn.close()
    else:
        print("Error! Cannot establish a database connection.")


if __name__ == "__main__":
    main()
