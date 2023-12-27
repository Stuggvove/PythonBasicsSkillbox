print("Задание 1")

menu =  input("Введите список блюд: ").split(";")
print("Ваше меню:", ", ".join(menu))

print("Задание 2")
line = input("Введите строку: ").split()
max_length = 0
longest_word = ''

for word in line:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("Самое длинное слово: «" + longest_word + "».")
print("Длина этого слова: " + str(max_length) + " символов.")

print("Задание 3")
doc = input("Введите документ: ")

start = '@ № $ % ^ & * ( )'.split()
end = '.txt .docx'.split()

if doc[0] in start:
    print("Плохое начало")
elif not (doc.endswith(".txt") or doc.endswith(".docx")):
    print("Плохой конец")
else:
    print("Все хорошо")

print("Задание 4")
text = input("Введите строку: ")
print(text.title())

print("Задание 5")
while True:
    passowrd = input("Введите пароль: ")
    count_sim = len(passowrd)

    flag_upper = False
    for i in passowrd:
        if i.isupper():
            flag_upper = True

    count_num = 0
    for i in passowrd:
        if i.isdigit():
            count_num += 1

    if count_sim >= 8 and flag_upper and count_num >= 3:
        print("Все хорошо")
    else:
        print("Пароль ненадеженый")

print("Задание 6")

text = input('Введите строку: ')

str_len = len(text)
result = ''
if str_len > 0:
    i = 0
    while i < str_len:
        counter = 0
        curr_char = text[i:i + 1]
        while i < str_len and text[i] == curr_char:
            i += 1
            counter += 1
        result += curr_char + str(counter)

print(result)

print("Задание 7")

ip = input('Введите IP: ').split('.')

if len(ip) < 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    count = 0
    range = 0
    for i in ip:
        if i.isdigit():
            count += 1
            if int(i) > 255:
                range += 1
                print(i, 'превышает 255')
        else:
            print(i, '- не целое число')
    if range == 0 and count == 4:
        print('IP-адрес корректен')

print("Задание 8")

first = input("Введите строку: ")
second = input("Введите строку: ")

for i in range(len(first)):
    if first == second:
        print("Первая строка получается из второй со сдвигом", i)
        break
    second = second[-1] + second[:-1]
else:
    print('Нельзя')

print("Задание 9")
def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lo = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char in up:
            uppercase += 1
        elif char in lo:
            lowercase += 1
    return uppercase, lowercase

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
