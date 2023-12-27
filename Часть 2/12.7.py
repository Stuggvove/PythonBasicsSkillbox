print("Задание 1")

class Property():
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


amount_money = int(input('Введите количество имеющихся денег: '))

wroth_1 = float(input('Стоимость квартиры: '))
nalog_appart = Apartment(wroth_1)
print('Налог на квартиру {}'.format(nalog_appart.tax()))

wroth_2 = float(input('Стоимость машины: '))
nalog_car = Car(wroth_2)
print('Налог на машину {}'.format(nalog_car.tax()))

wroth_3 = float(input('Стоимость дачи: '))
nalog_contrhous = CountryHouse(wroth_3)
print('Налог на дачу {}'.format(nalog_contrhous.tax()))

sum_nalog = nalog_appart.tax() + nalog_car.tax() + nalog_contrhous.tax()

if sum_nalog < amount_money:
    print('Отлично, денег хватает ')
else:
    print('Денег не хватает')

print("Задание 2")

import random

class Buddist:
    def __init__(self, karma = 0):
        self.__karma = karma

    def get_karma(self):
        return self.__karma

    def set_karma(self, closer):
        self.__karma += closer

def one_day(count):
    if random.randint(1,10) == 5:
        with open('karma.log', 'a') as karma_log:
                error = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
                karma_log.write(f"На {count} день случилось - {error}")
                return False
    else:
        return random.randint(1, 7)

budd = Buddist()
day = 0
while budd.get_karma() < 500:
    day += 1
    if one_day(day):
        pass
    else:
        budd.set_karma(one_day((day)))

print('Победа!')

print("Задание 3")



print("Задание 4")

print("Нет доступа к файлам для выполнения этого задания.")

print("Задание 5")

class Srack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return str(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i in sorted(self.task.keys()):
                display.append('{prior} {task}\n'.format(
                    prior=str(i),
                    task=self.task[i]
                )
            )
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Srack()
        self.task[priority].push(task)



manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

print("Задание 6")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print(circle.area())
print(rectangle.area())
print(triangle.area())