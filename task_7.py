minuty_vvod = int(input("Введите израсходованные минуты: "))
sms_vvod = int(input("Введите израсходованные смс: "))
mb_vvod = int(input("Введите израсходованные Мб интернета: "))

baza = 24.99


dop_minuty = minuty_vvod - 60
dop_sms = sms_vvod - 30
dop_mb = mb_vvod - 1024  # 1 ГБ = 1024 Мб
summa_minut = 0
summa_sms = 0
summa_mb = 0

if dop_minuty > 0:
    summa_minut = dop_minuty * 0.89

if dop_sms > 0:
    summa_sms = dop_sms * 0.59

if dop_mb > 0:
    summa_mb = dop_mb * 0.79

promezhutochnaja = baza + summa_minut + summa_sms + summa_mb
nalog = promezhutochnaja * 0.02
itog = promezhutochnaja + nalog

print(f"Базовая сумма тарификации: {baza:.2f} руб.")

if dop_minuty > 0:
    print(f"Сумма за дополнительные минуты: {summa_minut:.2f} руб.")

if dop_sms > 0:
    print(f"Сумма за дополнительные сообщения: {summa_sms:.2f} руб.")

if dop_mb > 0:
    print(f"Сумма за дополнительный интернет: {summa_mb:.2f} руб.")

print(f"Налог (2%): {nalog:.2f} руб.")
print(f"Итоговая сумма к оплате: {itog:.2f} руб.")