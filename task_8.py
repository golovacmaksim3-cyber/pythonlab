import random

zagadannoe = random.randint(1, 100)
popitka = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while popitka != zagadannoe:
    popitka = int(input("Введите вашу догадку: "))
    if popitka > zagadannoe:
        print("Меньше")
    elif popitka < zagadannoe:
        print("Больше")
    else:
        print("Поздравляю! Вы угадали число!")