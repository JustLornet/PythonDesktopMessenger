import enum
from datetime import datetime

from Server.DTOs.TransferData import TransferData
from Server.DTOs.TransferType import TransferType


class SenderInfo:
    __transfer_type: TransferType = TransferType.Undefined
    __sender_ip: str = "undefined"
    __sender_login: str = "undefined"
    __action_time: datetime
    __transfer_data: TransferData = None
    __sender_id: int = -1

    def fill_data(self, request_data: dict):
        self.__transfer_type = self.__transfer_type_parse(request_data["transfer_type"])
        self.__sender_ip = request_data["ip"]
        self.__sender_login = request_data["login"]
        self.__action_time = datetime.strptime(request_data["action_time"], "%Y-%m-%d %H:%M:%S.%f")
        if self.__transfer_type == TransferType.MessageSending:
            self.__transfer_data = TransferData(request_data["addressee"], request_data["message"])
            self.__sender_id = request_data["user_id"]
        elif self.__transfer_type == TransferType.MessageRequest:
            self.__sender_id = request_data["user_id"]

        return self

    def handle_transfer_type(self):
        if self.__transfer_type == TransferType.Registration:
            pass
        elif self.__transfer_type == TransferType.Authorization:
            pass
        elif self.__transfer_type == TransferType.MessageRequest:
            pass
        elif self.__transfer_type == TransferType.MessageSending:
            pass
        elif self.__transfer_type == TransferType.UserDeleting:
            pass
        elif self.__transfer_type == TransferType.Undefined:
            pass

    def transfer_type(self):
        return self.__transfer_type

    def sender_ip(self):
        return self.__sender_ip

    def sender_id(self):
        return self.__sender_id

    def sender_login(self):
        return self.__sender_login

    def action_time(self):
        return self.__action_time

    def transfer_data(self):
        return self.__transfer_data

    def __transfer_type_parse(self, trans_type_not_parsed: str) -> TransferType:
        for el in TransferType:
            if str(el) == trans_type_not_parsed:
                return el
