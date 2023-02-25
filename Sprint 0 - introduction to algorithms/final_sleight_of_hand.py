"""
B. Ловкость рук

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек. На клавише
написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши, на которых
написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k
клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки
получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут
нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой
строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов, которое смогут
набрать Гоша и Тимофей.

Пример 1
Ввод
3
1231
2..2
2..2
2..2
Вывод
2
"""

# {
# 'ID':'79792849',
# 'Вердикт': 'OK',
# 'Время':'90ms',
# 'Память':'4.25Mb',
# }
# Спасибо за подсказку 👍

from collections import Counter
from typing import Tuple


def get_scores(number: int, matrix: str) -> int:
    """
    Максимальное количество баллов, которое могут набрать Гоша и Тимофей.

    - number (:obj:`int`) - клавиши на которые могут нажать
    Гоша и Тимофей каждый (1 ≤ k ≤ 5)
    - matrix (:obj:`str`) - 4 строки по 4 символа в каждой строке
    совмещены в одну.
    Каждый символ - либо точка, либо цифра от 1 до 9.
    """
    return sum(
        all((key.isdigit(), value <= number))
        for key, value in Counter(matrix).items()
    )


def read_input() -> Tuple[int, str]:
    """Чтение входных данных."""
    number = int(input()) * 2
    matrix = f"{input()}{input()}{input()}{input()}"
    return number, matrix


if __name__ == '__main__':
    number, matrix = read_input()
    print(get_scores(number, matrix))
