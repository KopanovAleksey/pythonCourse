import random

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def array_of_progression(first_element: int, differenсe: int, elements_ammount: int) -> list():
    result = list()
    for i in range(elements_ammount):
        result.append(first_element + i*differenсe)
    return result


element1 = int(input("Введите первый член арефметической прогрессии: "))
diff = int(input("Введите разность арефметической прогрессии: "))
ammount = int(
    input("Введите количество элементов арефметической прогрессии: "))

print(*array_of_progression(element1, diff, ammount))


# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_element_index_in_range(array: list(), maximum: int, minimum: int) -> list:
    result = list()
    for i in range(len(array)):
        if minimum <= array[i] <= maximum:
            result.append(i)
    return result


sp = [random.randint(-100, 100) for i in range(int(input("Введите количество элементов массива: ")))]
mx = int(input("Введите верхнюю границу значений элементов: "))
mn = int(input("Введите нижнюю границу значений элементов: "))
print(sp)
print(find_element_index_in_range(sp, mx, mn))