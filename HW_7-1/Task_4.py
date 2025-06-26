
def trace(func):
    level = 0
    def wrapper(*args, **kwargs):
        nonlocal level
        indent = '    ' * level
        print(f'{indent}--> Вход в функцию {func.__name__} с аргументами {args}, {kwargs}')
        level += 1
        result = func(*args, **kwargs)
        level -= 1
        indent = '    ' * level
        print(f'{indent}<-- Выход из функции {func.__name__} с результатом {result}.')
        return result
    return wrapper



@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)
# Вывод:
# --> Вход в функцию 'factorial' с аргументами (3,), {}
#     --> Вход в функцию 'factorial' с аргументами (2,), {}
#         --> Вход в функцию 'factorial' с аргументами (1,), {}
#             --> Вход в функцию 'factorial' с аргументами (0,), {}
#             <-- Выход из функции 'factorial' с результатом 1
#         <-- Выход из функции 'factorial' с результатом 1
#     <-- Выход из функции 'factorial' с результатом 2
# <-- Выход из функции 'factorial' с результатом 6
