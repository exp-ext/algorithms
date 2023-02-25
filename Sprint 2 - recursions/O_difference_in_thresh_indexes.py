"""
O. Разность треш-индексов

Гоша долго путешествовал и измерил площадь каждого из n островов Алгосов,
но ему этого мало! Теперь он захотел оценить, насколько разнообразными
являются острова в составе архипелага.

Для этого Гоша рассмотрел все пары островов (таких пар, напомним,
n * (n-1) / 2) и посчитал попарно разницу площадей между всеми островами.
Теперь он собирается упорядочить полученные разницы, чтобы взять k-ую по
порядку из них.

Помоги Гоше найти k-ю минимальную разницу между площадями эффективно.

Пояснения к примерам

Пример 1

Выпишем все пары площадей и найдём соответствующие разницы

|2 - 3| = 1
|3 - 4| = 1
|2 - 4| = 2
Так как нам нужна 2-я по величине разница, то ответ будет 1.

Пример 2

У нас есть два одинаковых элемента в массиве —– две единицы, поэтому
минимальная (первая) разница равна нулю.

Формат ввода
В первой строке записано натуральное число n –— количество островов в
архипелаге (2 ≤ n ≤ 100 000).

В следующей строке через пробел записаны n площадей островов — n
натуральных чисел, каждое из которых не превосходит 1 000 000.

В последней строке задано число k. Оно находится в диапазоне от 1 до
n(n - 1) / 2.

Формат вывода
Выведите одно число –— k-ую минимальную разницу.

Пример 1
Ввод
3
2 3 4
2

Вывод
1
"""

# from itertools import combinations


# def kth_min_diff(areas, k):
#     pairs = list(combinations(areas, 2))
#     diffs = [abs(a - b) for a, b in pairs]
#     diffs.sort()
#     return diffs[k-1]

# import heapq


# def kth_min_diff(areas, k):
#     differences = []
#     for i in range(len(areas)):
#         for j in range(i + 1, len(areas)):
#             differences.append(abs(areas[i] - areas[j]))

#     return heapq.nsmallest(k, differences)[-1]


# def kth_min_diff(areas, k):
#     differences = []
#     for i in range(len(areas)):
#         for j in range(i+1, len(areas)):
#             differences.append(abs(areas[i] - areas[j]))

#     for i in range(len(differences)):
#         min_idx = i
#         for j in range(i+1, len(differences)):
#             if differences[j] < differences[min_idx]:
#                 min_idx = j
#         differences[i], differences[min_idx] = differences[min_idx], differences[i]

#     return differences[k-1]


def kth_min_diff(areas, k):
    pass


if __name__ == '__main__':
    _ = input()
    areas = list(map(int, input().split()))
    k = int(input())
    print(kth_min_diff(areas, k))
