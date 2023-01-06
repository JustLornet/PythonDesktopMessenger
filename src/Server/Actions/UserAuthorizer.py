from Server.DTOs.SenderInfo import SenderInfo
from Server.Database.DbManager import DbManager
from Server.Database.DbQueries import DbQueries


class UserAuthorizer:
    def __init__(self, db_manager: DbManager):
        self.__db_manager = db_manager

    __user: SenderInfo
    __is_login_exist: bool

    def __check_existing_logins(self):
        query = DbQueries.get_all_users_logins()
        all_logins = self.__db_manager.get_data(query)
        for el in all_logins:
            if el[0] == self.__user.sender_login():
                self.__is_login_exist = True
                break
        else:
            self.__is_login_exist = False

    def authorize_user(self, user: SenderInfo) -> int:
        self.__user = user
        self.__check_existing_logins()
        if self.__is_login_exist:
            # ищем id пользователя
            query = DbQueries.get_users_id_through_login(self.__user.sender_login())
            user_id_unparsed = self.__db_manager.get_data(query)
            user_id_parsed = user_id_unparsed[0][0]
            # меняем его статус онлайн + дата последней активности
            query = DbQueries.authorize_user(self.__user, user_id_parsed)
            self.__db_manager.set_changes(query)

            return user_id_parsed
        return -1
