"""
B. Чётные и нечётные числа
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа. Если все три числа оказываются
одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c. Числа не
превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
Ввод
1 2 -3
Вывод
FAIL
"""
from ..timing import timing


@timing
def check_parity(a: int, b: int, c: int) -> bool:
    arr = [a, b, c]
    for i in range(0, 3):
        if not arr[i] & 1:
            arr[i] = True
        else:
            arr[i] = False
    result = sum(arr)
    if result == 0 or result == 3:
        return True
    return False


@timing
def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


if __name__ == "__main__":
    a, b, c = map(int, input().strip().split())
    print_result(check_parity(a, b, c))
