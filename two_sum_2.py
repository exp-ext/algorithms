"""
Обратите внимание на ограничения в этой задаче.

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано
количество очков. Фишки лежат на столе в порядке не убывания очков на них.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки,
сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки
программирования для решения этой задачи. Помогите ей написать программу
для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 105.

Во второй строке записано n целых чисел в порядке не убывания —–
очки на фишках Риты в диапазоне от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».
"""

from typing import List, Optional, Tuple


def two_sum_ds(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in arr:
        Y = target_sum - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле,
    # значит, нужной пары элементов в массиве нет.
    return None, None


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None, None


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
