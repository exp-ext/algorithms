"""
L. Лишняя буква

Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв. Строка t
получена перемешиванием букв строки s и добавлением 1 буквы в
случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины
строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод
abcd
abcde
Вывод
e
"""

from typing import Tuple

from ..timing import timing


@timing
def get_excessive_letter(shorter: str, longer: str) -> str:
    temp = list(longer)
    for c in shorter:
        if c in longer:
            temp.remove(c)
    return temp[0]


@timing
def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


if __name__ == "__main__":
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))
