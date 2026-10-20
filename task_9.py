print("Типы измерения: 1 - Длина (метры, километры, сантиметры, мили, футы)")
tip = input("Введите тип измерения: ")
ishodnaja = input("Исходная единица (м, км, см, мили, футы): ")
celevaja = input("Целевая единица (м, км, см, мили, футы): ")
znachenie = float(input("Введите значение: "))

v_metrah = 0

if ishodnaja == "м":
    v_metrah = znachenie
elif ishodnaja == "км":
    v_metrah = znachenie * 1000
elif ishodnaja == "см":
    v_metrah = znachenie / 100
elif ishodnaja == "мили":
    v_metrah = znachenie * 1609.34
elif ishodnaja == "футы":
    v_metrah = znachenie * 0.3048

# Теперь переведем из метров в целевую единицу
rezultat = 0

if celevaja == "м":
    rezultat = v_metrah
elif celevaja == "км":
    rezultat = v_metrah / 1000
elif celevaja == "см":
    rezultat = v_metrah * 100
elif celevaja == "мили":
    rezultat = v_metrah / 1609.34
elif celevaja == "футы":
    rezultat = v_metrah / 0.3048

print("Результат конвертации:", rezultat)