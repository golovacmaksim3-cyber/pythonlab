def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import datetime
            vremja = str(datetime.datetime.now())
            imya_f = func.name
            stroka_dlya_fayla = f"Время: {vremja}, Функция: {imya_f}, Аргументы: {args}, {kwargs}\n"
            
            f = open(filename, "a", encoding="utf-8")
            f.write(stroka_dlya_fayla)
            f.close()
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("log.txt")
def umnojit(x, y):
    return x * y

print("Результат вызова функции:", umnojit(5, 4))