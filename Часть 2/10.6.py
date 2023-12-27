print("Задание 1")

summ = 0
line_count = 0
with open('work.txt', 'r') as people_file:
    try:
        for i_line in people_file:
            try:
                length = len(i_line)
                line_count += 1
                if i_line.endswith('\n'):
                    length -= 1
                summ += length
                if length < 3:
                    raise ValueError
            except ValueError:
                print('Имя в строке {} меньше трех букв'.format(line_count))
    except FileNotFoundError:
        print('Файл не найден ')
    finally:
        print('Сумма символов: ', summ)

print("Задание 2")

import random

result = open("out_file.txt", "w")

count = 0
while True:
    number = int(input("Введите число: "))

    rnd = random.randint(1, 14)

    if rnd == 1:
        raise BaseException("Вас постигла неудача!")

    count += number
    print(count)
    if count >= 777:
        result.write(str(count))
        break

print("Задание 3")

def answer(file_str):
    name, mail, age = file_str.split(" ")
    symbol = ("@", ".")
    age = int(age)
    if name.isalpha() is False:
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if age not in range(10, 100):
        raise ValueError("Поле «Имя» содержит НЕ только буквы")
    for char in symbol:
        if char not in mail:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    return file_str


with open("registrations.txt", "r", encoding="utf-8") as file, \
        open('registration_bad.log', 'a', encoding='utf-8') as error, \
        open('registrations_good.log', 'a', encoding='utf-8') as good:
    for str_in_file in file:
        print(str_in_file, end="")
        try:
            str_file = answer(str_in_file)
        except (NameError, ValueError, SyntaxError) as e:
            error.write(str(e))
        else:
            good.write(str_in_file + '\n')

print("Задание 4")

name = input("Введите имя: ")
while True:
    print("Текущий текст (1), написать сообщение (2): ")
    response = input("Введите: ")
    if response == "1":
        try:
            with open("chat.txt", "r") as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print("нет файла")
    elif response == "2":
        new_message = input("Введите сообщение: ")
        with open("chat.txt", "a") as file:
            file.write("{name} : {message} \n".format(name = name, message = new_message))
    else:
        print("Что-то новое?!")

print("Задание 5")

import math

def sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        print("Нельзя вычислить квадратный корень отрицательного числа")
        return None
