print("Задание 1")

class Warrior:
    def __init__(self, name, hp, damage):
        self.name = name  # str
        self.hp = hp  # int
        self.damage = damage  # int

    def hit(self, unit):
        unit.hp -= self.damage
        if unit.hp > 0:
            print(f'"{self.name}" атаковал "{unit.name}". У "{unit.name}" осталось {unit.hp} здоровья')
        else:
            print(f'"{self.name}" атаковал "{unit.name}". "{unit.name}" убит')
            unit.hp = 0
        return unit.hp


from random import randint as rnd

unit1 = Warrior('Воин 1', 100, 20)
unit2 = Warrior('Воин 2', 100, 20)
units = [unit1, unit2]

while True:
    attack_index = rnd(0, 1)  # Кто атакует
    target_index = (attack_index + 1) % 2  # Кого атакует
    target_hp = units[attack_index].hit(units[target_index])
    if target_hp == 0:
        print(f'"{units[attack_index].name}" Победил!')
        break

print("Задание 2")

class Student:
    def __init__(self, fi, number_group, grade):
        self.fi = fi
        self.number_group = number_group
        self.grade = grade

    def average_score(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        result = f'{self.fi} {self.number_group} {self.average_score()}'
        return result


students = []

for i in range(10):
    print(f'Студент {i + 1}: ')
    fi = input('имя: ')
    number_group = int(input('номер группы: '))
    grade = list(map(int, input("оценки: ").split()))
    students.append(Student(fi, number_group, grade))

sort = sorted(students, key=lambda student: student.average_score())
print(*sort, sep='\n')

print("Задание 3")

import random

class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        return f'Я родитель - {self.name}, мне {self.age}'

    def calmChild(self, child):
        if child.calm_state == 1:
            print('Иду успокаивать ребенка')
            child.calm_state = 0
        else:
            print('Ребенок спокоен')

    def feedChild(self, child):
        if child.hungry_state== 1:
            print('Иду кормит ребенка')
            child.hungry_state = 0
        else:
            print('Ребенок сыт')

class Child:
    calm_states = {0: 'спокоен ', 1: 'плачет '}
    hungry_states = {0: 'сыт ', 1: 'голоден '}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_state = 0
        self.hungry_state = 0

    def info(self):
        return f'Я ребенок - {self.name}, мне {self.age}'

    def print_state(self):
        print('Ребенок {} сейчас {}'.format(self.name, Child.calm_states[self.calm_state]))
        print('Ребенок {} сейчас {}'.format(self.name, Child.hungry_states[self.hungry_state]))

parentName = input('Как зовут родителя? ')
parentAge = int(input(f'Сколько {parentName} лет? '))
parent = Parent(parentName, parentAge, children=[])

childName = input('Как зовут ребенка? ')
childAge = int(input(f'Сколько {childName} лет? '))
child = Child(childName, childAge)
parent.children.append(child)

parent.info()

for i_child in parent.children:
    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    i_child.print_state()
    parent.calmChild(i_child)
    parent.feedChild(i_child)

print("Задание 4")

class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()

class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()

class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()

class Shtorm:
    title = 'Шторм'

class Steam:
    title = 'Пар'

class Dirt:
    title = 'Грязь'

class Lightning:
    title = 'Молния'

class Dust:
    title = 'Пыль'

class Lava:
    title = 'Лава'

f = Water()
a = Air()
s = f + a

print(f"Смешиваем '{f.title}' c '{a.title}' и получаем '{s.title}'")

print("Задание 5")

from random import randint, choice

class House:
    food = 50
    money = 0

class Person:

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):  # ест
        self.satiety += 1
        House.food -= 1
        return f'ест, сытость {self.satiety} еда {House.food}'

    def work(self):  # работает
        self.satiety -= 1
        House.money += 1
        return f'работает, сытость {self.satiety} деньги {House.money}'

    def play(self):  # играет
        self.satiety -= 1
        return f'играет, сытость {self.satiety}'

    def repast(self):  # идет в магазин
        House.food += 1
        House.money -= 1
        return f'идет в магазин, еда {House.food} деньги {House.money}'


person_1 = Person('Вася')
person_2 = Person('Федя')

for i in range(365):  # пробуем прожить год
    number_cubes = randint(1, 6)
    person = choice([person_1, person_2])  # рандомно выбираем персону
    if person.satiety < 0:  # голоден - умер. завершаем эксперимент
        print(f'К сожалению, {person.name} помер с голоду ')
        break
    if person.satiety < 20 and House.food >= 10:
        text = person.eat()
    elif House.food < 10:
        text = person.repast()
    elif House.money < 50:
        text = person.work()
    elif number_cubes == 1:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play()
    print(person.name, text)

    print('выжили' if i == 364 else 'все плохо')

print("Задание 6")

class Cell:
    element = "."
    flag = False

    def __init__(self, number):
        self.number = number
        self.element = "."
        self.flag = False

    def cell_info(self):
        print(f"Клетка {self.number} - {self.element}")


class Board:
    one = Cell(1)
    two = Cell(2)
    tree = Cell(3)
    four = Cell(4)
    five = Cell(5)
    six = Cell(6)
    seven = Cell(7)
    eight = Cell(8)
    nine = Cell(9)

    main_board = [one, two, tree,
             four, five, six,
             seven, eight, nine]

    winner_board = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]]

    def render_board(self):
        board = [self.one.element, self.two.element, self.tree.element,
                 self.four.element, self.five.element, self.six.element,
                 self.seven.element, self.eight.element, self.nine.element]

        print(board[0], end=" ")
        print(board[1], end=" ")
        print(board[2])

        print(board[3], end=" ")
        print(board[4], end=" ")
        print(board[5])

        print(board[6], end=" ")
        print(board[7], end=" ")
        print(board[8])

class Player:
    def __init__(self, name):
        self.name = name
        self.closed_cells = []


def logic_game(player, elem):
    while True:
        step1 = int(input(f"{player.name} Введите номер клеточки (1-9): "))
        active_cell = board.main_board[step1 - 1]
        if active_cell.flag == False:
            player.closed_cells.append(step1 - 1)
            active_cell.element = elem
            active_cell.flag = True
            board.render_board()
            break
        else:
            active_cell.cell_info()

def win_checker(player):
    player.closed_cells.sort()
    for i in range(len(board.winner_board)):
        if set(board.winner_board[i]).issubset(player.closed_cells):
            print(f'Победил {player.name}')
            return True

board = Board()
board.render_board()

player1 = Player("X")
player2 = Player("Y")

while True:
    logic_game(player1, "X")
    if win_checker(player1):
        break

    logic_game(player2, "Y")
    if win_checker(player2):
        break

print("Задание 7")

class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0]*cols for _ in range(rows)]
        else:
            self.data = data

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix(self.rows, self.cols, [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix(self.rows, self.cols, [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")
        return Matrix(self.rows, other.cols, [[sum(x*y for x, y in zip(self.data[i], [col[j] for col in other.data])) for j in range(other.cols)] for i in range(self.rows)])

    def transpose(self):
        return Matrix(self.cols, self.rows, [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
