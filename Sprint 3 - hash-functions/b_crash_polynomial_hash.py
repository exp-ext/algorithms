"""
B. Сломай меня
Гоша написал программу, которая сравнивает строки исключительно по их хешам.
Если хеш равен, то и строки равны. Тимофей увидел это безобразие и поручил
вам сломать программу Гоши, чтобы остальным неповадно было.

В этой задаче вам надо будет лишь найти две различные строки, которые для
заданной хеш-функции будут давать одинаковое значение.

Гоша использует следующую хеш-функцию:


для a = 1000 и m = 123 987 123.
В данной задаче необходимо использовать в качестве значений отдельных
символов их коды в таблице ASCII.

Формат ввода
В задаче единственный тест без ввода

Формат вывода
Отправьте две строки, по одной в строке. Строки могут состоять только
из маленьких латинских букв и не должны превышать в длину 1000 знаков
каждая. Код отправлять не требуется. Строки из примера использовать нельзя.

Пример вывода:

ezhgeljkablzwnvuwqvp

gbpdcvkumyfxillgnqrv
"""

import random
import string

base = 1000
tablesize = 123987123


def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m

    return int(hash_val)


if __name__ == '__main__':

    letters = string.ascii_lowercase
    word = ''.join(random.choice(letters) for i in range(10))
    hash_val = polynomial_hash(word[::-1], base, tablesize)
    result = {}

    while True:
        word = ''.join(random.choice(letters) for i in range(20))
        hash_val = polynomial_hash(word[::-1], base, tablesize)
        if not result.get(hash_val):
            result[hash_val] = word
        else:
            print(f'{word} - {hash_val}')
            print(result.get(hash_val), f'- {hash_val}')
            break
