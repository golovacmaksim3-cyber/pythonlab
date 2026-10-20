def merge_dicts(d1, d2):
    for kljuch in d2:
        if kljuch in d1:
            if type(d1[kljuch]) == dict and type(d2[kljuch]) == dict:
                merge_dicts(d1[kljuch], d2[kljuch])
            else:
                d1[kljuch] = d2[kljuch]
        else:
            d1[kljuch] = d2[kljuch]

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

merge_dicts(dict_a, dict_b)
print("Результат слияния словарей:", dict_a)