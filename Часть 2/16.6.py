print("Задание 1")

from typing import Callable

def check_permission(user):
    def decorator(func: Callable):
        def wrapped_func():
            if user in user_permissions:
                func()
            else:
                raise PermissionError
        return wrapped_func
    return decorator


user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()

print("Задание 2")

from typing import Callable, Optional

app = dict()

def callback(_name_function: Optional[Callable] = None, *, route: str = None) -> Callable:
    def decorator_callback(name_function: Callable) -> Callable:
        app[route] = name_function

        def wrapper(*args, **kwargs):
            function_call = name_function(*args, **kwargs)
            return function_call
        return wrapper

    if _name_function is None:
        return decorator_callback
    return decorator_callback(_name_function)


@callback(route='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

print("Задание 3")

import time
from datetime import datetime


def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for i in format:
            if i.isalpha():
                format = format.replace(i, '%' + i)
        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result
    return wrapped


def log_methods(date):
    def decorate(cls):
        for i in dir(cls):
            if i.startswith("__") is False:
                current_method = getattr(cls, i)
                decorated_method = timer(cls, current_method, date)
                setattr(cls, i, decorated_method)
        return cls
    return decorate



@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

print("Задание 4")

from typing import Callable

def decorator_with_args_for_any_decorator(func: Callable):
    """Это фабрика декораторов."""
    def decorator(*args, **kwargs):
        """Это сам декоратор."""
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        def wrapper(target_func):
            """Это функция-обертка."""
            def inner(*inner_args, **inner_kwargs):
                """Это внутренняя функция."""
                return func(target_func, *args, **kwargs)(*inner_args, **inner_kwargs)
            return inner
        return wrapper
    return decorator

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapper(text: str, num: int) -> None:
        print("Привет", text, num)
        func(text, num)
    return wrapper

@decorated_decorator("рублей", 200, "друзей")
def decorated_function(text: str, num: int) -> None:
    pass

decorated_function("Юзер", 101)

print("Задание 5")

def singleton(cls):
    def wrapped(*args, **kwargs):
        if not wrapped.instance:
            wrapped.instance = cls(*args, **kwargs)
        return wrapped.instance
    wrapped.instance = None
    return wrapped


@singleton
class Example:
    pass

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

print("Задание 6")

import time

class LoggerDecorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f"Вызов функции {func.__name__}")
            print(f"Аргументы: {args}, {kwargs}")
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Результат: {result}")
            print(f"Время выполнения: {end_time - start_time} секунд")
            return result
        return wrapper

@LoggerDecorator()
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result

result = complex_algorithm(10, 50)