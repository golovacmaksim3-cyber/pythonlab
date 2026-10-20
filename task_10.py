summa = float(input("Введите сумму покупки: "))
vozrast = int(input("Введите возраст покупателя: "))
den_rozhdenija = input("Сегодня День рождения? (да/нет): ")
status_vip = input("Клиент VIP? (да/нет): ")

skidka = 0

if status_vip == "да":
    skidka = 15
else:
    if summa > 1000:
        skidka = 10

    if vozrast >= 63:
        skidka = skidka + 5

    if den_rozhdenija == "да":
        skidka = skidka + 5

if skidka > 25:
    skidka = 25

print("Итоговая скидка составляет:", skidka, "%")