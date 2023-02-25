
def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    mid = int(len(array) / 2)

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: mid])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[mid: len(array)])

    # заводим массив для результата сортировки
    result = []

    # сливаем результаты
    lef, ri = 0, 0
    while lef < len(left) and ri < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[lef] <= right[ri]:
            result.append(left[lef])
            lef += 1
        else:
            result.append(right[ri])
            ri += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while lef < len(left):
        result.append(left[lef])  # перенеси оставшиеся элементы left в result
        lef += 1

    while ri < len(right):
        result.append(right[ri])  # перенеси оставшиеся элементы right в result
        ri += 1

    return result


print(merge_sort([1, 10, 20, 8, 5, 8, 4, 3, 2]))
