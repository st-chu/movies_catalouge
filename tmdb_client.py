import requests
import random


token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZDVkOWRlZTdjMzEwMjlkZWQ2NDBkYzE3NTEwNTg3YSIsInN1YiI6IjVmZDhmN' \
            '2NjMWYzZTYwMDAzZmIyOTJiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ewqO0KDgM6YtYjqzvQNBrZ-xgdk' \
            'A7nl1DBn5hO9XnL0'


def popular_movies(how_many):
    endpoint = 'https://api.themoviedb.org/3/movie/popular'
    headers = {
        'language': 'pl',
        'Authorization': token,
        'Content-Type': 'application/json;charset=utf-8',
        'languages': 'pl-PL'
    }
    r = requests.get(url=endpoint, headers=headers)
    return [random.choice(r.json().get('results')) for i in range(how_many)]


def image_url(file_path, file_size="w342"):
    base_url = "http://image.tmdb.org/t/p/"
    return f'{base_url}{file_size}{file_path}'


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']


def get_movie_image(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return random.choice(response.json()['backdrops'])

