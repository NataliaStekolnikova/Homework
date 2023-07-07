#Задачи для закрепления на занятии
# 1. Базовые операции со строками.
# Вводится строка. Удалить из нее все пробелы, после этого определить, является ли она палиндромом,
# т.е. одинаково пишется как с начала так и с конца.
s = input("Введите строку: ")
s = s.replace(" ", "")  # Удаление пробелов из строки
if s == s[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")

# 2. Базовые операции со строками.
# Найти самое длинное слово в введенном предложении
s = input("Введите предложение: ")
words = s.split()
longest_word = max(words, key=len)
print("Самое длинное слово в предложении:", longest_word)

# 3. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
import re
sentence = input("Введите предложение: ")
words = re.findall(r'\b[\w-]+\b', sentence) # Разбиваем предложение на слова с помощью регулярного выражения, включая дефисы
longest_word = max(words, key=len)
print(f"Самое длинное слово: {longest_word}")

# 4. Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc cde def", то должно быть выведено "abcdef".
input_string = input("Введите строку: ")
input_string = input_string.replace(" ", "")
unique_chars = set()
result = ""
for char in input_string:
    if char not in unique_chars:
        result += char
        unique_chars.add(char)
print("Результат:", result)


# 5. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Учитывать только английские буквы.
input_string = input("Введите строку: ")
lowercase_count = 0
uppercase_count = 0
for char in input_string:
    if 'a' <= char <= 'z':
        lowercase_count += 1
    else:
        if 'A' <= char <= 'Z':
            uppercase_count += 1
print("Количество строчных букв:", lowercase_count)
print("Количество прописных букв:", uppercase_count)
