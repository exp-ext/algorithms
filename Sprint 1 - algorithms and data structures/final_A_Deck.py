"""
A. Дек

Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x),
pop_back(), pop_front() работали корректно. Но, если в деке было
много элементов, программа работала очень долго. Дело в том, что
не все операции выполнялись за O(1). Помогите Гоше! Напишите
эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 100000. Во второй строке записано число m —
максимальный размер дека. Он не превосходит 50000. В следующих
n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке
уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке
уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если
дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если
дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод
4
push_front 861
push_front -819
pop_back
pop_back

Вывод
861
-819
"""
# {
# 'ID':'80151982',
# 'Вердикт': 'OK',
# 'Время':'0.561s',
# 'Память':'7.31Mb',
# }


from typing import List

ERROR = 'error'


class Deck:
    def __init__(self, max_size: int) -> None:
        self.array = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.head = 0
        self.tail = -1

    def push_back(self, value: str) -> None or OverflowError:
        if self.is_overflow:
            raise OverflowError
        self.tail = (self.tail + 1) % self.max_size
        self.array[self.tail] = value
        self.size += 1

    def push_front(self, value: str) -> None or OverflowError:
        if self.is_overflow:
            raise OverflowError
        self.head = (self.head - 1) % self.max_size
        self.array[self.head] = value
        self.size += 1

    def pop_back(self) -> str or IndexError:
        if self.is_empty:
            raise IndexError
        value = self.array[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value

    def pop_front(self) -> str or IndexError:
        if self.is_empty:
            raise IndexError
        value = self.array[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    @property
    def is_overflow(self) -> bool:
        return self.size == self.max_size

    @property
    def is_empty(self) -> bool:
        return self.size == 0


def implementation(n: int, m: int) -> List:
    """
    Построчно считываем команды n раз. Разбиваем,
    получаем список команда/аргумент.
    Используем функцию getattr для получения метода у экземпляра класса Deck.
    Затем мы вызываем этот метод с передачей аргумента, если он есть.
    Результат добавляем в список, который по окончании цикла возвращаем.
    """
    deck_instance = Deck(m)
    return_list = []
    for _ in range(n):
        try:
            list_cmd = input().split(' ')
            result = getattr(deck_instance, list_cmd[0])(*list_cmd[1:])
        except OverflowError:
            return_list.append(ERROR)
        except IndexError:
            return_list.append(ERROR)
        else:
            return_list.append(result) if result else None
    return return_list


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(*implementation(n, m), sep='\n')
