from Client.Actions.ActionElements.TransferType import TransferType
from Client.Elements.TransferBaseObject import TransferBaseObject


class UserRegister(TransferBaseObject):
    def __init__(self, login: str):
        super().__init__(TransferType.Registration, login)

    def get_data_to_send(self):
        data_to_send: dict = super().get_data_to_send()

        return data_to_send
