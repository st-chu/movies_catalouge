from flask import Flask, render_template
import tmdb_client
from tmdb_client import popular_movies

app = Flask(__name__)


@app.route('/')
def homepage():
    movie = tmdb_client.popular_movies(12)
    return render_template('homepage.html', movies=movie)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.image_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
