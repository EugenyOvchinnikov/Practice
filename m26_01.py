# Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N
# (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
from collections.abc import Iterable


class Square:
    """ Класс итератор """
    __current_number = 0

    def __init__(self, number: int):
        self.__number = number

    def __iter__(self):
        return self

    def __next__(self) -> int:
        Square.__current_number += 1
        if Square.__current_number > self.__number:
            raise StopIteration
        else:
            return Square.__current_number ** 2


# функция-генератор
def squares(number: int) -> Iterable[int]:
    for n in range(1, number + 1):
        yield n ** 2


if __name__ == '__main__':
    my_number = int(input('Введите число N: '))

    # Используем класс-итератор
    my_iter = Square(my_number)

    for i_elem in my_iter:
        print(i_elem, end=' ')

    # Используем функцию-генератор
    print()
    for square in squares(my_number):
        print(square, end=' ')

    # Генераторное выражение
    my_iter2 = (i ** 2 for i in range(1, my_number + 1))

    print()
    for i_elem in my_iter2:
        print(i_elem, end=' ')

