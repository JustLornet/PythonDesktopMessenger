from PyQt5.QtWidgets import QWidget, QDialog

from Client.Actions.ActionElements.TransferType import TransferType
from Client.DesktopApp.DataHandling.ActionHandler import ActionHandler
from Client.DesktopApp.ServerCommunication.ConnectToServerDesktop import ConnectToServerDesktop
from Client.DesktopApp.UI.Ui_AuthorizationWindow import Ui_AuthorizationWindow
from Client.Elements.UserInfoContainer import UserInfoContainer


class AuthorizationWindow(QDialog):
    def __init__(self, my_client: ConnectToServerDesktop, user_info: UserInfoContainer, parent=None):
        super().__init__(parent)

        self.__ui = Ui_AuthorizationWindow()
        self.__ui.setupUi(self)

        self.__my_client = my_client
        self.__user_info = user_info

        self.__ui.pushButton_Register.pressed.connect(self.__register_command)
        self.__ui.pushButton_SignIn.pressed.connect(self.__sign_in_command)

    def __register_command(self):
        login = self.__ui.lineEdit_Login.text()
        if login.__len__() > 0:
            self.__user_info.set_new_user(login)
            self.__user_info.last_transfer_type = TransferType.Registration
            self.__my_client.connect_to_server()
            if self.__user_info.is_authorized():
                self.close()

    def __sign_in_command(self):
        login = self.__ui.lineEdit_Login.text()
        self.__user_info.set_new_user(login)
        self.__user_info.last_transfer_type = TransferType.Authorization
        self.__my_client.connect_to_server()
        if self.__user_info.is_authorized():
            self.close()
