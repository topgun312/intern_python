from typing_extensions import Self


class ObjList:
    """
    Класс - узел двусвязного списка
    """

    def __init__(self, data: Self, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev
        self.instance = self

    def get_next(self) -> Self:
        return self.__next

    def get_prev(self) -> Self:
        return self.__prev

    def set_next(self, obj: Self) -> None:
        self.__next = obj

    def set_prev(self, obj: Self) -> None:
        self.__prev = obj

    def get_data(self) -> Self:
        return self.__data

    def set_data(self, obj: Self) -> None:
        self.__data = obj
