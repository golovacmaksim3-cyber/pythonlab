
prodazhi = [
    {"name": "Яблоко", "price": 2.5, "quantity": 100},
    {"name": "Молоко", "price": 3.0, "quantity": 50},
    {"name": "Яблоко", "price": 2.5, "quantity": 30},
    {"name": "Хлеб", "price": 1.5, "quantity": 80}
]

viruchka_tovarov = {}
unikalnie_nazvaniya = []

for item in prodazhi:
    imya = item["name"]
    dohod = item["price"] * item["quantity"]
    
    if imya in viruchka_tovarov:
        viruchka_tovarov[imya] += dohod
    else:
        viruchka_tovarov[imya] = dohod
        
    if imya not in unikalnie_nazvaniya:
        unikalnie_nazvaniya.append(imya)

samyi_pribylnyy = ""
max_dohod = -1

for imya in viruchka_tovarov:
    if viruchka_tovarov[imya] > max_dohod:
        max_dohod = viruchka_tovarov[imya]
        samyi_pribylnyy = imya

print("Выручка по каждому товару:", viruchka_tovarov)
print("Самый прибыльный товар:", samyi_pribylnyy)
print("Количество уникальных наименований:", len(unikalnie_nazvaniya))