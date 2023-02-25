"""
H. Двоичная система

Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести
их сумму, также в двоичной системе. Встроенную в язык программирования
возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить
задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального
числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

Пример 1
Ввод
1010
1011
Вывод
10101
"""

from typing import Tuple

from ..timing import timing


@timing
def get_sum(first_number: str, second_number: str) -> str:
    max_len = max(len(first_number), len(second_number))
    first_number = first_number.zfill(max_len)
    second_number = second_number.zfill(max_len)

    carry = 0
    result = ''

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if first_number[i] == '1' else 0
        r += 1 if second_number[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)


@timing
def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


if __name__ == "__main__":
    first_number, second_number = read_input()
    print(get_sum(first_number, second_number))
