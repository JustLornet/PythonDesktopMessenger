from Server.DTOs.SenderInfo import SenderInfo
from Server.Database.DbManager import DbManager
from Server.Database.DbQueries import DbQueries


class UserMessageIntoDb:
    def __init__(self, db_manager: DbManager):
        self.__db_manager = db_manager

    __user: SenderInfo
    __addressee_id: int = -1

    def save_message_to_db(self, user: SenderInfo) -> int:
        self.__user = user
        self.__get_addressee_id()
        query = DbQueries.set_messages(self.__user, self.__addressee_id)
        self.__db_manager.set_changes(query)

        return self.__addressee_id

    def __get_addressee_id(self):
        addressee, message = self.__user.transfer_data().get_data()
        query = DbQueries.get_users_id_through_login(addressee)
        self.__addressee_id = self.__db_manager.get_data(query)[0][0]
