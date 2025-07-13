import time
from functools import wraps


#декоратор фиксирующий время выполнения функции, ее результат и возможные ошибки
def log(filename="print"):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                if filename == "print":
                    print(result)
                    print(f"Время выполнения функции: {end_time - start_time}")
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(result)
                        file.write(f"Время выполнения функции: {end_time - start_time}")
                        file.write(f"{func.__name__} ok")
            except Exception as e:
                if filename == "print":
                    print(f"Время выполнения функции: {end_time - start_time}")
                    print(f"{func.__name__} error: {e} Inputs: {args, kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Время выполнения функции: {end_time - start_time}")
                        file.write(f"{func.__name__} error: {e} Inputs: {args, kwargs}")
        return inner
    return wrapper
