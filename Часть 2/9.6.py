print("Задание 1")

numbers = open("numbers.txt", "r")
num = numbers.read()

count = 0
for i in num:
    if i.isdigit():
        count += int(i)
print(count)

numbers.close()

answer = open("answer.txt", "w")
answer.write(str(count))

print("Задание 2")

text = open('work.txt', 'r')
print(*text.readlines()[::-1])
text.close()

print("Задание 3")
import os

path = r'D:\work'
total_size = 0
path, dirs, files = next(os.walk(path))
for f in files:
    fp = os.path.join(path, f)
    total_size += os.path.getsize(fp)

print('Размер каталога (в Кб): ', total_size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))

print("Задание 4")

new_file = open("work.txt", "r", encoding="utf8")
k = int(new_file.readline())

new_list = []

for line in new_file:
    new_line = line.split()

    if new_line != [] and int(new_line[-1]) > k:
        new_list.append(new_line)
new_file.close()

new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()

count = str(len(new_list))

out_lst = []
n = 1
for i in new_list:
    name_sim = str(i[0][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i[1] + ' ' + i[-1]
    out_lst.append(s_win)
    n += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    s = '\n'.join(out_lst)
    f_out.write(s)

for i in out_lst:
    print(f'{i}')

print("Задание 5")

file_text = open('work.txt', 'r', encoding='utf-8')
file_cipher_text = open('cipher_text.txt', 'a')

alfavit_lower = 'abcdefghijklmnopqrstuvwxyz'
alfavit_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
step = 0

def cipher(alfavit, step):
    mesto = alfavit.find(sym)
    if mesto + step > len(alfavit) - 1:
        new_mesto = (mesto + step) - len(alfavit)
        file_cipher_text.write(alfavit[new_mesto])
    else:
        new_mesto = mesto + step
        file_cipher_text.write(alfavit[new_mesto])

for i_elem in file_text:
    step += 1
    for sym in i_elem:
        if sym.islower():
            cipher(alfavit_lower, step)
        elif sym.isupper():
            cipher(alfavit_upper, step)
            file_cipher_text.write('\n')

file_text.close()
file_cipher_text.close()

print("Задание 6")

import collections
import zipfile

def unzip(archive):
    zfile = zipfile.ZipFile(archive, "r")
    for i in zfile.namelist():
        zfile.extract(i)
    zfile.close()

def collect_stats(file_name):
    result = {}
    if file_name.endswith(".zip"):
        unzip(file_name)
        file_name = "".join((file_name[:-3], "txt"))
    text = open(file_name, "r", encoding="utf-8")
    for i in file_name:
        for j in i:
            if j.isalpha():
                if j not in result:
                    result[j] = 0
            result[j] += 1
    text.close()

def sort_by_frequency(stats):
    sorted_values = sorted(stats.values())
    sorted = collections.OrderedDict()
    for i in sorted_values:
        for j in stats.keys():
            if stats[j] == i:
                sorted[j] = stats[j]
    return sorted

file_name = "work.zip"
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)