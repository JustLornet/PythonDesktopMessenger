from Client.Actions.ActionElements.TransferType import TransferType
from Client.Actions.ActionElements.RequestType import RequestType
import socket
from datetime import datetime


class TransferBaseObject:
    def __init__(self, transfer_type: TransferType, login: str = ""):
        self.__transfer_type = transfer_type
        self.__login = login

    request_from_server: str = ""

    def get_send_type(self):
        return self.__transfer_type

    def get_login(self):
        return self.__login

    def get_data_to_send(self):
        data_to_send: dict = {
            "transfer_type": str(self.__transfer_type),
            "ip": socket.gethostbyname(socket.gethostname()),
            "login": self.__login,
            "action_time": datetime.now().__str__(),
        }

        return data_to_send

    def handle_server_request(self) -> (RequestType, str):
        if self.request_from_server == "":
            return RequestType.Empty, ""
