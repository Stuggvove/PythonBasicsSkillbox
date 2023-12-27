import math

# Задача 1. Конвертация.

# При покупках за рубежом 
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, 
# если купить что-то в евро, 
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
# 
# Напишите программу, 
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
# 
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

euro = float(input('Введите стоимость покупки в евро: '))

dol = euro*1.25
rub = dol*60.87
print('Покупка будет стоить в рублях:', round(rub, 2))

# Задача 2. Грубая математика.

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание 
# и функции теперь рассчитываются довольно грубо.
# 
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
# 
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное или равно нулю.
# 
# Пример:
# 
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453
# 
# Введите число: -2.1
# x = -3   exp(x) = 0.049787068367863944
# 
# Введите число: -5.9
# x = -6   exp(x) = 0.0024787521766663585

num = int(input('Введите кол-во чисел: '))

for i in range(num):
    x = float(input('Введите число: '))
    if x > 0:
        x = math.ceil(x)
        print('x =', x, '   log(x) =', math.log(x))
    else:
        x = math.floor(x)
        print('x =', x, '   exp(x) =', math.exp(x))

# Задача 3. Убийца Steam.

# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление,
# пользователю нужно показать сколько процентов уже скачалось,
# чтобы он мог решить пойти заварить чаю, или подождать у экрана компьютера.
# 
# Обновления игры всегда занимают разное количество мегабайт,
# да и скорость интернет-соединения у игроков разная.
# 
# Напишите программу,
# принимающую на вход размер файла обновления в мегабайтах
# и скорость интернет соединения в мегабайтах в секунду.
# 
# Для каждой секунды программа рассчитывает
# и выводит на экран сколько процентов от всего объема уже скачано,
# до тех пор пока не будет скачан весь объем.
# В конце программа должна показать сколько всего секунд заняло скачивание обновления.
# Обеспечьте контроль ввода.
# 
# Пример:
# 
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# 
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))
download = 0
time = 0

while download < size:
    time += 1
    download += speed
    if download > size:
        download = size
    print('Прошло',  time, 'сек.', end = '')
    print('Скачано', download, 'из', size, 'Мб', end = ' ')
    print('(', round(download / size * 100),  '%)')

# Задача 4. Первая цифра.

# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.

num4 = float(input('Введите положительное действительное число: '))
print('Первая цифра после десятичной точки=', int(num4 * 10 % 10))

# Задача 5. Вот это объёмы!

# Для курсовой работы по физике
# Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной,
# которая может в теории существовать в нашей вселенной.
# Андрей хорошо разбирается в формулах,
# а вот считать что-то, а уж тем более самому - это явно не его.
# Объём Земли ему известен заранее  - это 10.8321 * 10 ** 11 км3
# 
# А вот объём случайной планеты ему нужно будет посчитать.
# Благо, у него есть формула
# 
# V = 4/3 πR ** 3
# 
# где V - это объём, π - число пи, а R - радиус планеты.
# 
# Напишите программу, 
# которая получает на вход радиус случайной планеты
# и выводит на экран во сколько раз планета Земля меньше или больше по объёму.
# Ответ округлите до трёх знаков после запятой

# Пример:
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз

# Пример 2:
# Введите радиус случайной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз

planet_radius = float(input('Введите радиус случайной планеты: '))
planet_volume = 4/3 * math.pi * planet_radius ** 3
earth_volume = 10.8321 * 10 ** 11

if earth_volume > planet_volume:
    print('Объём планеты Земля больше в', round(earth_volume / planet_volume, 3), 'раз')
elif earth_volume < planet_volume:
    print('Объём планеты Земля меньше в (1/', round(earth_volume / planet_volume, 3), ') = ', round(planet_volume / earth_volume, 3), 'раз')
else:
    print('Объем планет равен')

# Задача 6. Ход конём.

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

print('Введите местоположение коня:', )
loc_x = float(input(''))
loc_y = float(input(''))
loc_x = int(loc_x*10)
loc_y = int(loc_y*10)

print('Введите местоположение точки на доске:')
loc_point_x = float(input(''))
loc_point_y = float(input(''))
loc_x_point = int(loc_point_x*10)
loc_y_point = int(loc_point_y*10)

x_abs = abs(loc_x_point - loc_x)
y_abs = abs(loc_y_point - loc_y)

print('Конь в клетке ('+ str(loc_x) + ',' + str(loc_y) + '). Точка в клетке (' + str(loc_x_point) + ',' + str(loc_y_point) + ').')

if ((x_abs == 1) and (y_abs == 2)) or ((x_abs == 2) and (y_abs == 1)):
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь не может ходить в эту точку')

# Задача 7. За что?

# Вы встретились со своим старым другом,
# который тоже изучает программирование, правда, в другом учебном заведении.
# За чашкой кофе он пожаловался вам,
# что сумасбродный препод дал им задание написать программу,
# которая из двух введённых чисел определяет наибольшее,
# не используя при этом условные операторы, циклы и встроенные функции вроде max/min/sorted.
# 
# Радуясь, что на вашем курсе такого не требуют,
# вы всё-таки решаете помочь своему другу.
# 
# Напишите для него эту программу.
# 
# Пример:
# 
# Введите первое число: 10
# Введите второе число: 5
# 
# Наибольшее число: 10

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_max = round(((num_1 + num_2) + abs(num_1 - num_2)) / 2)

print("Наибольшее число:", num_max)