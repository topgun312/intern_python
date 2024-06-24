import itertools
import random
from typing import Any, Generator, Callable

from task_2.cell import Cell


def cell_out_of_range(func: Callable[[int, int], Any]) -> Callable[[int, int], Any]:
    """
    Функция - декоратор для проверки существования клетки с введенными координатами
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            raise Exception("Клетки с данной координатой не существует!")

    return wrapper


class GamePole:
    """
    Класс для управления игровым полем, размером N x N клеток
    """

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.create_pole()

    def create_pole(self) -> list[list[Cell]]:
        """
        Метод для создания пустого игрового поля
        """
        return [[Cell() for _ in range(self.N)] for _ in range(self.N)]

    def set_mines_on_pole(self, mines: int) -> None:
        """
        Метод для расстановки мин на игровом поле и обновление значений соседних клеток
        """
        cells_count = self.N**2
        if mines > cells_count:
            raise ValueError("Количество мин превышает количесвто клеток!")

        cells_pos = itertools.product(range(self.N), range(self.N), repeat=1)
        mines_pos = random.sample(tuple(cells_pos), k=mines)

        for mine_x, mine_y in mines_pos:
            cell = self.get_cell_coord(mine_x, mine_y)
            cell.set_mine()

            for neighbor_cell in self.get_all_neighbors(mine_x, mine_y):
                neighbor_cell.count_around_mines()

    def get_cell_coord(self, cell_x: int, cell_y: int) -> Cell:
        """
        Метод для получения клетки по его координатам
        """
        return self.pole[cell_y][cell_x]

    def get_all_neighbors_positions(
        self, cell_x: int, cell_y: int
    ) -> Generator[tuple[int, int], Any, None]:
        """
        Метод для получения позиций соседних клеток
        """
        for x_shift, y_shift in itertools.product((-1, 0, 1), repeat=2):
            if x_shift == y_shift == 0:
                continue
            x = cell_x + x_shift
            y = cell_y + y_shift
            if x not in range(self.N) or y not in range(self.N):
                continue
            yield (x, y)

    def get_all_neighbors(self, cell_x: int, cell_y: int) -> Generator[Cell, Any, None]:
        """
        Метод для получения действительных позиций всех соседних клеток
        """
        neighbors_pos = self.get_all_neighbors_positions(cell_x, cell_y)
        for neighbor_x, neighbor_y in neighbors_pos:
            yield self.get_cell_coord(neighbor_x, neighbor_y)

    @cell_out_of_range
    def open_cell(self, cell_x: int, cell_y: int) -> None:
        """
        Метод для открытия клеток
        """
        cell = self.get_cell_coord(cell_x, cell_y)
        if cell.mine:
            self.open_all_mine_cell()
        elif cell.is_empty:
            cell.set_open()
            self.open_empty_cell_neighbors(cell_x, cell_y)
        elif cell.has_around_mines and cell.fl_open:
            cell.set_open()
            self.open_around_mines_cell_neighbors(cell_x, cell_y)
        else:
            cell.set_open()

    def open_all_mine_cell(self) -> None:
        """
        Метод для открытия всех клеток с минами в случае проигрыша
        """
        for cell_row in self.pole:
            for cell in cell_row:
                if cell.mine == True:
                    cell.set_open()

    def open_empty_cell_neighbors(self, cell_x: int, cell_y: int) -> None:
        """
        Метод для открытия всех соседних клеток и их не пустых соседних клеток
        """
        neighbors_pos = self.get_all_neighbors_positions(cell_x, cell_y)
        for x, y in neighbors_pos:
            cell = self.get_cell_coord(x, y)
            if cell.fl_open:
                continue
            cell.set_open()
            if cell.is_empty:
                self.open_empty_cell_neighbors(x, y)

    def open_around_mines_cell_neighbors(self, cell_x: int, cell_y: int) -> None:
        """
        Метод для открытия всех соседних клеток рядом с численной клеткой
        """
        neighbors_pos = self.get_all_neighbors(cell_x, cell_y)
        for neighbors_x, neighbors_y in neighbors_pos:
            neighbor_cell = self.get_cell_coord(neighbors_x, neighbors_y)
            if not neighbor_cell.fl_open:
                self.open_cell(neighbors_x, neighbors_y)

    def game_win(self) -> bool:
        """
        Метод для определения условий для выигрыша в игре
        """
        count = 0
        for row in self.pole:
            for cell in row:
                if self.show_cell(cell) == "#":
                    count += 1
        if count == self.M:
            return True

    def show_cell(self, cell: Cell) -> str:
        """
        Метод для отображения в консоли конкретной клетки
        """
        if cell.fl_open:
            if cell.mine:
                return "*"
            if cell.is_empty:
                return " "
            elif cell.around_mines:
                return f"{cell.around_mines}"
        else:
            return "#"

    def show(self) -> None:
        """
        Метод для отображения всего игрового поля в консоли
        """
        for row in self.pole:
            print(" ".join(str(self.show_cell(cell)) for cell in row))
