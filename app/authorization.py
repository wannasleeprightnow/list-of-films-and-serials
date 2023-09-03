import sys

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from gui.authorization_window_gui import Ui_Form

from db.db import fetch_all, execute
from db.sql import select_user_data, insert_user_data

USER_ID = None


def ret_user_id():
    return USER_ID


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.items = [self.lineEdit, self.lineEdit_2]
        self.pushButton.clicked.connect(self.sign_in)
        self.pushButton_2.clicked.connect(self.sign_up)

    def sign_in(self):
        global USER_ID

        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        if not 0 in (len(login), len(password)):
            user = fetch_all(select_user_data, (login,))
            if user and user[0]["password"] == password:
                QMessageBox.about(self, "Sign In", "Вы вошли в свой аккаунт.")
                USER_ID = int(user[0]["id"])
            else:
                QMessageBox.about(self, "Sign In", "Введены неверные данные.")

    def sign_up(self):
        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        if not 0 in (len(login), len(password)):
            user = fetch_all(select_user_data, (login,))
            if user:
                QMessageBox.about(self, "Sign Up", "Такой пользователь уже существует.")
            else:
                execute(insert_user_data, (login, password))
                QMessageBox.about(self, "Sign Up", "Вы успешно зарегистрировались.")
