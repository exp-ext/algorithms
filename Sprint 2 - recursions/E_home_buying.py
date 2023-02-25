"""
E. Покупка домов

Тимофей решил купить несколько домов на знаменитом среди разработчиков
Алгосском архипелаге. Он нашёл n объявлений о продаже, где указана стоимость
каждого дома в алгосских франках. А у Тимофея есть k франков. Помогите ему
определить, какое наибольшее количество домов на Алгосах он сможет приобрести
за эти деньги.

Формат ввода
В первой строке через пробел записаны натуральные числа n и k.

n — количество домов, которые рассматривает Тимофей, оно не превосходит 100000;

k — общий бюджет, не превосходит 100000;

В следующей строке через пробел записано n стоимостей домов. Каждое из чисел
не превосходит 100000. Все стоимости — натуральные числа.

Формат вывода
Выведите одно число —– наибольшее количество домов, которое может купить
Тимофей.

Пример 1
Ввод
3 300
999 999 999
Вывод
0
"""


def home_buying(budget, houses_cost):
    """
    Эта функция возвращает количество домов, которые
    можно купить при заданном бюджете, и стоимость каждого дома.
    """
    count = 0
    for house in houses_cost:
        budget -= house
        if budget >= 0:
            count += 1
        else:
            return count
    return count


if __name__ == '__main__':
    num, budget = map(int, input().split())
    houses_cost = sorted(list(map(int, input().split())))
    print(home_buying(budget, houses_cost))
