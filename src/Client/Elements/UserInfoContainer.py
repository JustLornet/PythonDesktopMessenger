from Client.Actions.ActionElements.TransferType import TransferType
from Client.Elements.DataFormer import DataFormer


class UserInfoContainer:
    def __init__(self):
        self.__login: str = ""
        self.__id: int = -1
        # проверка - произошла ли авторизация пользователя, если да - вместо логина оперируем id
        self.__is_authorized: bool = False
        self.__last_transfer_type: TransferType = TransferType.Undefined
        self.__last_data_to_send: DataFormer = DataFormer()

    def set_new_user(self, login: str, user_id: int = -1):
        self.__id = user_id
        self.__login = login

    def confirm_user(self, user_id: int):
        self.__id = user_id

    def login(self) -> str:
        return self.__login

    def id(self) -> int:
        return self.__id

    def is_authorized(self) -> bool:
        if self.__id > 0:
            return True
        else:
            return False

    @property
    def last_transfer_type(self):
        return self.__last_transfer_type

    @last_transfer_type.setter
    def last_transfer_type(self, value):
        self.__last_transfer_type = value

    @property
    def last_data_to_send(self) -> DataFormer:
        return self.__last_data_to_send

    @last_data_to_send.setter
    def last_data_to_send(self, value: DataFormer):
        self.__last_data_to_send = value

    def clear_user(self):
        self.__id = -1
        self.__login = ""
        self.__last_transfer_type: TransferType = TransferType.Undefined
        self.__last_data_to_send: DataFormer = DataFormer()
