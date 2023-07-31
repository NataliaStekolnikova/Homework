# 1. Нaпишите прогрaмму, котoрая принимает на вход спиcок чисел и выводит на экран в oдну строкy значения,
# котoрые повторяются в нём бoлее одного раза.
# Выводимые числа не дoлжны повторяться, пoрядок их вывода может быть произвольным.

# def find_duplicates(numbers):
#     seen = set()
#     duplicates = set()
#
#     for number in numbers:
#         if number in seen:
#             duplicates.add(number)
#         else:
#             seen.add(number)
#
#     return duplicates
#
# # Ввод списка чисел
# input_string = input("Введите список чисел через пробел: ").split()
# numbers = []
# for number in input_string:
#     numbers.append(int(number))
#
# # Поиск повторяющихся чисел
# duplicates = find_duplicates(numbers)
#
# # Вывод результатов
# print("Повторяющиеся числа:")
# for number in duplicates:
#     print(number)
#
#
# # 2. Нaпишите программу, на вход которой подаётся список чисел одной строкой.
# # Программа должна для каждого элемента этого списка вывести сумму двух его cоседей.
# # Для элeментов списка, являющиxся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# # Например, если на вход подаётся cписок 1 3 5 6 10, то на выход ожидается cписок 13 6 9 15 7.
# # Если на вход пришло только однo число, надо вывести его же.
# # Вывoд должен содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.
#
# input_string = input("Введите список чисел через пробел: ").split()
# numbers = []
# for number in input_string:
#     numbers.append(int(number))
#
# # Проверка, является ли список пустым или содержит только одно число
# if len(numbers) == 0 or len(numbers) == 1:
#     result = numbers  # Если список пуст или содержит только одно число, то результатом будет сам список
# else:
#     result = []  # Результирующий список для хранения сумм соседних элементов
#
#     # Обработка каждого элемента списка
#     for i in range(len(numbers)):
#         # Определение индексов соседних элементов
#         left_neighbor = numbers[i - 1]
#         right_neighbor = numbers[(i + 1) % len(numbers)]  # Используем операцию остатка от деления для обработки крайних элементов
#
#         # Вычисление суммы соседних элементов и добавление в результирующий список
#         sum_neighbors = left_neighbor + right_neighbor
#         result.append(sum_neighbors)
#
# # Вывод результирующего списка
# result_str = ''
# for number in result:
#     result_str += str(number) + ' '
# print(result_str)
#
# # 3. Создайте кортеж с пятью любыми целыми числами от 0 до 3 включительно.
#
# my_tuple = (1, 3, 2, 0, 3)
#
# # 4. Также создайте второй кортеж числами от -3 до 0.
#
# my_second_tuple = (-3, -2, -1, 0, -3)
#
# # 5. Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# my_tuple = (1, 3, 2, 0, 3)
# my_second_tuple = (-3, -2, -1, 0, -3)
#
# my_third_tuple = my_tuple + my_second_tuple
#
# print(my_third_tuple)
#
# # 5. С помощью метода кортежа count() определите в нем количество нулей.
# # Выведите на экран третий кортеж и количество нулей в нем.
#
# my_tuple = (1, 3, 2, 0, 3, -3, -2, -1, 0, -3)
# count_zeros = my_tuple.count(0)
#
# print("Третий кортеж:", my_tuple)
# print("Количество нулей в кортеже:", count_zeros)

# 6. Посчитать количество каждой буквы в введенной строке. Задача - опорная!
# Слышим в Python посчитать - вспоминаем словари.
# Решение должно быть O(n). Использовать setdefault().

string = input("Введите строку: ")
letter_count = {}

# for letter in string:
#
#     if letter in letter_count:
#         letter_count[letter] = letter_count[letter] + 1
#     else:
#         letter_count[letter] = 1

for letter in string:
    letter_count[letter] = letter_count.get(letter,0) + 1

print("Количество каждой буквы:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")

# 6-2. Посчитать количество каждой буквы в введенной строке. Задача - опорная!
# Слышим в Python посчитать - вспоминаем словари.
# Решение должно быть O(n).
from collections import Counter
string = input("Введите строку: ")
letter_count = {}

string = 'some string'
result = Counter(string)

print("Количество каждой буквы:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
