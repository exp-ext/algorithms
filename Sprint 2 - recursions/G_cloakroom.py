"""
G. Гардероб

Рита решила оставить у себя одежду только трёх цветов: розового,
жёлтого и малинового. После того как вещи других расцветок были
убраны, Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце
—– малинового. Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода
В первой строке задано количество предметов в гардеробе: n –— оно
не превосходит 1000000. Во второй строке даётся массив, в котором
указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый
—– 1, малиновый –— 2.

Формат вывода
Нужно вывести в строку через пробел цвета предметов в правильном
порядке.

Пример 1
Ввод
7
0 2 1 2 0 0 1

Вывод
0 0 0 1 1 2 2
"""


def counting_sort(array: list, k: int = 3):
    if len(array) == 0:
        print(*array)
    counted_values = [0] * k
    counted_values[0] = array.count(0)
    counted_values[1] = array.count(1)
    counted_values[2] = array.count(2)
    # for value in array:
    #     counted_values[value] += 1
    index = 0
    for value in range(k):
        for _ in range(counted_values[value]):
            array[index] = value
            index += 1
    print(*array)


if __name__ == '__main__':
    _ = input()
    array = list(map(int, input().split()))
    counting_sort(array)
