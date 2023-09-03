import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from get_data import *
from gui.main_window_gui import Ui_widget
from db.db import *
from db.sql import *
from authorization import *


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        
        self.auth = MyWidget()
        self.auth.show()
        
        self.ui.add_button.clicked.connect(self.add_movie)
        self.ui.update_button.clicked.connect(self.update_tables)
        self.ui.remove_button.clicked.connect(self.remove_item)
        self.ui.info_button.clicked.connect(self.info)
        
        self.ui.condition_write.addItems(
            ["planned", "watching", "watched", "postponed", "abandoned"]
        )
        
        self.tables = {
            "planned": self.ui.planned_table,
            "watching": self.ui.watching_table,
            "watched": self.ui.watched_table,
            "postponed": self.ui.postponed_table,
            "abandoned": self.ui.abandoned_table,
        }

    def add_movie(self) -> None:
        
        user_id = ret_user_id()
        title = self.ui.title_write.text().capitalize()
        rating = self.ui.rating_write.text(),
        count_watched_series = self.ui.watched_series_write.text()
        movie_type = str(self.ui.movie_type_write.currentText())
        condition = str(self.ui.condition_write.currentText())
        
        if "" in (title, rating, count_watched_series):
            return
        
        self.copy_movie = fetch_all(select_movie, (user_id, title))
        if self.copy_movie:
            execute(delete_movie, (user_id, title) )
            
        execute(insert_movie, (user_id, title, rating[0], count_watched_series, movie_type, condition))
        
        self.update_tables()
        self.ui.title_write.clear()
        self.ui.rating_write.clear()
        self.ui.watched_series_write.clear()

    def update_tables(self):
        self.all_user_movies = fetch_all(select_all_user_movies, (ret_user_id(),))
        for table_name, table in self.tables.items():
            self.table_items = list(
                filter(lambda x: x["condition"] == table_name, self.all_user_movies)
            )
            table.setRowCount(len(self.table_items))
            for i, movie in enumerate(self.table_items):
                for j, key in enumerate(movie.keys()):
                    table.setItem(i, j, QTableWidgetItem(str(movie[key])))

    def info(self):
        self.ui.info_error.setText("")
        try:
            movie_info = parse_data(
                get_data_by_id(get_movie_id(self.ui.info_title_write.text()))
            )
        except IndexError:
            self.ui.info_error.setText("Введено неверное название.")
        else:
            self.ui.rating_place.setText(movie_info["rating"])
            self.ui.genres_place.setText(", ".join(movie_info["genres"]))
            self.ui.year_place.setText(movie_info["year"])
            self.ui.description_place.setText(movie_info["description"])

    def remove_item(self):
        execute(delete_movie, (ret_user_id(), self.ui.title_write.text().capitalize()))
        self.update_tables()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        mywin = Interface()
        mywin.show()
        sys.exit(app.exec_())
    finally:
        close_db()
