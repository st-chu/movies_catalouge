from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    movies_list = ['popular', 'now_playing', 'upcoming', 'top_rated', 'niepoprawna_wartość']
    selected_list = request.args.get('list_type', 'popular')
    try:
        movie = tmdb_client.get_movies(8, selected_list)
        return render_template('homepage.html', movies=movie, movies_list=movies_list, selected_list=selected_list)
    except:
        movie = tmdb_client.get_movies(8, 'popular')
        return render_template('homepage.html', movies=movie, movies_list=movies_list, selected_list='popular')


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
