from PyQt5 import QtCore
from db_handler import auth, reg


class CheckThread(QtCore.QThread):
    # Инициализация сигнала
    mysignal = QtCore.pyqtSignal(str)

    # Функции для аутентификации и регистрации
    def thr_auth(self, login, password):
        auth(login, password, self.mysignal)

    def thr_register(self, login, password):
        reg(login, password, self.mysignal)
