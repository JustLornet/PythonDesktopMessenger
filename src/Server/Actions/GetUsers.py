from Server.DTOs.SenderInfo import SenderInfo
from Server.Database.DbManager import DbManager
from Server.Database.DbQueries import DbQueries


class GetUsers:
    def __init__(self, db_manager: DbManager):
        self.__db_manager = db_manager

    __all_users: dict = {"Login": "LastOnline#@RegistrationTime"}
    __all_users_online: dict = {"Login": "LastOnline"}

    def get_all_users(self) -> dict:
        self.__all_users.clear()
        self.__all_users_online.clear()
        query = DbQueries.get_all_users_info()
        users = self.__db_manager.get_data(query)
        for el in users:
            self.__all_users.update({
                el[0]: f"online - {el[1]} | registration - {el[2]}",
            })

        return self.__all_users

    def get_online_users(self) -> dict:
        query = DbQueries.get_online_users()
        users = self.__db_manager.get_data(query)
        for el in users:
            self.__all_users_online.update({
                el[0]: f"{el[1]}",
            })

        return self.__all_users_online
