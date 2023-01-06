from enum import Enum


class TransferType(Enum):
    Registration = 1
    Authorization = 2
    MessageRequest = 3
    MessageSending = 4
    GetAllUsers = 5
    Undefined = 6
    GetOnlineUsers = 7
    SignOut = 8

