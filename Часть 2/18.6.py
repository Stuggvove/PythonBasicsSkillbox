print("Задание 1")

import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

print(re.findall(r"\b[a-zA-Z]{4}\b", text))

print("Задание 2")

import re

def work2(number: str) -> None:
    if re.match(r'^\w\d\d\d\w\w\d\d\d?$', number):
        print('Private')
    if re.match(r'^\w\w\d\d\d\d\d\d?$', number):
        print('Taxi')
    print('Fail')

work2('A203AA11')

print("Задание 3")

import requests
import json

def get_ship_info():
    response = requests.get('https://swapi.dev/api/starships/12/')
    data = response.json()

    ship_info = {
        'name': data['name'],
        'max_speed': data['max_atmosphering_speed'],
        'class': data['starship_class'],
        'pilots': []
    }

    for pilot_url in data['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        ship_info['pilots'].append({
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'weight': pilot_data['mass'],
            'homeworld': pilot_data['homeworld'],
            'homeworld_link': pilot_data['homeworld']['url']
        })

    with open('millennium_falcon.json', 'w') as f:
        json.dump(ship_info, f)

    print(ship_info)

get_ship_info()

print("Задание 4")

import re

phone_list = ['9999999999', '999999-999', '99999x9999', '+79261234567', '89261234567', '79261234567',
              '+7 926 123 45 67', '8(926)123-45-67', '123-45-67', '9261234567', '79261234567', '(495)1234567',
              '(495) 123 45 67', '89261234567', '8-926-123-45-67', '8 927 1234 234', '8 927 12 12 888',
              '8 927 12 555 12', '8 927 123 8 123']

pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'


def clean_up_number(phone_number: str, print_debug: bool = False) -> str:
    removed_chars = [' ', '(', ')', '+', '-', '.', ',', '!']
    clear_number = ''.join(filter(lambda x: x not in removed_chars, phone_number))
    if print_debug:
        print(f'🔁 Грязный номер: {phone_number} Чистый номер: {clear_number}')
    return clear_number


def check_phone_number(phone_number: str, check_length: bool = True, min_length: int = 10, pattern: str = None) -> bool:
    if check_length:
        if len(phone_number) < min_length:
            return False

    if pattern is None:
        pat = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    else:
        pat = pattern

    if re.search(pat, phone_number):
        return True
    else:
        return False


def check_number(phone_number: str, pattern: str) -> bool:
    if re.match(pattern, phone_number) and len(phone_number) == 10:
        return True
    else:
        return False

counter = 0
for item in phone_list:
    counter += 1
    res = 'всё в порядке' if check_phone_number(clean_up_number(item, True)) else 'не подходит'
    print(f'{counter} номер {item}: {res}')
print('*' * 40 + '\n')

counter = 0
for item in phone_list:
    counter += 1
    res = 'всё в порядке' if check_number(clean_up_number(item), pattern) else 'не подходит'
    print(f'{counter} номер {item}: {res}')
print('*' * 40 + '\n')

counter = 0
for item in phone_list:
    counter += 1
    res1 = 'всё в порядке' if check_phone_number(clean_up_number(item)) else 'не подходит'
    res2 = 'всё в порядке' if check_number(clean_up_number(item), pattern) else 'не подходит'
    print(f'{counter} номер {item}: {res1} - {res2}')

print("Задание 5")

import requests
from lxml import html
response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
h3 = html.fromstring(response).xpath('//h3')
for element in h3:
    print(element.text)

print("Задание 6")

import os
import json

def load_json_files(old_file, new_file):
    with open(old_file, 'r') as f:
        old_data = json.load(f)

    with open(new_file, 'r') as f:
        new_data = json.load(f)

    return old_data, new_data

def compare_parameters(old_data, new_data, diff_list):
    result = {}
    for param in diff_list:
        if old_data.get(param) != new_data.get(param):
            result[param] = new_data[param]
    return result

def save_result_to_file(result, filename):
    with open(filename, 'w') as f:
        json.dump(result, f)

old_data, new_data = load_json_files('json_old.json', 'json_new.json')
diff_list = ['services', 'staff', 'datetime']
result = compare_parameters(old_data, new_data, diff_list)
save_result_to_file(result, 'result.json')

print(result)