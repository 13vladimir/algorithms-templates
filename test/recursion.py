def build_matryoshka(size, n):
    if n >= 1:
        print(f'Создаём низ матрёшки размера {size}.')
        build_matryoshka(size - 1, n - 1)
        print(f'Создаём верх матрешки размера {size}.')
    else:
        return


build_matryoshka(4, 3)


def stairs_builder(n):
    # построить 1 ступеньку
    if n == 0:
        return
    print(f'Осталось построить {n} ступеней.')
    stairs_builder(n - 1)
    return


stairs_builder(1)


def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)


as_binary_string(2)


def binarySearch(arr, x, left, right):
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)

# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearch(arr, x, left = 0, right = len(arr))


def binarySearchDescending(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x: # искомый элемент больше центрального
        # на этот раз все элементы больше центрального
        # располагаются в левой половине
        return binarySearchDescending(arr, x, left, mid)
    else:
        return binarySearchDescending(arr, x, mid + 1, right)


def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1')
