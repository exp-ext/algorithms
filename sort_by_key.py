"""
В одном варианте алгоритму сортировки передаётся в качестве параметра функция
одного аргумента key(object). Эта функция будет применена к каждому
сравниваемому объекту, чтобы получить значение ключа для этого элемента.
Все объекты попарно будут сравниваться между собой по этому ключу.
"""
digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def card_strength(card):    # ключ сравнения
    return digit_lengths[card]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and key(item_to_insert) < key(array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


cards = [3, 7, 9, 2, 3]
insertion_sort_by_key(cards, card_strength)


"""
В другом варианте в алгоритм сортировки передаётся функция с двумя аргументами
less(object_1, object_2), которая сравнивает два объекта и возвращает true,
если первый объект должен быть расположен раньше второго, и false в противном
случае. Такую функцию называют «компаратор» (англ. compare, «сравнивать»).
"""

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def is_first_card_weaker(card_1, card_2):    # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


if __name__ == '__main__':
    cards = [3, 7, 9, 2, 3]
    insertion_sort_by_comparator(cards, is_first_card_weaker)


"""
Сравнение элементов при помощи компаратора позволяет более гибко задавать
порядок элементов, чем сравнение по ключу. Например, сортировку по любому
ключу легко переписать в виде сортировки с таким компаратором:
def less(object_1, object_2):
    return key(object_1) < key(object_2)
"""
