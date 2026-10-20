tekst = input("Введите текст: ")

slova = tekst.split()
obshoe_kolvo = len(slova)

print("Общее количество слов:", obshoe_kolvo)


chastota = {}
for slovo in slova:
    if slovo in chastota:
        chastota[slovo] = chastota[slovo] + 1
    else:
        chastota[slovo] = 1

# Ищем самое частое, самое короткое и самое длинное слово
samoe_chastoe = slova[0]
samoe_korotkoe = slova[0]
samoe_dlinnoe = slova[0]

for slovo in slova:
    if chastota[slovo] > chastota[samoe_chastoe]:
        samoe_chastoe = slovo
    if len(slovo) < len(samoe_korotkoe):
        samoe_korotkoe = slovo
    if len(slovo) > len(samoe_dlinnoe):
        samoe_dlinnoe = slovo

print("Самое часто встречающееся слово:", samoe_chastoe)
print("Самое короткое слово:", samoe_korotkoe)
print("Самое длинное слово:", samoe_dlinnoe)

novye_slova = []
for slovo in slova:
    if len(slovo) >= 3:
        novye_slova.append(slovo)

print("Количество слов после удаления коротких:", len(novye_slova))