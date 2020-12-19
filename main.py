from flask import Flask, render_template
import tmdb_client


app = Flask(__name__)


@app.route('/')
def homepage():
    movie = tmdb_client.popular_movies(8)
    return render_template('homepage.html', movies=movie)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.image_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    image = tmdb_client.get_movie_image(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast, image_path=image)


if __name__ == '__main__':
    app.run(debug=True)
