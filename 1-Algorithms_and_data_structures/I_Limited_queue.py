"""
I. Ограниченная очередь

Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает параметр
max_size, означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу
такой очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд,
оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди,
он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;

При превышении допустимого размера очереди нужно вывести «error».
При вызове операций pop() или peek() для пустой очереди нужно вывести «None».

Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Пример 1
Ввод
8
2
peek
push 5
push 2
peek
size
size
push 1
size

Вывод
None
5
2
2
error
2
"""


class CustomQueueSizedException(Exception):
    def __init__(self, message):
        self.message = message


class MyQueueSized:
    def __init__(self, max_size):
        self.array = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = -1
        self.qsize = 0

    def push(self, element):
        if self.qsize != self.max_size:
            self.tail = (self.tail + 1) % self.max_size
            self.array[self.tail] = element
            self.qsize += 1
        else:
            raise CustomQueueSizedException('error')

    def size(self):
        return self.qsize

    def peek(self):
        if self.qsize == 0:
            raise CustomQueueSizedException('None')
        return self.array[self.head]

    def pop(self):
        x = self.peek()
        self.head = (self.head + 1) % self.max_size
        self.qsize -= 1
        return x


qty_cmd = int(input())
max_size = int(input())
queue_sized = MyQueueSized(max_size)

for _ in range(qty_cmd):
    try:
        list_cmd = input().split(' ')
        if len(list_cmd) == 1:
            print(getattr(queue_sized, list_cmd[0])())
        else:
            getattr(queue_sized, list_cmd[0])(int(list_cmd[1]))
    except CustomQueueSizedException as error:
        print(error.message)
