# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(950, 860)
        widget.setMinimumSize(QtCore.QSize(950, 860))
        widget.setMaximumSize(QtCore.QSize(950, 860))
        self.condition_planned = QtWidgets.QLabel(widget)
        self.condition_planned.setGeometry(QtCore.QRect(10, 10, 110, 20))
        self.condition_planned.setObjectName("label")
        self.planned_table = QtWidgets.QTableWidget(widget)
        self.planned_table.setGeometry(QtCore.QRect(10, 40, 540, 130))
        self.planned_table.setObjectName("tableWidget")
        self.condition_watching = QtWidgets.QLabel(widget)
        self.condition_watching.setGeometry(QtCore.QRect(10, 180, 110, 20))
        self.condition_watching.setObjectName("condition_watching")
        self.condition_watched = QtWidgets.QLabel(widget)
        self.condition_watched.setGeometry(QtCore.QRect(10, 350, 110, 20))
        self.condition_watched.setObjectName("condition_watched")
        self.watching_table = QtWidgets.QTableWidget(widget)
        self.watching_table.setGeometry(QtCore.QRect(10, 210, 540, 130))
        self.watching_table.setObjectName("watching_table")
        self.watched_table = QtWidgets.QTableWidget(widget)
        self.watched_table.setGeometry(QtCore.QRect(10, 380, 540, 130))
        self.watched_table.setObjectName("watched_table")
        self.postponed_table = QtWidgets.QTableWidget(widget)
        self.postponed_table.setGeometry(QtCore.QRect(10, 550, 540, 130))
        self.postponed_table.setObjectName("postponed_table")
        self.abandoned_table = QtWidgets.QTableWidget(widget)
        self.abandoned_table.setGeometry(QtCore.QRect(10, 720, 540, 130))
        self.abandoned_table.setObjectName("abandoned_table")
        self.condition_postponed = QtWidgets.QLabel(widget)
        self.condition_postponed.setGeometry(QtCore.QRect(10, 520, 110, 20))
        self.condition_postponed.setObjectName("condition_postponed")
        self.condition_abandoned = QtWidgets.QLabel(widget)
        self.condition_abandoned.setGeometry(QtCore.QRect(10, 690, 110, 20))
        self.condition_abandoned.setObjectName("condition_abandoned")
        self.add = QtWidgets.QLabel(widget)
        self.add.setGeometry(QtCore.QRect(563, 10, 140, 20))
        self.add.setObjectName("add")
        self.add_title = QtWidgets.QLabel(widget)
        self.add_title.setGeometry(QtCore.QRect(663, 40, 65, 20))
        self.add_title.setObjectName("add_title")
        self.add_rating = QtWidgets.QLabel(widget)
        self.add_rating.setGeometry(QtCore.QRect(652, 70, 73, 20))
        self.add_rating.setObjectName("add_rating")
        self.add_watched_series = QtWidgets.QLabel(widget)
        self.add_watched_series.setGeometry(QtCore.QRect(563, 100, 162, 20))
        self.add_watched_series.setObjectName("add_watched_series")
        self.add_movie_type = QtWidgets.QLabel(widget)
        self.add_movie_type.setGeometry(QtCore.QRect(607, 130, 117, 20))
        self.add_movie_type.setObjectName("add_movie_type")
        self.add_condition = QtWidgets.QLabel(widget)
        self.add_condition.setGeometry(QtCore.QRect(618, 160, 110, 20))
        self.add_condition.setObjectName("add_condition")
        self.title_write = QtWidgets.QLineEdit(widget)
        self.title_write.setGeometry(QtCore.QRect(735, 40, 200, 20))
        self.title_write.setObjectName("title_write")
        self.rating_write = QtWidgets.QLineEdit(widget)
        self.rating_write.setGeometry(QtCore.QRect(735, 70, 200, 20))
        self.rating_write.setObjectName("rating_write")
        self.watched_series_write = QtWidgets.QLineEdit(widget)
        self.watched_series_write.setGeometry(QtCore.QRect(735, 100, 200, 20))
        self.watched_series_write.setObjectName("watched_series_write")
        self.movie_type_write = QtWidgets.QComboBox(widget)
        self.movie_type_write.setGeometry(QtCore.QRect(735, 130, 200, 20))
        self.movie_type_write.setObjectName("movie_type_write")
        self.movie_type_write.addItems(["film", "serial"])
        self.condition_write = QtWidgets.QComboBox(widget)
        self.condition_write.setGeometry(QtCore.QRect(735, 160, 200, 20))
        self.condition_write.setObjectName("condition_write")
        self.add_button = QtWidgets.QPushButton(widget)
        self.add_button.setGeometry(QtCore.QRect(750, 190, 90, 30))
        self.remove_button = QtWidgets.QPushButton(widget)
        self.remove_button.setGeometry(QtCore.QRect(845, 190, 90, 30))
        self.remove_button.setObjectName("remove_button")
        self.add_button.setObjectName("add_button")
        self.info = QtWidgets.QLabel(widget)
        self.info.setGeometry(QtCore.QRect(560, 260, 55, 20))
        self.info.setObjectName("info")
        self.info_title_write = QtWidgets.QLineEdit(widget)
        self.info_title_write.setGeometry(QtCore.QRect(735, 290, 200, 20))
        self.info_title_write.setObjectName("info_title_write")
        self.info_title = QtWidgets.QLabel(widget)
        self.info_title.setGeometry(QtCore.QRect(665, 290, 65, 20))
        self.info_title.setObjectName("info_title")
        self.info_rating = QtWidgets.QLabel(widget)
        self.info_rating.setGeometry(QtCore.QRect(653, 320, 80, 20))
        self.info_rating.setObjectName("info_rating")
        self.info_description = QtWidgets.QLabel(widget)
        self.info_description.setGeometry(QtCore.QRect(598, 410, 130, 20))
        self.info_description.setObjectName("info_description")
        self.info_genres = QtWidgets.QLabel(widget)
        self.info_genres.setGeometry(QtCore.QRect(652, 350, 80, 20))
        self.info_genres.setObjectName("info_genres")
        self.info_year = QtWidgets.QLabel(widget)
        self.info_year.setGeometry(QtCore.QRect(674, 380, 52, 20))
        self.info_year.setObjectName("info_year")
        self.rating_place = QtWidgets.QLabel(widget)
        self.rating_place.setGeometry(QtCore.QRect(735, 320, 200, 20))
        self.rating_place.setText("")
        self.rating_place.setObjectName("rating_place")
        self.genres_place = QtWidgets.QLabel(widget)
        self.genres_place.setGeometry(QtCore.QRect(735, 350, 200, 20))
        self.genres_place.setText("")
        self.genres_place.setObjectName("genres_place")
        self.description_place = QtWidgets.QTextBrowser(widget)
        self.description_place.setGeometry(QtCore.QRect(598, 440, 337, 370))
        self.description_place.setObjectName("description_place")
        self.year_place = QtWidgets.QLabel(widget)
        self.year_place.setGeometry(QtCore.QRect(735, 380, 200, 20))
        self.year_place.setText("")
        self.year_place.setObjectName("genres_place")
        self.update_button = QtWidgets.QPushButton(widget)
        self.update_button.setGeometry(QtCore.QRect(750, 820, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.add.setFont(font)
        self.update_button.setFont(font)
        self.condition_watching.setFont(font)
        self.condition_watched.setFont(font)
        self.condition_postponed.setFont(font)
        self.condition_abandoned.setFont(font)
        self.add_watched_series.setFont(font)
        self.add_movie_type.setFont(font)
        self.add_rating.setFont(font)
        self.add_title.setFont(font)
        self.add_title.setFont(font)
        self.add_condition.setFont(font)
        self.remove_button.setFont(font)
        self.info.setFont(font)
        self.info_title.setFont(font)
        self.info_rating.setFont(font)
        self.info_description.setFont(font)
        self.info_genres.setFont(font)
        self.condition_abandoned.setFont(font)
        self.add_button.setFont(font)
        self.info_button = QtWidgets.QPushButton(widget)
        self.info_button.setGeometry(QtCore.QRect(845, 820, 90, 30))
        self.condition_planned.setFont(font)
        self.info_button.setFont(font)
        self.info_year.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.planned_table.setFont(font)
        self.watching_table.setFont(font)
        self.watched_table.setFont(font)
        self.postponed_table.setFont(font)
        self.abandoned_table.setFont(font)
        self.movie_type_write.setFont(font)
        self.condition_write.setFont(font)
        self.title_write.setFont(font)
        self.rating_write.setFont(font)
        self.rating_place.setFont(font)
        self.genres_place.setFont(font)
        self.description_place.setFont(font)
        self.watched_series_write.setFont(font)
        self.info_title_write.setFont(font)
        self.description_place.setFont(font)
        self.update_button.setObjectName("update_button")
        self.planned_table.setColumnCount(4)
        self.watching_table.setColumnCount(4)
        self.watched_table.setColumnCount(4)
        self.postponed_table.setColumnCount(4)
        self.abandoned_table.setColumnCount(4)
        self.headers = ["Title", "Rating", "Watched Series", "Movie type"]
        self.planned_table.setHorizontalHeaderLabels(self.headers)
        self.watching_table.setHorizontalHeaderLabels(self.headers)
        self.watched_table.setHorizontalHeaderLabels(self.headers)
        self.postponed_table.setHorizontalHeaderLabels(self.headers)
        self.abandoned_table.setHorizontalHeaderLabels(self.headers)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Your Trip"))
        self.condition_planned.setText(_translate("widget", "Planned:"))
        self.condition_watching.setText(_translate("widget", "Watching:"))
        self.condition_watched.setText(_translate("widget", "Watched:"))
        self.condition_postponed.setText(_translate("widget", "Postponed:"))
        self.condition_abandoned.setText(_translate("widget", "Abandoned:"))
        self.add.setText(_translate("widget", "Add/Remove:"))
        self.add_title.setText(_translate("widget", "Title:"))
        self.add_rating.setText(_translate("widget", "Rating:"))
        self.add_watched_series.setText(_translate("widget", "Watched series:"))
        self.add_movie_type.setText(_translate("widget", "Movie type:"))
        self.add_condition.setText(_translate("widget", "Condition:"))
        self.add_button.setText(_translate("widget", "Add"))
        self.remove_button.setText(_translate("widget", "Remove"))
        self.info.setText(_translate("widget", "Info:"))
        self.info_title.setText(_translate("widget", "Title:"))
        self.info_rating.setText(_translate("widget", "Rating:"))
        self.info_description.setText(_translate("widget", "Description:"))
        self.info_genres.setText(_translate("widget", "Genres:"))
        self.update_button.setText(_translate("widget", "Update"))
        self.info_button.setText(_translate("widget", "Info"))
        self.info_year.setText(_translate("widget", "Year:"))
