

def build_matryoshka(size, n):
    if n >= 1:
        print(f"Создаём низ матрёшки размера {size}.")
        build_matryoshka(size - 1, n - 1)
        print(f"Создаём верх матрешки размера {size}.")
    else:
        return


def binarySearch(arr, x, left, right):
    if right <= left:   # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:   # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else:   # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


def binarySearchDescending(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:  # искомый элемент больше центрального
        # на этот раз все элементы больше центрального
        # располагаются в левой половине
        return binarySearchDescending(arr, x, left, mid)
    else:
        return binarySearchDescending(arr, x, mid + 1, right)


if __name__ == "__main__":
    build_matryoshka(4, 3)
    # изначально мы запускаем двоичный поиск на всей длине массива
    arr = [x for x in range(10)]
    x = 5
    print(binarySearch(arr, x, left=0, right=len(arr)))
    arr = sorted(arr, reverse=True)
    print(binarySearchDescending(arr, x, left=0, right=len(arr)))
