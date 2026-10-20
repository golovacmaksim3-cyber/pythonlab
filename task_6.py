den = int(input("Введите день рождения (число): "))
mesjac = int(input("Введите месяц рождения (номер): "))

if (mesjac == 3 and den >= 21) or (mesjac == 4 and den <= 19):
    print("Знак зодиака: Овен")
elif (mesjac == 4 and den >= 20) or (mesjac == 5 and den <= 20):
    print("Знак зодиака: Телец")
elif (mesjac == 5 and den >= 21) or (mesjac == 6 and den <= 20):
    print("Знак зодиака: Близнецы")
elif (mesjac == 6 and den >= 21) or (mesjac == 7 and den <= 22):
    print("Знак зодиака: Рак")
elif (mesjac == 7 and den >= 23) or (mesjac == 8 and den <= 22):
    print("Знак зодиака: Лев")
elif (mesjac == 8 and den >= 23) or (mesjac == 9 and den <= 22):
    print("Знак зодиака: Дева")
elif (mesjac == 9 and den >= 23) or (mesjac == 10 and den <= 22):
    print("Знак зодиака: Весы")
elif (mesjac == 10 and den >= 23) or (mesjac == 11 and den <= 21):
    print("Знак зодиака: Скорпион")
elif (mesjac == 11 and den >= 22) or (mesjac == 12 and den <= 21):
    print("Знак зодиака: Стрелец")
elif (mesjac == 12 and den >= 22) or (mesjac == 1 and den <= 19):
    print("Знак зодиака: Козерог")
elif (mesjac == 1 and den >= 20) or (mesjac == 2 and den <= 18):
    print("Знак зодиака: Водолей")
else:
    print("Знак зодиака: Рыбы")