import sys

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from authorization_window_gui import Ui_Form
from db_handler import LOGIN

from check_db import CheckThread




class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Привязка функций к кнопкам 
        self.items = [self.lineEdit, self.lineEdit_2]
        self.pushButton.clicked.connect(self.sign_in)
        self.pushButton_2.clicked.connect(self.sign_up)
        
        # Инициализация сигнала, для получения информации с нижних уровней
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
    
    
    # Обработчик сигнала
    def signal_handler(self, value):
        QMessageBox.about(self, 'Оповещение', value)
    
    # Декоратор, проверяющий ввод на валидность
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.items:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    # Данные пользователя
    def user_info(self):
        return self.items[0].text(), self.items[1].text()


    # Вызов фунций нижнего уровня при входе
    @check_input
    def sign_in(self):
        self.check_db.thr_auth(self.user_info()[0], self.user_info()[1])
    
    # Вызов фунций нижнего уровня при регистрации
    @check_input
    def sign_up(self):
        self.check_db.thr_register(self.user_info()[0], self.user_info()[1])
