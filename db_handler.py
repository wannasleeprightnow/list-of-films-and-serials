import sqlite3

DB = "database.sqlite"
LOGIN = ''

# Функция, добавляющая фильм/сериал в бд
def insert_movie_info(data: dict["title", "rating", "description", "genres",], movie_type: str) -> None:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    movie_type = cur.execute("""select id from types
    where movie_type=?""", (movie_type,)).fetchall()

    # Если в бд не существует таких жанров, то они добавляются, а потом берутся из айди
    try:
        genres = [j[0] for j in [cur.execute("""select id from genres
        where genre=?""", (data["genres"][i],)).fetchall() for i in range(len(data["genres"]))]]
    except IndexError:
        for genre in data["genres"]:
            if not cur.execute("""select id from genres
            where genre=?""", (genre, )).fetchall():
                cur.execute("insert into genres (genre) values (?)", (genre,))
                con.commit()
        
        genres = [cur.execute("""select id from genres
    where genre=?""", (data["genres"][i],)).fetchall() for i in range(len(data["genres"]))]

    genres = [str(i[0]) for i in genres]
    columns = "(title, movie_type, rating, description, genres, year)"
    values = (data['title'], str(movie_type[0][0]), data["rating"], data["description"], str(genres), data["year"])

    cur.execute("insert into movies" + columns + " values (?, ?, ?, ?, ?, ?)", values)

    con.commit()    
    cur.close()
    con.close()

# Функция, добавляющая фильм/сериал в бд юзеров
def insert_users_movie(users_data: dict["login", "title", "user_rating", "count_wathced_series", "movie_type", "condition"]) -> None:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    users_data["title"] = cur.execute("""select id from movies
    where title=?""", (users_data["title"].capitalize(),)).fetchone()[0]

    users_data["movie_type"] = cur.execute("""select id from types
    where movie_type=?""", (users_data["movie_type"],)).fetchone()[0]

    users_data["condition"] = cur.execute("""select id from conditions
    where condition=?""", (users_data["condition"],)).fetchone()[0]

    columns = "(login, title, user_rating, count_watched_series, movie_type, condition)"

    cur.execute("insert into users" + columns + " values (?, ?, ?, ?, ?, ?)", tuple(users_data.values()))

    con.commit()
    cur.close()
    con.close()


# Функция берующая конкретный тип или все фильмы и сериалы юзера
def all_users_movies(login: str, movie_type="movie") -> list:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    if movie_type == "movie":
        result = list(cur.execute("""select * from users
        where login=?""", (login,)).fetchall())
    elif movie_type != "movie":
        result = list(cur.execute("""select * from users
        where login=? and movie_type=(select id from types
        where movie_type=?)""", (login, movie_type,)).fetchall())

    cur.close()
    con.close()

    return result

# Функция, берущая информацию о фильм/сериале
def get_info(title: str) -> list:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    result = cur.execute("""select * from movies
    where title=?""", (title.capitalize(),)).fetchall()

    cur.close()
    con.close()

    return result


# Функция,. распаршивающая информацию о фильме/сериале
def parse_movies_info(info: list) -> list:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    info = list(info[0])

    info[2] = cur.execute("""select condition from conditions
    where id=?""", info[2]).fetchone()[0]

    info[5] = tuple(info[5][2:-2].split("', '"))
    info[5] = [info[5][i] for i in range(len(info[5]))]
    info[5] = [cur.execute("""select genre from genres
    where id=?""", (info[5][i][1:-2],)).fetchone()[0] for i in range(len(info[5]))]

    cur.close()
    con.close()

    return info


# Функция, достающая информацию юзера о фильме/сериале
def get_users_movie_info(id: str) -> list:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    result = list(cur.execute("""select * from users
    where title=?""", (id,)).fetchone())

    print(result)
    result[2] = cur.execute("""select title from movies
    where id=?""", (id,)).fetchone()[0]
    result[5] = cur.execute("""select movie_type from types
    where id=?""", (result[5],)).fetchone()[0]
    
    cur.close()
    con.close()

    return result


# Функция, удаляющая информацию о фильме/сериале из бд юзеров
def delete_users_movie(login: str, title: str) -> None:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    cur.execute("""delete from users
    where login=? and title=?""", (login, title[0]))

    con.commit()
    cur.close()
    con.close()


# Функция, получающая из бд айди фильма/сериала
def get_id_movie(title: str) -> str:
    con = sqlite3.connect(DB)
    cur = con.cursor()

    result = cur.execute("""select id from movies
    where title=?""", (title.capitalize(),)).fetchone()

    cur.close()
    con.close()
    return result


# Функция аутентификации
def auth(login, password, signal):

    global LOGIN
    # Подключение к бд
    con = sqlite3.connect(DB)
    cur = con.cursor()
    
    # Запрос для проверки введенных данных
    user = cur.execute("""select * from users_info
where login=?""", (login,)).fetchall()

    # Проверка введенных данных
    if user != [] and user[0][2] == password:
        signal.emit("Вы вошли в свой аккаунт.")
        LOGIN = login
    else:
        signal.emit("Введены неверные данные.")
    
    cur.close()
    con.close()


# Функция, возвращающая логин пользователя
def ret_login():
    return LOGIN


# Функция регистрации
def reg(login, password, signal):
    # Подключение к бд
    con = sqlite3.connect(DB)
    cur = con.cursor()
    
    # Проверка логина на уникальность
    if cur.execute("""select login from users_info
where login==?""", (login,)).fetchall()  != []:
        signal.emit("Такой логин уже используется.")
    else:
        # Пользователь добавляется в бд
        signal.emit("Вы успешно зарегистрировались.")
        cur.execute(f'insert into users_info (login, password) values(?, ?)', (login, password))
        con.commit()
        
    
    cur.close()
    con.close()


# Фунцкия, получающая все типы состояний
def all_conditions():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    result = [i[0] for i in cur.execute("""select condition from conditions""").fetchall()]

    cur.close()
    con.close()

    return result

