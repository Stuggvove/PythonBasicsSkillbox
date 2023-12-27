print("Задание 1")

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count = int(input("Введите количество песен: "))
sum = 0.0

for i in range(count):
    title = input("Введите название песни: ")
    sum += violator_songs.get(title, 0)
print(sum)

print("Задание 2")

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

for i in data:
    print(f'{i}: {data.get(i)}')
print()

data['ETH']['total_diff'] = 100
print(f'ETH: {data["ETH"]}')
print()

data["tokens"][0]["fst_token_info"]["name"] = "doge"
result = data["tokens"][0]["fst_token_info"]["name"]
print(result)
print()

total_out = 0
for i in data['tokens']:
    total_out = i.pop('total_out')
data['ETH']['total_out'] = total_out
print(data['ETH'])
print()

old_price = data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = old_price
print(data['tokens'][1]['sec_token_info']['total_price'])

print("Задание 3")

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for code in goods.values():
    count_quantity = 0
    count_cost = 0
    for product in store[code]:
        quantity = product['quantity']
        cost = product['price']
        count_cost += quantity * cost
        count_quantity += quantity

    print('{0} шт, общая стоимость {1} рублей'.format(count_quantity, count_cost))

print("Задание 4")

text = input('Введите текст: ')
sym_dict = dict()
text_dict = dict()

print('Оригинальный')
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1
for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ': ', sym_dict[i_sym])

print('Инвертированный')
for i_letter, i_num in sym_dict.items():
    text_dict.setdefault(i_num, []).append(i_letter)
for i in text_dict:
    print(i, ': ', text_dict[i])

print("Задание 5")

count = int(input("Введите количество пар: "))
text_dict = dict()
for i in range(1, count + 1):
    text = input(f"{i} пара (Через - ): ").lower().split(" - ") # привет - здравствуйте
    text_dict[text[0]] = text[1]
    text_dict[text[1]] = text[0]

while True:
    word = input("Введите слово: ").lower()
    if word in text_dict:
        print(text_dict[word])
    else:
        print("Нет такого слова")

print("Задание 6")

num_orders = int(input('Введите кол-во заказов: '))
orders_data = dict()

for i in range(1, num_orders + 1):
    order = input(f'{i} заказ: ').split(" - ")
    name = order[0]
    pizza = order[1]
    count = order[2]
    count = int(count)

    if name not in orders_data:
        orders_data[name] = {pizza: count}
    else:
        if pizza not in orders_data[name]:
            orders_data[name][pizza] = count
        else:
            orders_data[name][pizza] += count

for name, order in sorted(orders_data.items()):
    print(f'{name}:')
    for pizza, count in sorted(order.items()):
        print('', pizza, count)

print("Задание 7")

def find_common_elements(array_1, array_2, array_3):
    common = []
    for i in array_1:
        if i in array_2 and i in array_3:
            common.append(i)
    return common

def find_unique_elements(array_1, array_2, array_3):
    unique = []
    for i in array_1:
        if i not in array_2 and i not in array_3:
            unique.append(i)
    return unique

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("Задача 1: Решение без множеств")
print(find_common_elements(array_1, array_2, array_3))

print("Задача 2: Решение без множеств")
print(find_unique_elements(array_1, array_2, array_3))

print("Задание 8")

text = input("Введите строку: ")
text_dict = dict()

for i in text:
    text_dict[i] = text_dict.get(i, 0) + 1

odd_count = 0
for i in text_dict.values():
    if i % 2 != 0:
        odd_count += 1

if odd_count <= 1:
    print("Палиндром")
else:
    print("НЕ палиндром")