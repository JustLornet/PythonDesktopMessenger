import json
import socket
from Client import ConnectionConfig
from Client.Actions.ActionElements.TransferType import TransferType
from Client.DesktopApp.DataHandling.ActionHandler import ActionHandler
from Client.Elements.UserInfoContainer import UserInfoContainer


class ConnectToServerDesktop(object):
    def __init__(self, user_info: UserInfoContainer):
        self.__user_info = user_info
        self.__action_handler = ActionHandler(user_info)

    def connect_to_server(self):
        server_host, server_port = ConnectionConfig.host, ConnectionConfig.port
        # Выполнение:
        # TODO: нормально оформить, разнести на методы
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as user_socket:
            user_socket.connect((server_host, server_port))
            data_to_transfer = self.__action_handler.handle_action()
            # отправка сообщения на сервер
            to_send = json.dumps(data_to_transfer, ensure_ascii=False).encode()
            user_socket.sendall(to_send)
            # получение ответа от сервера
            applied_data = str(user_socket.recv(2048), "utf-8")
            parsed_data = json.loads(applied_data)
            # получение всех доступных данных
            # авторизация пользователя
            if parsed_data["user_id"] > 0:
                self.__user_info.confirm_user(parsed_data["user_id"])
            elif self.__user_info.last_transfer_type == TransferType.Authorization or \
                    self.__user_info.last_transfer_type == TransferType.Registration:
                self.__user_info.clear_user()
            # список всех пользователей
            if parsed_data["all_users"].__len__() > 1:
                self.__user_info.last_data_to_send.users_db = parsed_data["all_users"]
            # список пользователей онлайн
            if parsed_data["all_users_online"].__len__() > 1:
                self.__user_info.last_data_to_send.users_db = parsed_data["all_users_online"]
            # история сообщения
            if parsed_data["message_archive"].__len__() > 1:
                self.__user_info.last_data_to_send.message_history = parsed_data["message_archive"]
