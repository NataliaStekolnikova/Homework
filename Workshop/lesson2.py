import random

# Нужно угадать секретное трехзначное число на основе подсказок.
# В ответ на вашу попытку игра предлагает одну из следующих подсказок:
# "piko", когда ваше предположение имеет правильную цифру, но на неправильном месте,
# "fermi", когда ваше предположение имеет правильную цифру в правильном месте, и
# "bagels", если ваше предположение не имеет правильных цифр.
# У вас есть 10 попыток, чтобы угадать секретное число.

from random import randint

def generate_secret_number():
    # Генерирует случайное трехзначное число
    random_secret = str(randint(100, 999))
    return [int(digit) for digit in random_secret]

def get_user_guess():
    # Запрашивает у пользователя предположение и проверяет его
    while True:
        user_guess = input("Введите ваше предположение (это должно быть трехзначное число): ")
        if len(user_guess) != 3 or not user_guess.isdigit():
            print("Некорректный ввод. Введите трехзначное число.")
            continue
        return [int(digit) for digit in user_guess]

def give_hint(secret_number, user_guess):
    # Генерирует подсказку на основе секретного числа и предположения
    hint = []
    for i, digit in enumerate(user_guess):
        if digit == secret_number[i]:
            hint.append("fermi (правильная цифра в правильном месте)")
        elif digit in secret_number:
            hint.append("piko (вправильная цифра, но на неправильном месте)")
    if not hint:
        hint.append("bagels (не имеет правильных цифр)")
    return hint

def play_game():
    # Основной цикл игры
    print("Игра 'Быки и коровы'!")
    secret_number = generate_secret_number()
    for _ in range(10):
        user_guess = get_user_guess()
        hint = give_hint(secret_number, user_guess)
        print(", ".join(hint))
        if hint == ["fermi (правильная цифра в правильном месте)"] * 3:
            print("Вы выиграли!")
            return
    print("Вы проиграли. Загаданное число было" + str(secret_number))

play_game()