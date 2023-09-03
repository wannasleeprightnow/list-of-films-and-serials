from requests import get
from bs4 import BeautifulSoup

from config import KP_API_KEY


def get_movie_id(title: str) -> str:
    title = title.replace(" ", "+")
    html_page = get(url=f'https://www.kinopoisk.ru/index.php?kp_query={title}').text

    bs = BeautifulSoup(html_page, "html.parser")
    id = str(bs.find("p", class_="name")).split()[3][9:-1]
    return id


def get_data_by_id(id: str) -> dict:
    headers = {
    'accept': 'application/json',
    'X-API-KEY': KP_API_KEY,
}
    
    data = get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}', headers=headers)
    return data.json()


def parse_data(data: dict) -> dict:

    movie = {
        "title": data.get("nameRu"),
        "rating": str(str(data.get("ratingKinopoisk"))),
        "description": data.get("description"),
        "genres": [genre["genre"].capitalize() for genre in data.get("genres")],
        "year": str(data.get("year", data.get("startYear")))
    }
    
    return movie
