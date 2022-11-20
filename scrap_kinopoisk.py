from requests import get
from bs4 import BeautifulSoup


# Функция, достающая айди
def getting_id(title: str) -> str:
    title = "+".join(title.split())
    # Достаем айди из страницы кинопоиска
    html_page = get(url=f'https://www.kinopoisk.ru/index.php?kp_query={title}').text
    bs = BeautifulSoup(html_page, "html.parser")
    id = str(bs.find("p", class_="name")).split()[3][9:-1]
    return id


def getting_data(title: str) -> dict:
    id = getting_id(title)
    headers = {
    'accept': 'application/json',
    'X-API-KEY': 'fb256f97-1a03-4c25-a02c-7e81a6f3b89c',
}
    # Делаем запрос по айди в апи кинопоиска
    info = get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}', headers=headers)
    return dict(info.json())
    