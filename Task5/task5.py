# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def numberToPower(number: int, power: int) -> int:
    if power == 0:
        return 1
    else:
        return number * numberToPower(number, power - 1)
    

print(numberToPower(5, 3))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a: int, b: int) -> int:
    if a == 0:
        if b == 0:
            return 0
        return sum(a, b - 1) + 1
    return sum(a-1, b) + 1

print(sum(3, 9))