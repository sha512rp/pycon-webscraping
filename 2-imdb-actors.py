"""Download and parse actors for top movies in IMDB."""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'http://m.imdb.com/chart/top'


def main():
    for i, movie in enumerate(get_top_imdb_movies()):
        print(movie[0])
        print(get_movie_actors(movie[1]))
        print()
        if i > 2:
            break


def get_top_imdb_movies():
    """Retrive top 250 imdb movies."""
    movies = []
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    # .media h4
    for movie_tag in soup.find_all(class_='media'):
        title = movie_tag.find('h4').text.split('\n')[2]
        href = movie_tag.find('a')['href']
        movie_url = urljoin(BASE_URL, href)
        movies.append((title, movie_url))
    return movies


def get_movie_actors(movie_url):
    """Retrieve top paid crew for a movie."""
    actors = []
    res = requests.get(movie_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for actor_tag in soup.select('#cast-and-crew ul li strong'):
        actors.append(actor_tag.text)
    return actors


if __name__ == '__main__':
    main()
