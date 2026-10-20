def cache(func):
    katalog = {}
    def wrapper(*args):
        if args in katalog:
            print("Берем из кэша!")
            return katalog[args]
        else:
            rezultat = func(*args)
            katalog[args] = rezultat
            return rezultat
    return wrapper

@cache
def tyazhelaya_funkciya(n):
    print("Считаем значение...")
    return n * 100

print(tyazhelaya_funkciya(5))
print(tyazhelaya_funkciya(5))