from Server.Actions.GetUserAllMessageHistory import GetUserAllMessageHistory
from Server.Actions.GetUsers import GetUsers
from Server.Actions.ServerResponse.ResponseContainer import ResponseContainer
from Server.Actions.UserAuthorizer import UserAuthorizer
from Server.Actions.UserMessageIntoDb import UserMessageIntoDb
from Server.Actions.UserRegister import UserRegister
from Server.Actions.UserSignOut import UserSignOut
from Server.DTOs.SenderInfo import SenderInfo
from Server.DTOs.TransferType import TransferType
from Server.Database.DbManager import DbManager


class RequestHandler:
    def __init__(self, db_manager: DbManager):
        # инициализировать обработчик для бд:
        self.__db_manager = db_manager
        # инициализировать действия:
        self.__user_register = UserRegister(db_manager)
        self.__user_authorizer = UserAuthorizer(db_manager)
        self.__user_sign_out = UserSignOut(db_manager)
        self.__user_message_into_db = UserMessageIntoDb(db_manager)
        self.__get_user_message_history = GetUserAllMessageHistory(db_manager)
        self.__get_users = GetUsers(db_manager)

        self.__user: SenderInfo
        self.__user_id: int = -1
        self.__addressee_id: int = -1
        # TODO: пересылать всю историю сообщений - слишком затратно, пересылать всего раз - при авторизации,
        #  потом слать только новые сообщения, а историю хранить на клиенте, но чистить при выходе
        self.__message_history: dict = {"Sender#@Addressee#@Date": "Message"}
        self.__all_users: dict = {"Login": "LastOnline#@RegistrationTime"}
        self.__all_users_online: dict = {"Login": "LastOnline"}

    def __handle_request(self):
        self.__init_dicts()
        trans_name = self.__user.transfer_type().name
        if trans_name == TransferType.Registration.name:
            self.__register_user()
        elif trans_name == TransferType.Authorization.name:
            self.__authorize()
        elif trans_name == TransferType.MessageRequest.name:
            self.__get_messages()
        elif trans_name == TransferType.MessageSending.name:
            self.__send_message()
        elif trans_name == TransferType.GetAllUsers.name:
            self.__get_all_users()
        elif trans_name == TransferType.GetOnlineUsers.name:
            self.__get_online_users()
        elif trans_name == TransferType.SignOut.name:
            self.__sign_out()
        else:
            print("Command not recognized")
    
    def execute_give_response(self, current_user: SenderInfo) -> ResponseContainer:
        self.__user = current_user
        self.__handle_request()
        # TODO: конструктор не должен быть таким длинным - передавать только те аргументы, которые нужны -
        #  в зависимости от запроса, и передавать клиенту только нужные
        server_response = ResponseContainer(user_id=self.__user_id, addressee_id=self.__addressee_id,
                                            message_history=self.__message_history, all_users=self.__all_users,
                                            all_users_online=self.__all_users_online)

        return server_response

    def __register_user(self):
        self.__user_id = self.__user_register.register_user(self.__user)
        if self.__user_id > 0:
            self.__authorize()

    def __authorize(self):
        self.__user_id = self.__user_authorizer.authorize_user(self.__user)

    def __sign_out(self):
        self.__user_sign_out.sign_out_user(self.__user)

    def __send_message(self):
        self.__addressee_id = self.__user_message_into_db.save_message_to_db(self.__user)

    def __get_messages(self):
        self.__message_history = self.__get_user_message_history.get_full_message_history(self.__user)

    def __get_all_users(self):
        self.__all_users = self.__get_users.get_all_users()

    def __get_online_users(self):
        self.__all_users_online = self.__get_users.get_online_users()

    def __init_dicts(self):
        self.__message_history: dict = {"Sender#@Addressee#@Date": "Message"}
        self.__all_users: dict = {"Login": "LastOnline#@RegistrationTime"}
        self.__all_users_online: dict = {"Login": "LastOnline"}
