import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        end = time.time()
        milli = (end - start) * 1000
        print(f"Время выполнения функции '{func.name}': {milli:.4f} мс")
        return rezultat
    return wrapper

@timing
def prim_cikla():
    s = 0
    for i in range(100000):
        s += i
    return s

prim_cikla()