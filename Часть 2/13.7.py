print("Задание 1")

class Square1:
    def __init__(self, num: int):
        self.count = 0
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.num:
            raise StopIteration
        else:
            return self.count * self.count

v1 = int(input("Введите число: "))
class_v1 = Square1(v1 + 1)
for i in class_v1:
    print(i, end=" ")

print()

def square2(number: int):
    for i in range(number):
        yield i ** 2

v2 = int(input("Введите число: "))
for i in square2(v2 + 1):
    print(i, end=" ")

print()

v3 = int(input("Введите число: "))
print(*[i * i for i in range(1, v3 + 1)])

print("Задание 2")

import os.path

def gen_files_path(folder: str, path=os.path.abspath(os.sep)) -> str:
    for elem in os.listdir(path):
        path_elem = os.path.join(os.path.abspath(path), elem)
        if os.path.isfile(path_elem):
            print(path_elem)
            continue
        elif folder == elem:
            print(f"\nКаталог {folder} найден.\nПуть к каталогу: {path_elem}")
        else:
            path_elem = gen_files_path(folder=folder, path=path_elem)
            if path_elem:
                return path_elem


path_search = input("Введите путь для поиска: ")
folder_search = input("Какой каталог будем искать? ")
print("\nПути всех встречающихся файлов\n")
if not gen_files_path(folder=folder_search, path=path_search):
    print(f"\nКаталог {folder_search} не найден")

print("Задание 3")

import os
from collections.abc import Iterable


def strings_count(directory: str) -> Iterable[tuple]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                curr_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                for line in curr_file.readlines():
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(root, file), count


for element in strings_count(directory='..'):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))

print("Задание 4")

from typing import Any, Optional

class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node [{value}]'.format(value=str(self.value))

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> None:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, element: Any) -> None:
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index) -> int:
        cur_node = self.head
        cur_index = 0

        while cur_node is not None:
            if cur_index == index:
                return cur_node.value
            cur_node = cur_node.next
            cur_index += 1

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

print("Задание 5")

import os

def error_log_generator(log_path):
    with open(log_path, 'r') as log_file:
        for line in log_file:
            if 'ERROR' in line:
                yield line

def filter_errors(log_path, output_path):
    with open(output_path, 'w') as output_file:
        for line in error_log_generator(log_path):
            output_file.write(line)

filter_errors('/path/to/log_file.log', '/path/to/output_file.log')