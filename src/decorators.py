import time
from functools import wraps



def format_inputs(args, kwargs):
    """"Функция, которая формирует аргументы"""
    parts = []
    if args:
        parts.append(f"args: {args}")
    if kwargs:
        parts.append(f"kwargs: {kwargs}")
    return ", ".join(parts) if parts else "no inputs"


#декоратор фиксирующий время выполнения функции, ее результат и возможные ошибки
def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                message = f"{result}\n{func.__name__} ok"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                end_time = time.perf_counter()
                inputs = format_inputs(args, kwargs)
                message = f"{func.__name__} error: {e} Inputs: {inputs}"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                raise
        return inner
    return wrapper
