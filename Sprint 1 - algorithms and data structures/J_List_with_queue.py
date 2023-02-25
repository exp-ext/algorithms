"""
J. Списочная очередь

Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример 1
Ввод
10
put -34
put -23
get
size
get
size
get
get
put 80
size

Вывод
-34
1
-23
0
error
error
1
"""


class CustomQueueOfListsException(Exception):
    def __init__(self, message):
        self.message = message


class QueueOfLists:
    def __init__(self):
        self.array = []

    def put(self, element):
        self.array.append(element)

    def size(self):
        return len(self.array)

    def get(self):
        if self.size() == 0:
            raise CustomQueueOfListsException('error')
        return self.array.pop(0)


n = int(input())
queue_instance = QueueOfLists()

for i in range(n):
    try:
        list_cmd = input().split(' ')
        if len(list_cmd) == 1:
            print(getattr(queue_instance, list_cmd[0])())
        else:
            getattr(queue_instance, list_cmd[0])(list_cmd[1])
    except CustomQueueOfListsException as error:
        print(error.message)
