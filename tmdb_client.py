import requests


def popular_movies(how_many):
    endpoint = 'https://api.themoviedb.org/3/movie/popular'
    token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZDVkOWRlZTdjMzEwMjlkZWQ2NDBkYzE3NTEwNTg3YSIsInN1YiI6IjVmZDhmN' \
            '2NjMWYzZTYwMDAzZmIyOTJiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ewqO0KDgM6YtYjqzvQNBrZ-xgdk' \
            'A7nl1DBn5hO9XnL0'
    headers = {
        'language': 'pl',
        'Authorization': token,
        'Content-Type': 'application/json;charset=utf-8',
        'languages': 'pl-PL'
    }
    r = requests.get(url=endpoint, headers=headers)

    return r.json().get('results')[:how_many]


def image_url(file_path, file_size="w342"):
    base_url = "http://image.tmdb.org/t/p/"
    return f'{base_url}{file_size}{file_path}'



