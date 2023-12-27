print("Задание 1")

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = [(key, value["age"]) for key, value in students.items()]
print(pairs)

def work2(students):
    interests = set(sum([students[i]['interests'] for i in students], []))
    len_name = sum(len(students[i]["surname"]) for i in students)
    return interests, len_name

result2 = work2(students)
print(result2[0], "\n", result2[1])

print("Задание 2")


def crypto(checking_list):
    return [v for i, v in enumerate(checking_list) if is_prime(i)]


def is_prime(num):
    divider = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divider += 1
    return divider == 2

checking_list = input("Введиет список: ")
print(crypto(checking_list))

print("Задание 3")

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = [sum((index, value), ()) for index, value in players.items()]
print(result)

print("Задание 4")

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([*map(tuple, zip(list[::2], list[1::2]))])

print("Задание 5")

def tpl_sort(tpl):
    return tuple(sorted(tpl))

tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))

print("Задание 6")

contacts = ['Введите имя и фамилию нового контакта (через пробел): ', 'Введите номер телефона: ']
dict = dict()

while True:
    print('1. Добавить контакт')
    print('2. Найти человека')
    num = input('Введите номер действия: ')

    if num == '1':
        ss = str()

        for i in contacts:
            s = input(i)
            ss += ' ' + s

        ss = ss.split()
        key = (ss[0], ss[1])

        if key in dict:
            print('Такой человек уже есть в контактах.')
        else:
            dict[key] = ss[2]
            print('Текущий словарь контактов:', dict)

    if num == '2':
        num = input('Введите имя или фамилию: ')
        for k in dict.keys():
            if num == k[1]:
                print(k[0], k[1], dict[k])

print("Задание 7")

def min_lens(str, num):
    return min(len(str), len(num))

str = "abcd"
nums = (10, 20, 30, 40)

list = ((str[i], nums[i]) for i in range(min_lens(str, nums)))
print(list)