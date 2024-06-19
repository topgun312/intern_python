from task_1.linkedlist import LinkedList
from task_1.objlist import ObjList


if __name__ == "__main__":
    lst = LinkedList()
    lst.add_obj(ObjList("данные 1"))
    lst.add_obj(ObjList("данные 2"))
    lst.add_obj(ObjList("данные 3"))
    result = lst.get_data()
