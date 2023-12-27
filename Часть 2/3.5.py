print("Задание 1")

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_five = a.count(5)
print('Кол-во цифр 5:', count_five)
for _ in range(count_five):
    a.remove(5)

a.extend(c)
count_three = a.count(3)
print('Кол-во цифр 3:', count_three)

print('Итоговый список:', a)

print("Задание 2")
class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 3))

class_1.extend(class_2)
class_1.sort()
print(class_1)

print("Задание 3")
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = 0
cost = 0
detail = input('Название детали: ')

for i in range(len(shop)):
    if shop[i][0] == detail.lower():
        count += 1
        cost += shop[i][1]
if count > 0:
    print('Кол-во деталей -', count)
    print('Общая стоимость -', cost)
else:
    print('Товар не найден.')

print("Задание 4")
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    command = input('Гость пришел или ушел? ').lower()
    if command == 'пора спать':
        break
    guest_name = input('Имя гостя: ')
    if command == 'пришел':
        if len(guests) >= 6:
            print(f'Прости, {guest_name}, но мест нет.')
        else:
            guests.append(guest_name)
            print(f'Привет, {guest_name}!')
    elif command == 'ушел':
        guests.remove(guest_name)
        print(f'Пока, {guest_name}!')
    print()

print('Вечеринка закончилась, все легли спать.')

print("Задание 5")
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time = 0.0
count = int(input('Сколько песен выбрать? '))
for i in range(count):
    song = input('Введите название песни: ').lower()
    for j in violator_songs:
        if j[0].lower() == song:
            time += j[1]

print(f'Общее время звучания песен: {time} минут')

print("Задание 6")
skates_size = []
foot_size = []
count = 0

number_skates = int(input('Кол-во роликов: '))
for i in range(number_skates):
    size = int(input("Введите размер роликов: "))
    skates_size.append(size)

number_foot = int(input('Кол-во людей: '))
for i in range(number_foot):
    size = int(input("Введите ваш размер: "))
    foot_size.append(size)

for foot in foot_size:
    if foot in skates_size:
        skates_size.remove(foot)
        count += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', count)

print("Задание 7")
guys = int(input('Кол-во человек: '))
number_drop = int(input('Какое число в считалке? '))

piople_list = list(range(1, guys + 1))
index_drop = 0

for i in range(guys - 1):
    start_count = index_drop % len(piople_list)
    index_drop = (start_count + number_drop - 1) % len(piople_list)
    print('Выбывает человек под номером', piople_list[index_drop])
    piople_list.remove(piople_list[index_drop])

print('Остался человек под номером', * piople_list)

print("Задание 8")
def is_symmetric(sequence):
    return sequence == sequence[::-1]

def find_min_addition(sequence):
    i = 0
    while i < len(sequence) // 2:
        if sequence[i] != sequence[-(i + 1)]:
            break
        i += 1
    return len(sequence) - 2 * i

def find_numbers_to_add(sequence, min_addition):
    i = 0
    while i < len(sequence) // 2:
        if sequence[i] != sequence[-(i + 1)]:
            break
        i += 1
    return sequence[:i][::-1]

n = int(input("Количество чисел: "))
sequence = []
for i in range(n):
    num = int(input("Число: "))
    sequence.append(num)

if is_symmetric(sequence):
    print("Последовательность уже симметрична. Ничего добавлять не нужно.")
else:
    min_addition = find_min_addition(sequence)
    print("Нужно приписать чисел: ", min_addition)
    numbers_to_add = find_numbers_to_add(sequence, min_addition)
    print("Сами числа: ", numbers_to_add)