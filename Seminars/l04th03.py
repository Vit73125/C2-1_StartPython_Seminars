# 3) Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
# (Вывод тех элементов, которые были без повторов)

# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

lst = [int(num) for num in input("Введите числа через пробел: ").split()]
print(set(lst))