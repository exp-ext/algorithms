"""
K. Сортировка слиянием
Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше
обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
Функция merge принимает два отсортированных массива, сливает их в один
отсортированный массив и возвращает его. Если требуемая сигнатура имеет
вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом
[left,mid) массива array, а второй – полуинтервалом [mid,right) массива array.
Функция merge_sort принимает некоторый подмассив, который нужно отсортировать.
Подмассив задаётся полуинтервалом — его началом и концом. Функция должна
отсортировать передаваемый в неё подмассив, она ничего не возвращает.
Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно
вызывает сортировку отдельно для каждой. Затем два отсортированных массива
сливаются в один с помощью merge.
Заметьте, что в функции передаются именно полуинтервалы [begin,end), то есть
правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4),
где arr=[4,5,3,0,1,2], то будут отсортированы только первые четыре элемента,
изменённый массив будет выглядеть как arr=[0,3,4,5,1,2].
Реализуйте эти две функции.
Мы рекомендуем воспользоваться заготовками кода для данной задачи,
расположенными по ссылке.

Формат ввода
Передаваемый в функции массив состоит из целых чисел, не превосходящих
по модулю 109. Длина сортируемого диапазона не превосходит 105.

Формат вывода
При написании и отправке решений соблюдайте следующие правила:
Отправляйте решение в виде файла. Если текст решения будет вставлен в форму,
то будет возвращена ошибка.

Python

merge(arr: list, left: int, mid: int, right: int) -> array
merge_sort(arr: list, left: int, right: int) -> None

"""


def merge(arr: list, left: int, mid: int, right: int) -> list:
    result = []
    left = arr[left:mid]
    right = arr[mid:right]
    i_left = i_right = 0
    while len(result) < len(left) + len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        if i_right == len(right):
            result += left[i_left:]
            break
        if i_left == len(left):
            result += right[i_right:]
            break
    return result


def merge_sort(arr: list, left: int, right: int) -> list:
    if right - left >= 2:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        arr[left:right] = merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
