class ObjList:
    """
    Класс - узел двусвязного списка
    """

    def __init__(self, data: object, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def get_next(self) -> object:
        return self.__next

    def get_prev(self) -> object:
        return self.__prev

    def set_next(self, obj: object) -> None:
        self.__next = obj

    def set_prev(self, obj: object) -> None:
        self.__prev = obj

    def get_data(self) -> object:
        return self.__data

    def set_data(self, obj: object) -> None:
        self.__data = obj
