# 1. Нaпишите прогрaмму, котoрая принимает на вход спиcок чисел и выводит на экран в oдну строкy значения,
# котoрые повторяются в нём бoлее одного раза.
# Выводимые числа не дoлжны повторяться, пoрядок их вывода может быть произвольным.

def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return duplicates
input_string = input("Введите список чисел через пробел: ").split()
numbers = []
for number in input_string:
    numbers.append(int(number))
duplicates = find_duplicates(numbers)
print("Повторяющиеся числа:")
for number in duplicates:
    print(number)

# 2. Нaпишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его cоседей.
# Для элeментов списка, являющиxся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся cписок 1 3 5 6 10, то на выход ожидается cписок 13 6 9 15 7.
# Если на вход пришло только однo число, надо вывести его же.
# Вывoд должен содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.

input_string = input("Введите список чисел через пробел: ").split()
numbers = []
for number in input_string:
    numbers.append(int(number))
if len(numbers) == 0 or len(numbers) == 1:
    result = numbers
else:
    result = []
    for i in range(len(numbers)):
        left_neighbor = numbers[i - 1]
        right_neighbor = numbers[(i + 1) % len(numbers)]
        result.append(left_neighbor + right_neighbor)
result_str = ' '.join([str(item) for item in result])
print(result_str)

# 3. Создайте кортеж с пятью любыми целыми числами от 0 до 3 включительно.
my_tuple = (1, 3, 2, 0, 3)

# 4. Создайте второй кортеж числами от -3 до 0.
my_second_tuple = (-3, -2, -1, 0, -3)

# 5. Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
my_tuple = (1, 3, 2, 0, 3)
my_second_tuple = (-3, -2, -1, 0, -3)
print(my_tuple + my_second_tuple)

# 6. С помощью метода кортежа count() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.
my_tuple = (1, 3, 2, 0, 3, -3, -2, -1, 0, -3)
print(my_tuple.count(0))

# 7. Посчитать количество каждой буквы в введенной строке. Задача - опорная!
# Слышим в Python посчитать - вспоминаем словари.
# Решение должно быть O(n). Использовать setdefault().
input_string = input("Введите строку: ")
letter_count = {}

for char in input_string:
    letter_count.setdefault(char, 0)
    letter_count[char] += 1

print("Количество каждой буквы:")
for letter, count in letter_count.items():
    print(letter, ":", count)

# 7-2. Посчитать количество каждой буквы в введенной строке. Задача - опорная!
# Слышим в Python посчитать - вспоминаем словари.
# Решение должно быть O(n).
from collections import Counter
string = input("Введите строку: ")
letter_count = Counter(string)

print("Количество каждой буквы:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")

# Задачи для домашней работы
# 1. Пары элементов.
# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами. Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
def count_equal_pairs(numbers):
    numbers_list = numbers.split()
    count_dict = {}
    for num in numbers_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    pair_count = 0
    for count in count_dict.values():
        if count > 1:
            pair_count += count * (count - 1) // 2

    return pair_count

numbers = input("Введите числа, разделенные пробелами: ")
pair_count = count_equal_pairs(numbers)
print("Количество пар элементов, равных друг другу:", pair_count)

# 2. Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.
from collections import Counter
input_list = [1, 2, 3, 4, 2, 3, 5, 1, 6, 7, 6]
counter = Counter(input_list)
print("Уникальные элементы в списке:")
for element in input_list:
    if counter[element] == 1:
        print(element)

# 3. Упорядоченный список
# Дан список целых чисел. Требуется переместить все ненулевые элементы
# в левую часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
def move_zeros(nums):
    left = 0
    for current in range(len(nums)):
        print("Шаг", current, ": ", end="")
        if nums[current] != 0:
            print("Было: num[",left,"]=",nums[left],", nums[",current,"]=",nums[current],"стало: ", end="")
            nums[left], nums[current] = nums[current], nums[left]
            print("num[",left,"]=",nums[left],", nums[",current,"]=",nums[current])
            left += 1
        else:
            print("пропускаем")
    return nums
numbers = [0, 0, 1, 0, 3, 12, 0, 0, 7, 0, 0, 1]
print("Исходный список:\n[0, 0, 1, 0, 3, 12, 0, 0, 7, 0, 0, 1]")
print(move_zeros(numbers))

# 4. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
my_list = ['a', 'b', 'c']
my_tuple = tuple(my_list)
print(my_tuple)  # ('a', 'b', 'c')

# 5. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
my_tuple = ('a', 'b', 'c')
my_list = list(my_tuple)
print(my_list) # ['a', 'b', 'c']

