from task_3.data import Data
from task_3.router import Router
from task_3.server import Server

if __name__ == "__main__":

    router = Router()
    s1 = Server()
    s2 = Server()
    s3 = Server()
    s4 = Server()

    data = Data("Hello!", 3)
    router.link(s3)
    send = s1.send_data(data)
    router.send_data()
    s3.get_data()

    data_1 = Data("Hi", 4)
    router.link(s4)
    send1 = s2.send_data(data_1)
    router.send_data()
    s4.get_data()
