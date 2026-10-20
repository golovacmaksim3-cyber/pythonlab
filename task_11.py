vozrast = int(input("Введите возраст заемщика: "))
dohod = float(input("Введите ежемесячный доход: "))
razmer = float(input("Введите размер запрашиваемого кредита: "))
srok = int(input("Введите срок кредита в месяцах: "))
istorija = input("Кредитная история (отличная/хорошая/удовлетворительная/плохая): ")
poruchiteli = input("Есть поручители? (да/нет): ")
zalog = input("Есть залог? (да/нет): ")


mes_platezh = razmer / srok
sootnoshenie = mes_platezh / dohod

risk = "низкий"
stavka = 12.0
rekomendacija = "Одобрить"

if sootnoshenie > 0.5 or istorija == "плохая":
    risk = "критический"
    stavka = 25.0
    rekomendacija = "Отклонить"
elif sootnoshenie > 0.3 or istorija == "удовлетворительная":
    risk = "высокий"
    stavka = 19.0
    if zalog == "да":
        rekomendacija = "Одобрить под залог"
    else:
        rekomendacija = "Отклонить"
elif sootnoshenie > 0.15:
    risk = "средний"
    stavka = 15.0
    rekomendacija = "Одобрить"
else:
    risk = "низкий"
    stavka = 12.0
    rekomendacija = "Одобрить"

print("\n--- Результат оценки ---")
print("Соотношение платежа к доходу:", sootnoshenie)
print("Категория риска:", risk)
print("Предложенная процентная ставка:", stavka, "%")
print("Рекомендация:", rekomendacija)