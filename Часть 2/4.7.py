print("Задание 1")
vowels = "аоиеёэыуюя"

text = input("Введите текст: ")
search = [char for char in text if char in vowels]
print("Список гласных букв:", search)
print("Длина списка:", len(search))

print("Задание 2")

num = int(input("Введите число: "))
result = [(1 if x % 2 == 0 else x % 5) for x in range(num)]
print(result)

print("Задание 3")
import random

def gen_list():
    lst = [round(random.uniform(5, 10), 2) for x in range(20)]
    return lst

fst_team = gen_list()
sec_team = gen_list()

result = [(fst_team[i] if fst_team[i] > sec_team[i] else sec_team[i]) for i in range(20)]

print('Первая команда:', fst_team)
print('Вторая команда:', sec_team)
print('Победители тура:', result)

print("Задание 4")
alphabet = 'abcdefg'

task_1 = alphabet[:]

print('1:', task_1)
print('2:', alphabet[::-1])
print('3:', alphabet[::2])
print('4:', alphabet[1::2])
print('5:', alphabet[:1])
print('6:', alphabet[len(alphabet) - 1:])
print('7:', alphabet[int(len(alphabet) / 2):int(len(alphabet) / 2 + 1)])
print('8:', alphabet[int(len(alphabet) - 3):])
print('9:', alphabet[3:5])
print('10:', alphabet[4:2:-1])

print("Задание 5")
text = input('Введите текст: ')

#Первый попавшийся индекс
first_h = text.index("h")
#Наибольший индекс
second_h = text.rindex("h")

result = text[first_h + 1 : second_h]
print(result[::-1])

print("Задание 6")

result = [[i, i + 4, i + 8] for i in range(1, 5)]
print(result)

print("Задание 7")
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [element for inner in nice_list for last in inner for element in last]
print(result)

print("Задание 8")

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))

char_list = [(alphabet[(alphabet.index(i) + shift) % 33] if i != ' ' else ' ') for i in text]

new_str = ''
for i in char_list:
    new_str += i

print(new_str)