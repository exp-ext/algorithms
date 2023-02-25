"""
G. Стек - MaxEffective

Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
100000. Далее идут команды по одной в строке. Команды могут быть следующих
видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для
команды pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример 1
Ввод	Вывод
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max
error
error
4
None

Вывод
error
error
4
None
"""


class StackMaxEffective:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def push(self, item):
        if self.items:
            new_max = max(item, self.items[-1][1])
        else:
            new_max = item
        self.items.append((item, new_max))

    def pop(self):
        return self.items.pop()[0]

    def get_max(self):
        return self.items[-1][1]


if __name__ == '__main__':

    stack = StackMaxEffective()
    n = int(input())

    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'pop':
            if stack:
                stack.pop()
            else:
                print('error')
        if cmd[0] == 'push':
            stack.push(int(cmd[1]))
        if cmd[0] == 'get_max':
            if stack:
                print(stack.get_max())
            else:
                print('None')
