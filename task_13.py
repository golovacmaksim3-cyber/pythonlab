vvod = input("Введите список чисел через пробел: ")
elementy = vvod.split()
chisla = []

for el in elementy:
    if "." in el:
        chisla.append(float(el))
    else:
        chisla.append(int(el))

unikalnie = []
povtoriajuschiesja = []
chetnye = []
nechetnye = []
otricatelnye = []
plavajuschie = []
suma_kratnih_5 = 0

for chislo in chisla:
    # Уникальные и повторяющиеся
    if chislo not in unikalnie:
        unikalnie.append(chislo)
    else:
        if chislo not in povtoriajuschiesja:
            povtoriajuschiesja.append(chislo)
    
    # Четные и нечетные (только для целых)
    if type(chislo) == int or chislo % 1 == 0:
        if int(chislo) % 2 == 0:
            chetnye.append(chislo)
        else:
            nechetnye.append(chislo)
            
    # Отрицательные
    if chislo < 0:
        otricatelnye.append(chislo)
        
    # С плавающей точкой
    if type(chislo) == float or "." in str(chislo):
        if chislo % 1 != 0:
            plavajuschie.append(chislo)
            
    # Кратные 5
    if chislo % 5 == 0:
        suma_kratnih_5 += chislo

samyi_bolshoy = chisla[0]
samyi_malenkiy = chisla[0]
for chislo in chisla:
    if chislo > samyi_bolshoy:
        samyi_bolshoy = chislo
    if chislo < samyi_malenkiy:
        samyi_malenkiy = chislo

print("1. Уникальные числа:", unikalnie)
print("2. Повторяющиеся числа:", povtoriajuschiesja)
print("3. Четные:", chetnye, "/ Нечетные:", nechetnye)
print("4. Отрицательные числа:", otricatelnye)
print("5. Числа с плавающей точкой:", plavajuschie)
print("6. Сумма чисел, кратных 5:", suma_kratnih_5)
print("7. Самое большое число:", samyi_bolshoy)
print("8. Самое маленькое число:", samyi_malenkiy)