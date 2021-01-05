from flask import Flask, render_template, request, redirect, url_for
import tmdb_client
import datetime

FAVORITES = set([])

app = Flask(__name__)


@app.route('/')
def homepage():
    movies_list = ['popular', 'now_playing', 'upcoming', 'top_rated', 'niepoprawna_wartość']
    selected_list = request.args.get('list_type', 'popular')
    print(FAVORITES)
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


@app.route("/search")
def search():
    search_query = request.args.get('q', '')
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template('search.html', movies=movies, search_query=search_query)


@app.route("/tv-today")
def tv_today():
    date = datetime.date.today()
    try:
        tv = tmdb_client.get_tv_airing_today()
        return render_template('tv_today.html', tv=tv, date=date)
    except:
        tv = []
        return render_template('tv_today.html', tv=tv, date=date)


@app.route("/favorites/add", methods=['POST'])
def add_to_favourites():
    movie_id = request.form.get('movie_id')
    selected_list = request.args.get('list_type') tu
    print(selected_list)
    if movie_id:
        FAVORITES.add(movie_id)
    return redirect(url_for('homepage', selected_list=selected_list)) tu


if __name__ == '__main__':
    app.run(debug=True)
