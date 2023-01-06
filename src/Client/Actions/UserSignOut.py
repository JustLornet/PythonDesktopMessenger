from Client.Elements.TransferBaseObject import TransferBaseObject
from Client.Actions.ActionElements.TransferType import TransferType


class UserSignOut(TransferBaseObject):
    def __init__(self, login: str):
        super().__init__(TransferType.SignOut, login)

    def get_data_to_send(self):
        data_to_send: dict = super().get_data_to_send()

        return data_to_send
