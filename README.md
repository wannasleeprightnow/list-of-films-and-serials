# List of films and serials

## Описание
Десктопное приложение, написанное на PyQt5, для составления списка фильмов и сериалов.

![](https://github.com/wannasleeprightnow/list-of-films-and-serials/raw/main/images/full_window.png)

## Функции

### Авторизация и регистрация
Пользователь создает аккаунт/заходит в уже созданный.

![](https://github.com/wannasleeprightnow/list-of-films-and-serials/raw/main/images/sign_in_sign_up.png)

### Добавление
Далее он может добавить фильм/сериал в список. Список делится на следующие состояния:
- Planned
- Watching
- Watched
- Postponed
- Abandoned

При добавлении пользователь указывает:
- Название
- Свою оценку от 0 до 10
- Количество просмотренных серий, в случае с сериалами
- Тип - сериал или фильм
- Состояние(planned, watching и тд)

![](https://github.com/wannasleeprightnow/list-of-films-and-serials/raw/main/images/add_bb.png)

### Удаление
Пользователь может удалять фильмы/сериалы, введя его название сюда:

![](https://github.com/wannasleeprightnow/list-of-films-and-serials/raw/main/images/remove_bb.png)

### Получение краткой информации
Также, пользователь может получить краткую информацию о фильме/сериале, введя его название сюда:

![](https://github.com/wannasleeprightnow/list-of-films-and-serials/raw/main/images/info_bb.png)

## Запуск

Клонирование репозитория:

```bash
git clone https://github.com/wannasleeprightnow/list-of-films-and-serials list-of-films-and-serials
```

Создание и активация виртуального окружения:

```bash
python3 -m venv venv
# Для linux
source venv/bin/activate
# Для windows
source venv\Scripts\activate.bat
```
Получить KP_API_KEY на этом [сайте](https://kinopoiskapiunofficial.tech/rates) и подставить его в команду:

```bash
echo "SQLITE_DB_FILE = "db/db.sqlite"
KP_API_KEY = """ > .env
```
Обновление pip, установка зависимостей и запуск:

```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 app/main_window.py
```
