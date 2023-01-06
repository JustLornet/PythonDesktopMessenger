import threading
import time
from time import sleep

import PyQt5.QtGui
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication

from Client.Actions.ActionElements.TransferType import TransferType
from Client.DesktopApp.DataHandling.ActionHandler import ActionHandler
from Client.DesktopApp.ServerCommunication.ConnectToServerDesktop import ConnectToServerDesktop
from Client.DesktopApp.UI.AuthorizationWindow import AuthorizationWindow
from Client.DesktopApp.UI.Ui_MainWindow import Ui_MainWindow
from Client.Elements.UserInfoContainer import UserInfoContainer


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Привязка формы
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        # Кнопки
        self.__ui.pushButton_SignOut.pressed.connect(self.__sign_out_command)
        self.__ui.pushButton_SendMessage.pressed.connect(self.__send_message_command)
        self.__ui.radioButton_AllUsers.pressed.connect(self.__get_all_users_command)
        self.__ui.radioButton_UsersOnline.pressed.connect(self.__get_online_users_command)
        # Общие ресурсы
        self.__user_info = UserInfoContainer()
        self.__my_client = ConnectToServerDesktop(self.__user_info)
        self.__authorization_window = AuthorizationWindow(self.__my_client, self.__user_info)
        self.__list_view_users_model = PyQt5.QtGui.QStandardItemModel()
        self.__ui.listView_Users.setModel(self.__list_view_users_model)
        self.__list_view_messages_model = PyQt5.QtGui.QStandardItemModel()
        self.__ui.listView_MessageHistory.setModel(self.__list_view_messages_model)
        self.__remember_index = self.__ui.listView_Users.currentIndex()
        # Авторизация пользователя
        self.__sign_out_command()
        # Поток получения сообщений
        self.__time_sleep = 2
        self.__is_continue_getting_messages = True
        threading.Thread(target=self.__get_messages_command).start()
        # При закрытии окна
        self.__my_close = False

    def __sign_out_command(self):
        self.__clear_all()
        while not self.__user_info.is_authorized():
            self.__authorization_window.exec()
        else:
            self.__is_continue_getting_messages = True
            threading.Thread(target=self.__get_messages_command).start()

    def __send_message_command(self):
        selected_user = self.__ui.listView_Users.currentIndex().data()
        if selected_user is None:
            selected_user = self.__remember_user
        selected_user_login = selected_user.split("\n")[0]
        message = self.__ui.lineEdit_SendMessageField.text()
        if message.__len__() > 0 and selected_user_login.__len__() > 0:
            self.__user_info.last_transfer_type = TransferType.MessageSending
            self.__user_info.last_data_to_send.addressee = selected_user_login
            self.__user_info.last_data_to_send.message_to_send = message
            self.__my_client.connect_to_server()
            self.__ui.lineEdit_SendMessageField.clear()

    def __get_all_users_command(self):
        self.__time_sleep = 2
        self.__user_info.last_transfer_type = TransferType.GetAllUsers
        self.__my_client.connect_to_server()
        self.__fill_users_model(self.__user_info.last_data_to_send.get_all_users())
        self.__is_continue_getting_users = False

    def __get_online_users_command(self):
        # Поток получения пользователей
        self.__time_sleep = 0.3
        self.__is_continue_getting_users = True
        threading.Thread(target=self.__online_users_thread_command).start()

    def __get_messages_command(self):
        while threading.main_thread().is_alive() and self.__is_continue_getting_messages:
            if self.__user_info.is_authorized():
                self.__user_info.last_transfer_type = TransferType.MessageRequest
                self.__my_client.connect_to_server()
                self.__fill_message_history()
                time.sleep(self.__time_sleep)
            else:
                continue

    def __online_users_thread_command(self):
        while threading.main_thread().is_alive() and self.__is_continue_getting_users:
            if self.__user_info.is_authorized():
                selected_user = self.__ui.listView_Users.currentIndex().data()
                if selected_user is not None:
                    self.__remember_user = selected_user
                self.__user_info.last_transfer_type = TransferType.GetOnlineUsers
                self.__my_client.connect_to_server()
                self.__fill_users_model(self.__user_info.last_data_to_send.get_online_users())
                self.__ui.listView_MessageHistory.scrollToBottom()
                time.sleep(1)
            else:
                continue

    def __fill_users_model(self, to_fill: list):
        self.__list_view_users_model.clear()
        for el in to_fill:
            item = PyQt5.QtGui.QStandardItem(el)
            self.__list_view_users_model.appendRow(item)

    def __fill_message_history(self):
        self.__list_view_messages_model.clear()
        self.__user_info.last_data_to_send.message_history.reverse()
        for el in self.__user_info.last_data_to_send.message_history:
            item = PyQt5.QtGui.QStandardItem(el)
            self.__list_view_messages_model.appendRow(item)

    def __clear_all(self):
        self.__is_continue_getting_messages = False
        # Выход из аккаунта
        if self.__user_info.is_authorized():
            self.__user_info.last_transfer_type = TransferType.SignOut
            self.__my_client.connect_to_server()
        # Чистка всех полей/сущностей
        self.__user_info.clear_user()
        self.__list_view_messages_model.clear()
        self.__list_view_users_model.clear()
        self.__ui.lineEdit_SendMessageField.clear()

    def __close_event(self, event):
        if self.__my_close:
            self.__user_info.last_transfer_type = TransferType.SignOut
            self.__my_client.connect_to_server()
        else:
            event.ignore()
