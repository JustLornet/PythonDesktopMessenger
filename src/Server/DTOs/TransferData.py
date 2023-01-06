class TransferData:
    def __init__(self, addressee: list, message: str):
        self.__addressee = addressee
        self.__message = message

    def get_data(self) -> (str, str):
        # TODO: переделать под отправку нескольким пользователям
        return self.__addressee, self.__message
