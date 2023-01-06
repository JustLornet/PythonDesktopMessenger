from Actions.ActionElements.TransferType import TransferType
from Elements.TransferBaseObject import TransferBaseObject
from Elements.UserInfoContainer import UserInfoContainer


class RequestHandler:
    def __init__(self, init_data: TransferBaseObject):
        self.__init_data = init_data

    __server_request: dict

    def handle_request(self, got_data: dict):
        self.__server_request = got_data
        transfer_type_name = self.__init_data.get_send_type().name
        if transfer_type_name == TransferType.Registration.name:
            UserInfoContainer.login = self.__server_request["login"]
            # TODO: прописать логику, что если такое имя уже существует, пользователь не авторизуется
        elif transfer_type_name == TransferType.Authorization.name:
            UserInfoContainer.login = self.__server_request["login"]
        elif transfer_type_name == TransferType.MessageRequest.name:
            return self.__server_request["message"]
        elif transfer_type_name == TransferType.MessageSending.name:
            pass
        elif transfer_type_name == TransferType.GetAllUsers.name:
            pass
        else:
            print("Command not recognized")

