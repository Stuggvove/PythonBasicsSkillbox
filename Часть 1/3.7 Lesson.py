# Задача 1. Язык математики

# В первый же день на сайте отвалилась формула по расчёту рекламной метрики, и только Вася может её поправить. 
# Часть программы с вводными данными представлена ниже, отдельно записана формула на математическом языке.

# Дана программа:

# a = 8
# b = 10
# c = 12
# d = 18

# Продолжите программу: переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.

#
# Выражение: 

# (-3 + a**2) * b - 2**3
#      c- 2 * d

a, b, c , d = 8, 10, 12, 18
result = (((-3) + a**2) * b - 2**3)/(c - 2 * d)
print(result)

# Задача 2. Финансовый отчёт

# Васе пришло очередное задание — автоматизация финансовой отчётности. 
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически. 
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

num_1, num_2, num_3 ,num_4 = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '), input('Введите четвёртое число: ')
sum_1, sum_2 = int(num_1) + int(num_2), int(num_3) + int(num_4)
print(sum_1 / sum_2)

# Задача 3. Следующее и предыдущее числа

# В олимпиаде по программированию участвовали 1000 человек,
# и программа автоматически распределила их по количеству баллов.
# Иногда количество баллов у участников одинаковое,
# и тогда комиссии нужно посмотреть фамилии одного из таких участников,
# а также его соседей, это реализует специальная часть алгоритма.
#
# Напишите программу,
# которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее число.
# Результат: 

# Введите число: 5
# После числа 5 идет число 6
# До числа 5 идет число 4

num_1 = input('Введите число: ')
num_2, num_3 = int(num_1) + 1, int(num_1) - 1
print('После числа', num_1, 'идёт число', num_2)
print('До числа', num_1, 'идёт число', num_3)

# Задача 4. Площадь треугольника

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

a, b = input('Введите длину первого катета: '), input('Введите длину второго катета: ')
s = int(a) * int(b) / 2
print('Площаль треугольника равна:', s)


# Задача 5. Часы

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах 
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

minutes = int(input('Введите количество минут: '))
hours = minutes / 60
remained_minutes = 1 - hours
print(hours, 'Осталось:', remained_minutes)

# Задача 6. Проверяем бухгалтера

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример: 
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

num_1, num_2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
sum = (num_1 % 100) + (num_2 % 100)
print('Сумма:', sum)

# Задача 7. Режем число на части

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

num_1 = int(input('Введите четырёхзначное число: '))
num_2, num_3, num_4, num_5 = num_1 // 1000, ((num_1 // 100) % 100) % 10, ((num_1 // 10) % 10), num_1 % 10
print(num_2, num_3, num_4, num_5)

# Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)

# Вы уже умеете менять местами строковые переменные и знаете, 
# что в переменных кроме строк можно хранить и числа. 
# Напишите программу, которая меняла бы значения двух переменных местами, 
# но без использования третьей переменной и синтаксического сахара, который мы разбирали, а именно: 
# без конструкции a, b = b, a. В переменные будут вводиться только числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a * b
b = a // b
a = a // b
print(a, b)

# Не изменяйте уже написанный код (input-ы и print-ы). Между принтами можно вставить столько строк кода, сколько вам нужно для решения.