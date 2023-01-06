import datetime
import socket


class DataFormer:
    def __init__(self):
        self.__sender = socket.gethostbyname(socket.gethostname())
        self.__sender: str = "undefined"
        self.__addressee: list = ["undefined"]
        self.__message_to_send: str = ""
        self.__users_db: dict = {}
        self.__message_history: list = []

    @property
    def addressee(self):
        return self.__addressee

    @addressee.setter
    def addressee(self, value):
        self.__addressee = value

    @property
    def message_to_send(self):
        return self.__message_to_send

    @message_to_send.setter
    def message_to_send(self, value):
        self.__message_to_send = value

    @property
    def message_history(self) -> list:
        return self.__message_history

    @message_history.setter
    def message_history(self, unparsed_dict: dict):
        self.__message_history.clear()
        for el in unparsed_dict:
            sender, addressee, date = tuple(el.split("#@"))
            self.__message_history.append(f"{sender} --> {addressee}, {date}:\n{unparsed_dict[el]}\n")

    @property
    def users_db(self) -> dict:
        return self.__users_db

    @users_db.setter
    def users_db(self, value):
        self.__users_db.clear()
        self.__users_db = value

    def get_online_users(self) -> list:
        result_list: list = []
        # первый элемент - пояснение, нет информации
        if self.__users_db.__contains__("Login"):
            self.__users_db.pop("Login")
        for el in self.__users_db:
            item = f"{el}\nlast online - {self.__users_db[el]}"
            result_list.append(item)

        return result_list

    def get_all_users(self) -> list:
        result_list: list = []
        # первый элемент - пояснение, нет информации
        if self.__users_db.__contains__("Login"):
            self.__users_db.pop("Login")
        for el in self.__users_db:
            online, registration = tuple(self.__users_db[el].split(" | "))
            item = f"{el}\n{online}\n{registration}"
            result_list.append(item)

        return result_list

    def form_dict_to_send(self) -> dict:
        dict_to_send: dict = {
            "sender": self.__sender,
            "addressee": self.__addressee,
            "send_time": datetime.datetime.now().__str__(),
            "message": self.__message_to_send,
        }

        return dict_to_send
