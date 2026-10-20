def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                expected_type = types[i]
                current_value = args[i]
                if not isinstance(current_value, expected_type):
                    raise TypeError(f"Аргумент под номером {i} должен быть типа {expected_type}")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print("Результат:", add(3, 5))
