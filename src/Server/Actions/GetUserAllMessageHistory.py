from Server.DTOs.SenderInfo import SenderInfo
from Server.Database.DbManager import DbManager
from Server.Database.DbQueries import DbQueries


class GetUserAllMessageHistory:
    def __init__(self, db_manager: DbManager):
        self.__db_manager = db_manager

    __user: SenderInfo
    __addressee_id: int = -1
    __message_history: dict = {"Sender#@Addressee#@Date": "Message"}
    __users_id_login: dict = {"ID": "Login"}

    def get_full_message_history(self, user: SenderInfo) -> dict:
        self.__message_history.clear()
        self.__users_id_login.clear()
        self.__user = user
        self.__get_users_dict()
        query = DbQueries.get_all_user_messages(self.__user)
        messages = self.__db_manager.get_data(query)
        for el in messages:
            self.__message_history.update({
                f"{self.__users_id_login[el[3]]}#@{self.__users_id_login[el[4]]}#@{el[2]}": el[1],
            })

        return self.__message_history

    def __get_users_dict(self):
        query = DbQueries.get_all_id_login_relations()
        not_parsed = self.__db_manager.get_data(query)
        for el in not_parsed:
            self.__users_id_login.update({
                el[0]: el[1],
            })
