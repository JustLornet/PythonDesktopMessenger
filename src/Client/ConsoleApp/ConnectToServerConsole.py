import json
import socket
from Client import ConnectionConfig
from Client.Actions.ActionElements.TransferType import TransferType
from Client.Elements.UserInfoContainer import UserInfoContainer


class ConnectToServerConsole(object):
    login: str = "undefined"

    def connect_to_server(self):
        server_host, server_port = ConnectionConfig.host, ConnectionConfig.port
        current_user = UserInfoContainer()
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as user_socket:
                user_socket.connect((server_host, server_port))
                # data_to_transfer = DataFormer.DataFormer()
                # выбор действия
                print(f"Actions: {TransferType.Registration}, {TransferType.Authorization},"
                      f"{TransferType.MessageRequest}, {TransferType.MessageSending}, {TransferType.GetAllUsers},"
                      f"{TransferType.GetOnlineUsers}, Sign out")
                # ввод данных пользователем
                action: str = input("Choose action: ")
                if not (action == TransferType.Registration.__str__() or
                        action == TransferType.Authorization.__str__() or
                        action == TransferType.MessageRequest.__str__() or
                        action == TransferType.MessageSending.__str__() or
                        action == TransferType.GetAllUsers.__str__() or
                        action == TransferType.GetOnlineUsers.__str__() or action == "Sign out"):
                    print("Неверное действие")
                    continue
                if action == "Sign out":
                    current_user.clear_user()
                    continue
                if (not action == TransferType.GetAllUsers.__str__() and
                    not action == TransferType.GetOnlineUsers.__str__()) and\
                        (not current_user.is_authorized()):
                    if action == TransferType.Registration.__str__() \
                            or action == TransferType.Authorization.__str__():
                        login: str = input("Set login: ")
                        current_user.set_new_user(login=login)
                    else:
                        print("Пожалуйста, авторизуйтесь")
                        continue
                action_handler = ActionHandlerConsoleApp(action, current_user)
                if action == TransferType.MessageSending.__str__():
                    addressee_to_send = input("Введите адресатов:")
                    message_to_send = input("Введите сообщение:")
                    action_handler.set_message(addressee_to_send.split(','), message_to_send)
                data_to_transfer = action_handler.handle_action()
                # отправка сообщения на сервер
                to_send = json.dumps(data_to_transfer, ensure_ascii=False).encode()
                user_socket.sendall(to_send)
                # получение ответа от сервера
                applied_data = str(user_socket.recv(1024), "utf-8")
                parsed_data = json.loads(applied_data)
                # если авторизация или регистрация, обновляем пользователя
                if action == TransferType.Registration.__str__() or action == TransferType.Authorization.__str__():
                    current_user.set_new_user(data_to_transfer["login"], parsed_data["user_id"])
                elif action == TransferType.MessageRequest.__str__():
                    self.__print_dict(parsed_data["message_archive"])
                elif action == TransferType.GetAllUsers.__str__():
                    self.__print_dict(parsed_data["all_users"])
                elif action == TransferType.GetOnlineUsers.__str__():
                    self.__print_dict(parsed_data["all_users_online"])

    def __print_dict(self, to_print: dict):
        for i in range(0, to_print.__len__()):
            print(to_print.popitem())




