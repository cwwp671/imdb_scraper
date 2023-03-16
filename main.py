import sys
from pathlib import Path
from imdb_scraper.app import app

sys.path.append(str(Path(__file__).parent / "imdb_scraper"))

if __name__ == "__main__":
    app.run(debug=True)
