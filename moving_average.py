from typing import List, Tuple

"""
Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение
которых велись измерения. 1 ≤ n ≤ 105

Во второй строке через пробел записаны n целых неотрицательных чисел qi,
каждое лежит в диапазоне от 0 до 103.

В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.

Примечание для Go:

Заметьте, что в данной задаче достаточно большой размер ввода.
Поэтому необходимо задавать размер буфера для сканера хотя бы 600 Кб.
"""


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)

    for i in range(0, len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


if __name__ == "__main__":
    arr, window_size = read_input()
    print(" ".join(map(str, moving_average(arr, window_size))))
