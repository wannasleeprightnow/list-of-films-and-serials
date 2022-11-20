import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow
from interface import Ui_widget
from db_handler import *
from parse_data import parse
from authorization import *


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        # Показ окна аутентификации
        self.auth = MyWidget()
        self.auth.show()
        # Привязка кнопок
        self.ui.add_button.clicked.connect(self.add_movie)
        self.ui.update_button.clicked.connect(self.update_tables)
        self.ui.remove_button.clicked.connect(self.remove_item)
        self.ui.info_button.clicked.connect(self.info)
        # Заполнение комбо-бокса состояниями
        self.ui.condition_write.addItems(all_conditions())
        self.tables = [self.ui.planned_table, self.ui.watching_table,
        self.ui.watched_table, self.ui.postponed_table, self.ui.abandoned_table]

    def add_movie(self):
        # Информация, введенная пользователем
        self.info = {
            "login": ret_login(),
            "title": self.ui.title_write.text(),
            "user_rating": self.ui.rating_write.text(),
            "count_watched_series": self.ui.watched_series_write.text(),
            "movie_type": str(self.ui.movie_type_write.currentText()),
            "condition": str(self.ui.condition_write.currentText())
        }
        # Проверка на наличие информации о фильме/сериале, в случае отсутсвия ее добавление
        if not get_info(self.info["title"]):
            insert_movie_info(parse(self.info["title"]), self.info["movie_type"])

        title_id = get_id_movie(self.info["title"])[0]
        titles = [i[2] for i in all_users_movies(self.info["login"], self.info["movie_type"])]

        # Условие, проверяющее, что у пользователя только один экземпляр фильма/сериала
        if str(title_id) in titles:
            delete_users_movie(self.info["login"], get_id_movie(self.info["title"].capitalize()))

        # Добавление фильма/сериала к пользователю и обновление таблиц
        insert_users_movie(self.info)
        self.update_tables()

        self.ui.title_write.clear()
        self.ui.rating_write.clear()
        self.ui.watched_series_write.clear()

    # Функция, обновляющая таблицы
    def update_tables(self):
        for name in self.tables:
            self.update_table(name)

    def update_table(self, name_table: str):
        # Соответствие каждой таблице индекса состояния, которое она показывает
        tables_coondition = {
            self.ui.planned_table: "1",
            self.ui.watching_table: "2",
            self.ui.watched_table: "3",
            self.ui.postponed_table: "4",
            self.ui.abandoned_table: "5",
            }
        # Получение всех фильмов/сериалов пользователя и сортировка их по состоянию
        movies = all_users_movies(ret_login())
        print(movies)
        movies = [get_users_movie_info(movies[i][2]) for i in range(len(movies)) if movies[i][6] == tables_coondition[name_table]]
        name_table.setRowCount(len(movies))
        # Заполнение таблицы
        for i, elem in enumerate(movies):
            for j, val in enumerate(elem[2:6]):
                name_table.setItem(i, j, QTableWidgetItem(str(val)))

    # Функция, отображающая информацию о фильме/сериале, который запросил пользователь
    def info(self):
        result = parse_movies_info(get_info(self.ui.info_title_write.text()))
        self.ui.rating_place.setText(result[3])
        self.ui.genres_place.setText(', '.join(result[5]))
        self.ui.year_place.setText(result[-1])
        self.ui.description_place.setText(result[4])

    # Функция, удаляющая фильм/сериал, который запросил пользователь
    def remove_item(self):
        title = get_id_movie(self.ui.title_write.text().capitalize())
        delete_users_movie(ret_login(), title)
        self.update_tables()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
