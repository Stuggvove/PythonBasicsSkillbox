print("Задание 1")

from typing import List
from math import prod

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

print(list(map(lambda x: round(x ** 3, 3), floats)))
print(list(filter(lambda x: len(x) >= 5, names)))
print(prod(numbers))

print("Задание 2")

from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda x, y: (x, y), letters, numbers)))

print("Задание 3")

from collections import Counter

def can_be_poly(val: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(val).values()))) <= 2

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

print("Задание 4")

from collections import Counter

def count_unique_characters(s):
    s = s.lower()
    counter = Counter(s)
    unique_chars = sum(1 for count in counter.values() if count == 1)
    return unique_chars

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)