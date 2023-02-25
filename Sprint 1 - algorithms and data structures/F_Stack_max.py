"""
F. Стек - Max

Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции
push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не
превосходит 10000. В следующих n строках идут команды. Команды могут
быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример 1
Ввод
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max

Вывод
None
-2
-2
"""


class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.is_empty() or item >= self.max[-1]:
            self.max.append(item)
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        removed = self.items.pop()
        if removed == self.max[-1]:
            self.max.pop()
        if self.is_empty():
            self.max.clear()
        return removed

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.max[-1]


if __name__ == '__main__':
    stack = StackMax()
    n = int(input())
    result = []
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push':
            stack.push(int(cmd[1]))
        if cmd[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if cmd[0] == 'get_max':
            result.append(stack.get_max())

    for index in result:
        print(index)
