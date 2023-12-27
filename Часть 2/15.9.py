print("Задание 1")

class File:
    def __init__(self, file_name: str, prefix: str):
        self.file_name = file_name
        self.prefix = prefix
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.prefix)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with File('work1', 'w') as f:
    f.write('TEST')

print("Задание 2")

import math
from abc import ABC


class MyMath(ABC): #Абстрактный класс
    @classmethod #Стаический метод
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(self, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_value(self,edge: int) -> float:
        return edge ** 3

    @classmethod
    def sphere_area(self, radius: int) -> float:
        return 4 * math.pi * radius ** 2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

print("Задание 3")

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "День: {}, Месяц: {}, Год: {}".format(
            self.day, self.month, self.year
        )

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        list = date.split("-")
        day, month, year = int(list[0]), int(list[1]), int(list[2])
        date_obj = cls(day, month, year) #Обращение к самому классу (def __init__ ...)
        return date_obj

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        list = date.split("-")
        day, month, year = int(list[0]), int(list[1]), int(list[2])
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

print("Задание 4")

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self._cache = OrderedDict()
        self._capacity = capacity

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, new_item):
        key, value = new_item
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)

    def get(self, key):
        if key not in self._cache:
            return -1
        else:
            self._cache.move_to_end(key)
            return self._cache[key]

    def print_cache(self):
        for key, value in self._cache.items():
            print(f"{key} : {value}")

# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2")) # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4