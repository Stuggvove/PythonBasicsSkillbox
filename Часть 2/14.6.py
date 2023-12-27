print("Задание 1")

from typing import Callable, Any

def how_are_you(func: Callable) -> Callable:
    def wrapped_func() -> Any:
        print('Как у тебя дела?')
        print(input('Ваш ответ: '))
        print('А у меня не очень!')
        return func()
    return wrapped_func

@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')

test()

print("Задание 2")

from typing import Callable
import time

def decorator_waiter(func: Callable) -> Callable:
    time.sleep(4)
    return func

@decorator_waiter
def test_print():
    print("Почему я так долго жду?!")

test_print()

print("Задание 3")

from datetime import datetime
from time import sleep
import functools
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """Декоратор. Логирует ошибки функций с указанием даты и времени возникновения."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(f'{func.__name__}\n{func.__doc__}')
            function = func(*args, **kwargs)
            return function
        except Exception as exc:
            string = '{} - {}:\t{}\n'.format(datetime.now(), func.__name__, exc)
            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(string)

    return wrapped_func

@logging
def division_by_zero():
    """Деление на нoль."""
    sleep(1)
    raise ZeroDivisionError('Деление на ноль')

@logging
def value_error():
    """Вызывает ValueError."""
    sleep(1)
    raise ValueError('Неверное значение')

@logging
def name_error():
    """Вызывает NameError."""
    sleep(1)
    raise NameError('Неверное имя')

@logging
def index_error():
    """Вызывает IndexError."""
    sleep(1)
    raise IndexError('Нет такого индекса')

division_by_zero()
value_error()
name_error()
index_error()

print("Задание 4")

from typing import Callable

def counter_decorator(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        print('Функция вызвана:', wrapped_func.count, 'раз')
        return result

    wrapped_func.count = 0
    return wrapped_func

@counter_decorator
def good():
    print('Я молодец!')

@counter_decorator
def bad():
    print('ПЛОХО!')

good()
good()
good()

bad()
bad()
bad()

print("Задание 5")

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:          
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))