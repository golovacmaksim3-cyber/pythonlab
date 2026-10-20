def unique_elements(spisok):
    rezultat = []
    
    for element in spisok:
        if type(element) == list:
            v_metrah = unique_elements(element)
            for sub_el in v_metrah:
                if sub_el not in rezultat:
                    rezultat.append(sub_el)
        else:
            if element not in rezultat:
                rezultat.append(element)
                
    return rezultat

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("Уникальные элементы:", unique_elements(list_a))