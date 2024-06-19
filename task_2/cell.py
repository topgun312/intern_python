from typing import Optional


class Cell:
    """
    Класс для представления клетки игрового поля
    """

    def __init__(self, around_mines: Optional[int] = None, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    @property
    def is_empty(self) -> bool:
        """
        Метод для проверки клетки на пустоту
        """
        return not self.mine and self.around_mines is None

    @property
    def has_around_mines(self) -> bool:
        """
        Метод для проверки наличия числа в клетке
        """
        return self.around_mines is not None

    def set_mine(self) -> None:
        """
        Метод для установки клетки миной
        """
        self.mine = True

    def set_open(self) -> None:
        """
        Метод для установки клетки как открытой
        """
        self.fl_open = True

    def count_around_mines(self) -> None:
        """
        Метод для увеличения численного значения клетки
        """
        if self.around_mines is None:
            self.around_mines = 0
        self.around_mines += 1
