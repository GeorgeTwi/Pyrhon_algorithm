"""2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы."""

from random import *


def marge(right, left):
    res = []
    i = j = 0

    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            res.append(right[i])
            i += 1
        else:
            res.append(left[j])
            j += 1
    res += right[i:] + left[j:]
    return res


def marge_sort(list):
    if len(list) < 2:
        return list
    else:
        a = list[:len(list) // 2]
        b = list[len(list) // 2:]
    return marge(marge_sort(a), marge_sort(b))


array = [round(random() * 50, 3) for _ in range(10)]
print(marge_sort(array))
