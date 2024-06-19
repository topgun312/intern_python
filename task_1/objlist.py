class ObjList:
    """
    Класс - узел двусвязного списка
    """

    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_data(self):
        return self.__data

    def set_data(self, obj):
        self.__data = obj
