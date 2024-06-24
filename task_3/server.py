import itertools

from task_3.data import Data


class Server:
    """
    Класс для описания работы серверов в сети
    """

    ip_iter = itertools.count(1)

    def __init__(self):
        self.ip_address = next(Server.ip_iter)
        self.buffer = []

    def get_ip(self) -> int:
        """
        Метод класса для возвращения своего IP-адреса
        """
        return self.ip_address

    def send_data(self, data: Data) -> None:
        """
        Метод класса для отправки информационного пакета data с указанным IP-адресом получателя
        """
        from task_3.router import Router

        data_router = {
            "data": data.data_str,
            "ip_to": data.ip_address,
            "ip_from": self.get_ip()
        }
        Router.buffer.append(data_router)
        self.buffer.append({"data": data_router["data"], "ip_to": data_router["ip_to"]})

    def get_data(self) -> None:
        """
        Метод класса для получения списка принятых пакетов и очистки входного буфера
        """
        for item in self.buffer:
            print(
                "Полученные данные: ", *map(lambda i: f"{i[0]}: {i[1]} ", item.items())
            )
        self.buffer.clear()
