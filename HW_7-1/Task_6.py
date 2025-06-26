
def call_limit(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise RuntimeError(f'Превышено максимальное количество вызовов функции {func.__name__}.')
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator




@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")    # Вывод: Первый вызов
print_message("Второй вызов")    # Вывод: Второй вызов
print_message("Третий вызов")    # Вывод: Третий вызов
print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '