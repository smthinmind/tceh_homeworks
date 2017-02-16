
import sys
import random
from datetime import datetime, date, time, timedelta
import time


# Task 1:

def my_1st_decorator(function):
    def cancell_the_function(*args):
        print('{} will not be called'.format(function.__name__))
    return cancell_the_function


@ my_1st_decorator
def my_function():
    print('My function works!')


@ my_1st_decorator
def my_another_function():
    print('It works too!')


@ my_1st_decorator
def one_more_fuction(x, y):
    result = 0
    for i in range(x, y):
        if i % 2 == 0:
            result += i
    return print(result)


if __name__ == '__main__':

    my_function()
    my_another_function()
    one_more_fuction(0, 100)


# Task 2:

def function_runtime(function):
    def check_runtime(*args):
        runtime = time.time()
        print('Function starts! Result is: ')

        function(*args)

        runtime = round(time.time() - runtime, 2)
        print('Function runtime is {}s'.format(runtime), '\n')

    return check_runtime


@function_runtime
def function_1(x):
    result = 0
    for i in range(x):
        result += 1
    return print(result)


@function_runtime
def function_2(x):
    result = 0
    for i in range(x):
        result += i
    return print(result)


@function_runtime
def function_3(x, y):
    result = 0
    for i in range(x, y):
        if i % 2 == 0:
            result += i
    return print(result)


if __name__ == '__main__':

    function_1(20000000)
    function_2(20000000)
    function_3(0, 20000000)


# Task 3:

l = (i for i in range(101) if i % 2 == 0)
print(l)
print(list(l))


# Task 4:

def asc():
    a = int(input('Start randomizer from: '))
    b = int(input('With step no more: '))
    while True:
        c = random.randint(a, a + b)
        yield c
        a = c


if __name__ == '__main__':

    asc_gen = asc()

    for i in range(10):
        print(next(asc_gen))


# Task 5:

def day_by_day_from(year, month, day):
    from_date = date(year, month, day)
    delta = timedelta(days=1)
    while True:
        yield from_date
        from_date = from_date + delta


if __name__ == '__main__':

    day_by_day = day_by_day_from(2017, 2, 13)

    for i in range(10):
        print(next(day_by_day))
