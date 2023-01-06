import socketserver
import json
import ServerConfig
from DTOs.SenderInfo import SenderInfo
from Actions.RequestHandler import RequestHandler
from Server.Database.DbManager import DbManager
from datetime import datetime


class RequestAcceptor (socketserver.BaseRequestHandler):
    __data: str = "test"
    __db_manager: DbManager = DbManager()
    #__request_handler: RequestHandler = RequestHandler(__db_manager)

    # обработка запроса
    def handle(self):
        request_handler = RequestHandler(self.__db_manager)
        # получение данных
        print("\n\n")
        print(f"Время: {datetime.now()}")
        print(f"Входящее подключение от {self.client_address[0]}")
        print("Получение запроса")
        self.__data = self.request.recv(1024)
        parsed_data = json.loads(self.__data)
        print(f"Данные: {parsed_data}")
        # обработка данных
        current_user = SenderInfo().fill_data(parsed_data)
        print("Обработка запроса, формирование ответа")
        response = request_handler.execute_give_response(current_user)
        dict_to_send = response.get_dict()
        print(f"Ответ: {dict_to_send}")
        # ответ на данные
        to_send = json.dumps(dict_to_send, ensure_ascii=False).encode()
        print("Отправка ответа")
        self.request.sendall(to_send)
        print("Подключение окончено")


def start_server():
    # запуск сервера
    host, port = ServerConfig.host, ServerConfig.port
    with socketserver.TCPServer((host, port), RequestAcceptor) as my_server:
        my_server.serve_forever()
