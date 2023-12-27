import copy

print("Задание 1")

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)
print_numbers(10)

print("Задание 2")

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(dict, key, depth = None):
    if depth is None or depth >= 1:
        if key in dict:
            return dict[key]
    else:
        return None
    for element in dict.values():
        if isinstance(element, dict):
            result = find_key(element, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


key = input('Введите искомый ключ: ')
maximum_depth = int(input('Введите максимальную глубину: '))
value_key = find_key(site, key, maximum_depth)
print(f'Значение ключа: {value_key}')

print("Задание 3")

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать',
        }
    }
}

def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site
    for i in struct.values():
        if isinstance(i, dict):
            result = find_key(i, key, meaning)
            if result:
                return site

number_sites = int(input("Количество сайтов: "))
d_copy = dict()
goods = dict()

for i in range(number_sites):
    name_product = input("Название продукта: ")
    key = {"title" : f"Куплю/продам {name_product} недорого", 'h2': f"У нас самая низкая цена на {name_product}"}
    for j in key:
        find_key(site, j, key[j])
    name_of_product = f'Сайт для {name_product}:'
    d_copy = copy.deepcopy(site)
    goods[name_of_product] = d_copy
    for key, value in goods.items():
        print(key)
        print(value)

print("Задание 4")

def sum(*args):
    if not any(type(arg) == list for arg in args):
        result = 0
        for arg in args:
            result += arg
        return result

    unpacked = []
    for arg in args:
        if type(arg) != list:
            unpacked.append(arg)
        else:
            unpacked.extend(arg)
    return sum(*unpacked)

print(sum([[1, 2, [3]], [1], 3]))

print("Задание 5")

def my_list(*args):
    lst = []
    for elem in args:
        for sub_elem in elem:
            if not isinstance(sub_elem, list):
                lst.append(sub_elem)
            else:
                result = my_list(sub_elem)
                lst.extend(result)
    return lst

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(my_list(nice_list))

print("Задание 6")

def partition(lst):
    pivot = lst[-1]
    less = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst if x > pivot]
    return less, equal, greater

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        less, equal, greater = partition(lst)
        return quicksort(less) + equal + quicksort(greater)

lst = [5, 8, 9, 4, 2, 9, 1, 8]
print(quicksort(lst))