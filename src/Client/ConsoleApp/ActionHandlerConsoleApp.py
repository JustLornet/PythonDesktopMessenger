from ConnectToServer.Actions.ActionElements.TransferType import TransferType
from ConnectToServer.Actions.MessageRequester import MessageRequester
from ConnectToServer.Actions.MessageSender import MessageSender
from ConnectToServer.Actions.UserAuthorizer import UserAuthorizer
from ConnectToServer.Actions.UserRegister import UserRegister
from ConnectToServer.Elements.TransferBaseObject import TransferBaseObject
from ConnectToServer.Elements.UserInfoContainer import UserInfoContainer


class ActionHandlerConsoleApp:
    def __init__(self, transfer_type: str, user_info: UserInfoContainer):
        self.__transfer_type = transfer_type
        self.__current_user_info = user_info
        self.__login = user_info.login()

    __addressee: list = ["undefined"]
    __message: str = "undefined"
    __init_data_container: TransferBaseObject

    def handle_action(self) -> dict:
        if self.__transfer_type == TransferType.Registration.__str__():
            return self.__register()
        elif self.__transfer_type == TransferType.Authorization.__str__():
            return self.__authorize()
        elif self.__transfer_type == TransferType.MessageRequest.__str__():
            return self.__get_messages()
        elif self.__transfer_type == TransferType.MessageSending.__str__():
            return self.__send_messages()
        elif self.__transfer_type == TransferType.GetAllUsers.__str__():
            return TransferBaseObject(TransferType.GetAllUsers).get_data_to_send()
        elif self.__transfer_type == TransferType.GetOnlineUsers.__str__():
            return TransferBaseObject(TransferType.GetOnlineUsers).get_data_to_send()
        else:
            print("Command not recognized")

    def set_message(self, addressee: list, message: str):
        self.__addressee = addressee
        self.__message = message

    def __register(self) -> dict:
        self.__init_data_container = UserRegister(self.__login)

        return self.__init_data_container.get_data_to_send()
        # TODO: проверка на то, получилось ли создать пользователя - по имеющимся логинам,
        #  если проверка выполнилась, вернуть логин:

    def __authorize(self) -> dict:
        self.__init_data_container = UserAuthorizer(self.__login)

        return self.__init_data_container.get_data_to_send()

    def __get_messages(self) -> dict:
        self.__init_data_container = MessageRequester(self.__current_user_info)

        return self.__init_data_container.get_data_to_send()

    def __send_messages(self) -> dict:
        self.__init_data_container = MessageSender(self.__addressee, self.__message, self.__current_user_info)

        return self.__init_data_container.get_data_to_send()

    def get_init_data(self):
        return self.__init_data_container
