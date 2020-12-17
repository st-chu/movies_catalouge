from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def homepage():
    movies = []

    for item in range(1, 10):
        movies.append('film')

    return render_template('homepage.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
