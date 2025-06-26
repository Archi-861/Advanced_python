
def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(expected_types)):
                if i < len(args):
                    if not isinstance(args[i], expected_types[i]):
                        arg_name = func.__code__.co_varnames[i]
                        raise TypeError(f'Неверный тип аргумента {arg_name}.'
                                        f'Ожидался {expected_types[i]}, получен {type(args[i])}.')
            return func(*args, **kwargs)
        return wrapper
    return decorator



@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     # 5
print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>