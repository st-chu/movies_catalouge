from movies_catalouge import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.image_url(file_path=poster_api_path)
    assert expected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"


def test_get_endpoint_full_url():
    target = 'movie/popular?language=pl-PL'
    endpoint = "https://api.themoviedb.org/3/movie/popular?language=pl-PL"
    endpoint_url = tmdb_client.get_endpoint_full_url(target)
    assert endpoint == endpoint_url


def test_get_headers():
    token = 'my token'
    headers = tmdb_client.get_headers(token)
    assert token in headers["Authorization"]


def test_call_tmdb_api(monkeypatch):
    mock_details = ['detail1', 'detail2', 'detail3']
    mock_requests = Mock()
    response = mock_requests.return_value
    response.json.return_value = mock_details
    monkeypatch.setattr("movies_catalouge.tmdb_client.requests.get", mock_requests)
    details = tmdb_client.call_tmdb_api('popular')
    assert details == mock_details


def test_get_movie_list(monkeypatch):
    mock_movie_list = ['movie 1', 'movie 2']
    call_mock = Mock(return_value=mock_movie_list)
    monkeypatch.setattr("movies_catalouge.tmdb_client.call_tmdb_api", call_mock)
    movie_list = tmdb_client.get_movies_list(list_name='popular')
    assert movie_list == mock_movie_list


def test_get_single_movie(monkeypatch):
    mock_movie_details = {'key1': 'value1', 'key2': 'value2'}
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie_details
    monkeypatch.setattr("movies_catalouge.tmdb_client.requests.get", request_mock)
    movie_details = tmdb_client.get_single_movie(movie_id=3)
    assert movie_details == mock_movie_details


def test_get_single_movie_cast(monkeypatch):
    cast = ['actor1', 'actor2']
    mock_movie_cast = {'cast': cast}
    call_mock = Mock(return_value=mock_movie_cast)
    monkeypatch.setattr("movies_catalouge.tmdb_client.call_tmdb_api", call_mock)
    movie_cast = tmdb_client.get_single_movie_cast(2)
    assert movie_cast == cast


def test_get_movie_image(monkeypatch):
    images = ['image1', 'image2', 'image3']
    backdrops = {'backdrops': images}
    call_mock = Mock(return_value=backdrops)
    monkeypatch.setattr("movies_catalouge.tmdb_client.call_tmdb_api", call_mock)
    image = tmdb_client.get_movie_image(23)
    assert image in images