# 6. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', 2, 'python'
print(a) # a
print(b) # 2
print(c) # python

# 7. Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементу последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.
my_tuple = (1,)
sum_value = 0
for value in my_tuple * 3:
    sum_value += value
    print(sum_value)
print(len(my_tuple))

# 8. Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

while num2:
    num1, num2 = num2, num1 % num2

print("Наибольший общий делитель (НОД):", num1)

# 9. *Города*. Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах
# (Брест есть в Беларуси и Франции).
countries = {}
cities_to_find = []  
n = int(input("Введите количество стран: "))
for _ in range(n):
    data = input("Введите название страны и относящиеся к ней города: ").split()
    country = data[0]
    cities = data[1:]
    for city in cities:
        if city in countries:
            countries[city].append(country)
        else:
            countries[city] = [country]
m = int(input("Введите количество городов для поиска: "))
for _ in range(m):
    city = input("Введите название города: ")
    cities_to_find.append(city)
for city in cities_to_find:
    if city in countries:
        country_list = countries[city]
        print(f"Город {city} находится в странах: {' и '.join(country_list)}")
    else:
        print(f"Информация о городе {city} не найдена")


# 10. Во входной строке записан текст. Словом считается последовательность непробельных символов, идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных слов содержится в этом тексте
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
text = input()
result = count_unique_words(text)
print(result)

# 11. Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.
def count_common_numbers(list1, list2):
    return len(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = count_common_numbers(list1, list2)
print(result)  # 2

# 12. Даны два списка чисел. Посчитайте, сколько различных чисел
# входит только в один из этих списков.
def count_unique_numbers(list1, list2):
    return len(set(list1) ^ set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = count_unique_numbers(list1, list2)
print("Количество различных чисел, входящих только в один из списков:", result)

# 13. *Языки*
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# Пример входных данных:
# 3 # N количество школьников
# 2 # M1 количество языков первого школьника
# Russian # языки первого школьника
# English
# 3 # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
# *Выходные данные*
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.

def how_many_languages_pupils_know():
    n = int(input("Введите количество школьников: "))
    all_languages = set()
    any_languages = set()
    for i in range(n):
        m = int(input(f"Введите количество языков {i + 1}-го школьника: "))
        languages = set()
        for j in range(m):
            language = input(f"Введите название {j + 1}-го языка {i + 1}-го школьника: ")
            languages.add(language)
        if i == 0:
            all_languages = languages
        else:
            all_languages &= languages
        any_languages |= languages
    print("Количество языков, которые знают все школьники:", len(all_languages))
    print("Список языков, которые знают все школьники:")
    for language in all_languages:
        print(language)
    print("Количество языков, которые знает хотя бы один школьник:", len(any_languages))
    print("Список языков, которые знает хотя бы один школьник:")
    for language in any_languages:
        print(language)
how_many_languages_pupils_know()

# 14. Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].
result = [prefix + suffix for prefix in 'xy' for suffix in 'yzv']
print(result)

# 15. Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz'].
result = result[::2]
print(result)

# 16. Используйте генератор списков чтобы получить следующий ['1x', '2x', '3x', '4x'].
result = [str(i) + 'x' for i in range(1, 5)]
print(result)

# 17. Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.
result = [item for item in result if item != '2x']
print(result)

# 18. Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
original_list = ['1x', '3x', '4x']
new_list = original_list.copy()
new_list.append('2x')
print("Исходный список:", original_list)
print("Новый список:", new_list)

# 19. Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
dictionary = {x: x**3 for x in range(1, 21)}
print(dictionary)

# 20. Создайте множество с помощью генератора множеств, состоящее из общих делителей чисел 1000 и 9000.
divisors = {i for i in range(1, 1001) if 1000 % i == 0 and 9000 % i == 0}
print(divisors)

# 21. Создайте генератор, который возвращает следующее число Фибоначчи.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создание экземпляра генератора
fib_gen = fibonacci_generator()

# Получение следующего числа Фибоначчи
next_fibonacci = next(fib_gen)
print(next_fibonacci)

# Получение ещё одного следующего числа Фибоначчи
next_fibonacci = next(fib_gen)
print(next_fibonacci)

# 22. Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
# Пример для числа 3:
# 0 0 0	0
# 0	1 2	3
# 0	2 4	6
# 0	3 6	9
def multiplication_table_generator(n):
    for i in range(n + 1):
        row = [str(i * j) for j in range(n + 1)]
        yield '\t'.join(row)

# Запрос числа у пользователя
number = int(input("Введите число: "))

# Создание экземпляра генератора
table_gen = multiplication_table_generator(number)

# Печать строк таблицы умножения
for row in table_gen:
    print(row)


