from task_3.server import Server


class Router:
    """
    Класс для описания работы роутера в сети
    """

    ip_receiver = {}
    buffer = []

    def link(self, server: Server) -> None:
        """
        Метод класса для присоединения сервера к роутере
        """
        server_ip = server.get_ip()
        self.ip_receiver[server_ip] = server

    def unlink(self, server: Server) -> None:
        """
        Метод класса для отсоединения сервера от роутера
        """
        unlink_ip = server.get_ip()
        if unlink_ip in self.ip_receiver:
            self.ip_receiver.pop(unlink_ip)

    def send_data(self) -> None:
        """
        Метод класса для отправки всех пакетов из буфера роутера соответсвующим серверам
        """
        for i in self.buffer:
            ip_to = i["ip_to"]
            if ip_to in self.ip_receiver:
                self.ip_receiver[ip_to].buffer.append(
                    {"data": i["data"], "ip_from": i["ip_from"]}
                )
                self.buffer.clear()
