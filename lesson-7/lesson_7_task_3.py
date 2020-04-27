"""3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима)."""
from random import *


#вторая часть ф-ии сортировки
def heap(list, n, i):
    x = i
    z_1 = i + 1
    z_2 = i + 2

    if z_1 < n and list[i] < list[z_1]:
        x = z_1

    if z_2 < n and list[x] < list[z_2]:
        x = z_2

    if x != i:
        list[i], list[x] = list[x], list[i]

        heap(list, n, x)


# первая часть функции сортировки
def sort(list):
    n = len(list)

    for i in range(n, -1, -1):
        heap(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heap(list, i, 0)



m = 2
array = [randint(0, 100) for _ in range((2 * m) + 1)]
print(array)
sort(array)
print(array)
print(f'Медиана: {array[len(array) // 2]}')







