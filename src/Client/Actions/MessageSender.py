from Client.Elements.TransferBaseObject import TransferBaseObject
from Client.Actions.ActionElements.TransferType import TransferType
from Client.Elements.UserInfoContainer import UserInfoContainer


class MessageSender(TransferBaseObject):
    def __init__(self, addressee: list, message: str, user_info: UserInfoContainer):
        super().__init__(TransferType.MessageSending, user_info.login())
        self.__addressee = addressee
        self.__message = message
        self.__user_info = user_info

    __addressee: list = ["undefined"]
    __message: str = ""

    def get_data_to_send(self) -> dict:
        data_to_send: dict = super().get_data_to_send()
        data_to_send.update({
            "user_id": self.__user_info.id(),
            "addressee": self.__addressee,
            "message": self.__message,
        })

        return data_to_send
