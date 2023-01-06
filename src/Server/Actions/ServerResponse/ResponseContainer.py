class ResponseContainer:
    def __init__(self, user_id: int = -1, addressee_id: int = -1, new_message: str = "",
                 message_history={"": ""}, all_users={"": ""}, all_users_online={"": ""}):
        self.__user_id = user_id
        self. __addressee_id = addressee_id
        self.__new_message = new_message
        self.__message_history = message_history
        self.__all_users = all_users
        self.__all_users_online = all_users_online

    def get_dict(self) -> dict:
        dict_to_send = {
            "user_id": self.__user_id,
            "addressee_id": self.__addressee_id,
            "new_message": self.__new_message,
            "message_archive": self.__message_history,
            "all_users": self.__all_users,
            "all_users_online": self.__all_users_online,
        }

        return dict_to_send
