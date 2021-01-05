import requests
import random
from typing import List, Dict, Union


token = '****************'


base_url = 'https://api.themoviedb.org/3/'


def get_movies_list(list_name: str) -> Dict[str, Union[int, List[Dict[str, Union[str, bool, int, float, List[int]]]]]]:
    endpoint = f'https://api.themoviedb.org/3/movie/{list_name}?language=pl-PL'
    headers = {
        'Authorization': token,
    }
    response = requests.get(url=endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies(how_many: int, list_name: str) -> List[Dict[str, Union[bool, str, List[int], int, float]]]:
    movies = get_movies_list(list_name)
    random_movies = [movies['results'].pop(random.randint(0, len(movies['results'])-1)) for movie in range(how_many)]
    return random_movies


def image_url(file_path: str, file_size="w342") -> str:
    base_url = "http://image.tmdb.org/t/p/"
    return f'{base_url}{file_size}{file_path}'


def get_single_movie(
        movie_id: int
) -> Dict[str, Union[bool, str, Dict[str, Union[int, str]], int, List[Dict[str, Union[int, str]]], float,
                     List[Dict[str, str]]]]:
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?language=pl-PL"
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id: int):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']


def get_movie_image(movie_id: int) -> List[Dict[str, Union[bool, int, str, float]]]:
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return random.choice(response.json()['backdrops'])


def search(search_query: str):
    endpoint = f'https://api.themoviedb.org/3/search/movie?query={search_query}'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    return response.json()['results']


def get_tv_airing_today():
    endpoint = f'{base_url}tv/airing_today?language=pl-PL'
    headers = {'Authorization': token}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['results']



