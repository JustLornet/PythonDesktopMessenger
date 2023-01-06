from Client.Actions.ActionElements.TransferType import TransferType
from Client.Actions.MessageRequester import MessageRequester
from Client.Actions.MessageSender import MessageSender
from Client.Actions.UserAuthorizer import UserAuthorizer
from Client.Actions.UserRegister import UserRegister
from Client.Elements.TransferBaseObject import TransferBaseObject
from Client.Elements.UserInfoContainer import UserInfoContainer
from Client.Actions.UserSignOut import UserSignOut


class ActionHandler:
    def __init__(self, user_info: UserInfoContainer):
        self.__current_user_info = user_info

    __addressee: list = ["undefined"]
    __message: str = "undefined"
    __init_data_container: TransferBaseObject

    def handle_action(self) -> dict:
        transfer_type = self.__current_user_info.last_transfer_type
        if transfer_type == TransferType.Registration:
            return self.__register()
        elif transfer_type == TransferType.Authorization:
            return self.__authorize()
        elif transfer_type == TransferType.MessageRequest:
            return self.__get_messages()
        elif transfer_type == TransferType.MessageSending:
            return self.__send_messages()
        elif transfer_type == TransferType.GetAllUsers:
            return TransferBaseObject(TransferType.GetAllUsers).get_data_to_send()
        elif transfer_type == TransferType.GetOnlineUsers:
            return TransferBaseObject(TransferType.GetOnlineUsers).get_data_to_send()
        elif transfer_type == TransferType.SignOut:
            return self.__sign_out()
        else:
            print("Command not recognized")

    def set_message(self, addressee: list, message: str):
        self.__addressee = addressee
        self.__message = message

    def __register(self) -> dict:
        self.__init_data_container = UserRegister(self.__current_user_info.login())

        return self.__init_data_container.get_data_to_send()
        # TODO: проверка на то, получилось ли создать пользователя - по имеющимся логинам,
        #  если проверка выполнилась, вернуть логин:

    def __authorize(self) -> dict:
        self.__init_data_container = UserAuthorizer(self.__current_user_info.login())

        return self.__init_data_container.get_data_to_send()

    def __sign_out(self) -> dict:
        self.__init_data_container = UserSignOut(self.__current_user_info.login())

        return self.__init_data_container.get_data_to_send()

    def __get_messages(self) -> dict:
        self.__init_data_container = MessageRequester(self.__current_user_info)

        return self.__init_data_container.get_data_to_send()

    def __send_messages(self) -> dict:
        self.__addressee = self.__current_user_info.last_data_to_send.addressee
        self.__message = self.__current_user_info.last_data_to_send.message_to_send
        self.__init_data_container = MessageSender(self.__addressee, self.__message, self.__current_user_info)

        return self.__init_data_container.get_data_to_send()

    def get_init_data(self):
        return self.__init_data_container
