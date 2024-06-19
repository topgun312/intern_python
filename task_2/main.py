from task_2.gamepole import GamePole


def main() -> None:
    """
    Основная функция для запуска игры "Сапер", ввода команд для создания игрового поля, а также ввода координат клеток для игры
    """
    n = int(input("Для старта игры введите размер поля (N x N): "))
    m = int(input("Введите количество мин (менее общего количества клеток на поле): "))
    game = GamePole(n, m)
    game.set_mines_on_pole(m)
    game.show()
    while True:
        try:
            x = int(input("Введите координату X: "))
            y = int(input("Введите координату Y: "))
            game.open_cell(x, y)
            game.show()
            if game.pole[y][x].mine == True:
                print("БУМ!!! Вы проиграли!")
                break
            elif game.game_win():
                print("УРА!!! Вы победили!")
                break
        except Exception as ex:
            print("Ошибка: " + str(ex))


if __name__ == "__main__":
    main()
