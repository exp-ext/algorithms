"""
A. Ближайший ноль

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый
участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого
участка. Если участок пустой, эта величина будет равна нулю — расстояние до
самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта
улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены
нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 10**6). В следующей строке
записаны n целых неотрицательных чисел — номера домов и обозначения пустых
участков на карте (нули). Гарантируется, что в последовательности есть хотя бы
один ноль. Номера домов (положительные числа) уникальны и не превосходят 10**9.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите
в одну строку, разделяя их пробелами.

Пример
Ввод
5
0 1 4 9 0

Вывод
0 1 2 1 0
"""

# {
# 'ID':'79788610',
# 'Вердикт': 'OK',
# 'Время':'1.696s',
# 'Память':'113.46Mb',
# }

from typing import List


def cycle(values_line: List[int],
          number_street: List[int],
          reverse: bool = False) -> List[int]:
    """
    Общий цикл (алгоритм) обработки длины улицы.
    - values_line (:obj:`List[int]`) - список с 0 и порядковым
    положением домов к нулю.
    - length (:obj:`int`) - количество записей в списке number_street.
    - number_street (:obj:`List[int]`) - исходные данные о домах.
    - reverse (:obj:`bool`) - направление перебора значений.
    """
    length = len(number_street)
    if reverse:
        work_range = reversed(range(length))
        last_zero = 2 * length
    else:
        work_range = range(length)
        last_zero = -length

    for i in work_range:
        if number_street[i]:
            if reverse:
                values_line[i] = min(last_zero - i, values_line[i])
            else:
                values_line[i] = i - last_zero
        else:
            last_zero = i

    return values_line


def nearest_zero(number_street: List[int]) -> List[int]:
    """
    Главный модуль подставляющий данные в алгоритм обработки.
    - length (:obj:`int`) - длинна улицы n (1 ≤ n ≤ 106).
    - number_street (:obj:`List[int]`) - номера домов и обозначения пустых
    участков на карте (нули).
    """
    values_line = [0] * len(number_street)
    values_line = cycle(values_line, number_street)
    reverse = True
    return cycle(values_line, number_street, reverse)


def read_input() -> List[int]:
    """Чтение входных данных."""
    _ = input()
    return list(map(int, input().strip().split()))


if __name__ == '__main__':
    print(*nearest_zero(read_input()))
