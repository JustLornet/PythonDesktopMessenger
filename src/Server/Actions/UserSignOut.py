from Server.DTOs.SenderInfo import SenderInfo
from Server.Database.DbManager import DbManager
from Server.Database.DbQueries import DbQueries


class UserSignOut:
    def __init__(self, db_manager: DbManager):
        self.__db_manager = db_manager

    __user: SenderInfo

    def sign_out_user(self, user: SenderInfo):
        self.__user = user
        # ищем id пользователя
        query = DbQueries.get_users_id_through_login(self.__user.sender_login())
        user_id_unparsed = self.__db_manager.get_data(query)
        user_id_parsed = user_id_unparsed[0][0]
        # меняем его статус онлайн + дата последней активности
        query = DbQueries.sign_out_user(self.__user, user_id_parsed)
        self.__db_manager.set_changes(query)
