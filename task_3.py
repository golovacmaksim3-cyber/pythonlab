summa = int(input("Введите сумму в рублях: "))

k100 = summa // 100
ost = summa % 100

k50 = ost // 50
ost = ost % 50

k10 = ost // 10
ost = ost % 10

k5 = ost // 5
ost = ost % 5

m2 = ost // 2
ost = ost % 2

m1 = ost

print("Для размена потребуется:")
print("Купюр по 100 руб:", k100)
print("Купюр по 50 руб:", k50)
print("Купюр по 10 руб:", k10)
print("Купюр по 5 руб:", k5)
print("Монет по 2 руб:", m2)
print("Монет по 1 руб:", m1)