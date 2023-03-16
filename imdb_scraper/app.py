import os
from flask import Flask, render_template, request, jsonify
from .search import create_connection, search_quotes

# Initialize the Flask app with the template folder set to the project's templates folder.
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))


# Route for the home page.
@app.route('/')
def index():
    # Render the index.html template.
    return render_template('index.html')


# Route for handling search requests.
@app.route('/search', methods=['POST'])
def search():
    # Get the form data.
    movie_title = request.form.get('movie_title', None)
    character_name = request.form.get('character_name', None)
    keywords = request.form.get('keywords', None)

    # Create a list of keywords if they exist.
    keywords_list = [kw.strip() for kw in keywords.split(',')] if keywords else []

    # Connect to the database.
    database = "quotes.db"
    conn = create_connection(database)

    if conn is not None:
        # Perform the search.
        results = search_quotes(conn, movie_title=movie_title, keywords=keywords_list, character_name=character_name)
        conn.close()

        # Create a list of dictionaries containing the character and quote for each result.
        search_results = [{'character': result[2], 'quote': result[3]} for result in results]

        # Return the search results as a JSON object.
        return jsonify(search_results)
    else:
        # Return an error message if the connection to the database could not be established.
        return jsonify({'error': 'Error! Cannot establish a database connection.'})


# Run the Flask app in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
