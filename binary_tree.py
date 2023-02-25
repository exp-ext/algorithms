"""
Этот код реализует структуру данных двоичного дерева поиска (BST).
BST - это тип дерева, в котором каждый узел имеет не более двух
дочерних элементов, и данные в левом поддереве меньше, чем данные
в узле, а данные в правом поддереве больше, чем данные в узле.
"""


class Node:
    """
    Класс Node - это простая реализация узла в дереве,
    который имеет поле данных и указатели слева и справа
    на его дочерние элементы.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Tree:
    """
    Класс Tree реализует структуру данных BST.
    Он имеет переменную экземпляра root для
    отслеживания корневого узла дерева.
    """
    def __init__(self) -> None:
        self.root = None

    def __find(self, node, parent, value):
        """
        Метод __find выполняет поиск узла в дереве с заданным значением.
        Он возвращает узел, его родителя и флаг, указывающий, был ли
        узел найден.
        """
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        """
        Метод append вставляет в дерево новый узел с заданным значением,
        используя метод __find для поиска подходящего места для нового узла.
        """
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node):
        """
        Метод show_tree выполняет обход дерева по порядку, печатая данные
        в узлах в отсортированном порядке.
        """
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        """
        Метод show_wide_tree выполняет обход дерева по ширине, выводя данные
        на каждом уровне дерева в отдельной строке.
        """
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):
        """
        Методы __del_leaf и __del_one_child используются для удаления узлов
        с 0 или 1 дочерним узлом соответственно.
        """
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        """
        Метод __find_min используется для поиска узла с наименьшим
        значением в поддереве. Он используется в случае, когда
        удаляемый узел имеет двух детей, чтобы найти для него замену.
        """
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        """
        Метод del_node используется для удаления узла с заданным ключом
        из дерева.
        """
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


v = [10, 5, 7, 16, 13, 2, 20]
t = Tree()
for x in v:
    t.append(Node(x))

t.del_node(5)
t.show_tree(t.root)
print()

v = [20, 5, 24, 2, 16, 11, 18]
t = Tree()
for x in v:
    t.append(Node(x))

# t.del_node(5)
t.show_wide_tree(t.root)
