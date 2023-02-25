"""
G. Работа из дома

Вася реализовал функцию, которая переводит целое число из десятичной системы в
двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное
представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.

Пример 1
Ввод
5
Вывод
101
"""
from ..timing import timing


@timing
def to_binary(number: int) -> str:
    digs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    сс = 2
    encoded_n = ''
    while True:
        encoded_n = digs[number % сс] + encoded_n
        number = number // сс
        if number == 0:
            return encoded_n


@timing
def read_input() -> int:
    return int(input().strip())


if __name__ == "__main__":
    print(to_binary(read_input()))
