import datetime

from Server.DTOs.SenderInfo import SenderInfo


class DbQueries:
    @staticmethod
    def get_users_through_user(user: SenderInfo):
        query = f"""
        select * from Users
        where Login = '{user.sender_login()}'"""

        return query

    @staticmethod
    def get_users_id_through_login(login: str):
        query = f"""
            select UserID from Users
            where Login = '{login}'"""

        return query

    @staticmethod
    def get_online_users():
        query = """
        select Login, LastOnline from Users
        where IsOnline = 1"""

        return query

    @staticmethod
    def get_all_users_info():
        query = """
            select Login, LastOnline, RegistrationDatetime from Users"""

        return query

    @staticmethod
    def get_all_user_messages(user: SenderInfo):
        query = f"""
                    select * from Messages
                    where SenderID = '{user.sender_id()}' or AddresseeID = '{user.sender_id()}'"""

        return query

    @staticmethod
    def get_all_id_login_relations():
        query = """
            select UserID, Login from Users"""

        return query

    @staticmethod
    def set_messages(user: SenderInfo, addressee_id: int):
        addressee, message = user.transfer_data().get_data()
        query = f"""
                insert into Messages (Message, SendTime, SenderID, AddresseeID)
                values ('{message}', convert(datetime, '{user.action_time().strftime("%Y-%m-%d %H:%M:%S")}', 120),
                {user.sender_id()}, {addressee_id})"""

        return query

    @staticmethod
    def add_user(user: SenderInfo):
        query = f"""
        insert into Users (Login, LastOnline, RegistrationDatetime, IsOnline)
        values ('{user.sender_login()}', convert(datetime, '{user.action_time().strftime("%Y-%m-%d %H:%M:%S")}', 120),
        convert(datetime, '{user.action_time().strftime("%Y-%m-%d %H:%M:%S")}', 120), 1)"""

        return query

    @staticmethod
    def authorize_user(user: SenderInfo, user_id: int):
        query = f"""
        update Users
        set LastOnline = convert(datetime, '{user.action_time().strftime("%Y-%m-%d %H:%M:%S")}', 120), IsOnline = 1
        where UserID = {user_id}"""

        return query

    @staticmethod
    def sign_out_user(user: SenderInfo, user_id: int):
        query = f"""
            update Users
            set LastOnline = convert(datetime, '{user.action_time().strftime("%Y-%m-%d %H:%M:%S")}', 120), IsOnline = 0
            where UserID = {user_id}"""

        return query

    @staticmethod
    def get_all_users_logins():
        query = "select Login from Users"

        return query
