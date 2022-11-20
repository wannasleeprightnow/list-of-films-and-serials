from scrap_kinopoisk import getting_data


def parse(title: str) -> dict:
    data = getting_data(title)
    info = {
        "title": title.capitalize(),
        "rating": str(data.get("ratingKinopoisk")),
        "description": data.get("description"),
        "year": data.get("year"),
        "genres": [i["genre"] for i in data.get("genres")]
    }
    return info
