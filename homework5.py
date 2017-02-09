import random


# Задание 1.1

odd = [str(x) for x in range(1, 101) if x % 2 != 0]
print(odd)


# Задание 1.2
# Оператор hasattr подсмотрен

my_list = [123, 'abc', [0, 1, 2], ('a', 'b'), 456]

not_iter_items = [x for x in my_list if not hasattr(x, '__iter__')]
print(not_iter_items)


# Задание 1.3
# Не нашел короткого способа рандомизировать регистр, поэтому решение "в лоб"
# Списковое выражение > 80 символов, но перенос по строкам еще хуже

text = 'The quick brown fox jumps over the lazy dog'

m = [(x.upper(), ''.join([random.choice([y.upper(), y.lower()]) for y in x]), len(x)) for x in text.split()]
print(m)


# Задание2


class IntToStr(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, str):
            return str(self.value) + other
        else:
            return self.value + other

    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self.value)
        else:
            return other + self.value

if __name__ == '__main__':
    obj = IntToStr(9.2)
    print(obj + 3)
    print('a' + obj)
    print(obj + 'z')


# Задание 3
# Написать класс Stack, у которого есть два метода push(value) и pop().
# Если мы пытаемся сделать pop из пустого стека,
# нужно выбрасывать исключение IndexError.
# Подробнее про стек: https://ru.wikipedia.org/wiki/LIFO


class Stack:
    def __init__(self):
        self.value = None
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print('Stack is {}'.format(self.stack))

    def pop(self):
        try:
            print('Popped item is {}'.format(self.stack[-1]))
            self.stack.pop()
            print('Stack is {}'.format(self.stack))

        except IndexError:
            print('Can\'t pop - stack is empty')


if __name__ == '__main__':
    a = Stack()
    a.push('abc')
    a.push(123)
    a.pop()
    a.pop()
    a.pop()
