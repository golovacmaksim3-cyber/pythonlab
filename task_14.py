nabor1_str = input("Введите первый набор чисел через пробел: ").split()
nabor2_str = input("Введите второй набор чисел через пробел: ").split()

nabor1 = []
for el in nabor1_str:
    nabor1.append(float(el))

nabor2 = []
for el in nabor2_str:
    nabor2.append(float(el))

obshie = []
tolko_v_1 = []
tolko_v_2 = []
razlichnye = []

for ch in nabor1:
    if ch in nabor2:
        if ch not in obshie:
            obshie.append(ch)
    else:
        if ch not in tolko_v_1:
            tolko_v_1.append(ch)

for ch in nabor2:
    if ch not in nabor1:
        if ch not in tolko_v_2:
            tolko_v_2.append(ch)

for ch in nabor1:
    if ch not in obshie:
        if ch not in razlichnye:
            razlichnye.append(ch)
for ch in nabor2:
    if ch not in obshie:
        if ch not in razlichnye:
            razlichnye.append(ch)

print("1. Присутствуют в обоих наборах:", obshie)
print("2. Только в первом:", tolko_v_1, "| Только во втором:", tolko_v_2)
print("3. Из обоих наборов за исключением общих:", razlichnye)