class Data:
    """
    Класс с пакетом данных, содержащих информационный пакет и IP-адрес получателя
    """

    def __init__(self, data_str: str, ip_address: int):
        self.data_str = data_str
        self.ip_address = ip_address
