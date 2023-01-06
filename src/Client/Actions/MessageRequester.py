from Client.Elements.TransferBaseObject import TransferBaseObject
from Client.Actions.ActionElements.TransferType import TransferType
from Client.Elements.UserInfoContainer import UserInfoContainer


class MessageRequester(TransferBaseObject):
    def __init__(self, user_info: UserInfoContainer):
        super().__init__(TransferType.MessageRequest, user_info.login())
        self.__user_info = user_info

    def get_data_to_send(self) -> dict:
        data_to_send: dict = super().get_data_to_send()
        data_to_send.update({
            "user_id": self.__user_info.id()
        })

        return data_to_send
