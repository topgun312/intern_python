from task_1.objlist import ObjList


class LinkedList:
    """
    Класс двусвязного списка
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        """
        Метод для добавления нового объекта obj класса ObjList в конец связного списка
        """
        new_object = ObjList(obj)
        if self.head == None:
            self.head = self.tail = new_object
            self.head.set_prev(None)
            self.tail.set_next(None)
        else:
            self.tail.set_next(new_object)
            new_object.set_prev(self.tail)
            self.tail = new_object
            self.tail.set_next(None)
            self.tail = new_object

    def remove_obj(self) -> None:
        """
        Метод для удаления последнего объекта из связного списка
        """
        try:
            if self.tail == None:
                raise Exception("Нет данных для удаления!")
            else:
                self.tail = self.tail.get_prev()
                if self.tail != None:
                    self.tail.set_next(None)
        except Exception as ex:
            print("Ошибка: " + str(ex))

    def get_data(self) -> None:
        """
        Метод для получения списка из строк локального свойства data всех объектов связного списка
        """
        cur_list = []
        current = self.head
        if self.head == None:
            print("Список пустой!")
            return
        while current != None:
            cur_list.append(current.get_data().get_data())
            current = current.get_next()
        print(cur_list)
