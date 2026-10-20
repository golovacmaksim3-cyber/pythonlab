def flatten_list(spisok):
    i = 0
    while i < len(spisok):
        element = spisok[i]
        if type(element) == list:
            spisok.pop(i)
            element.reverse()
            for el in element:
                spisok.insert(i, el)
            element.reverse()
        else:
            i += 1
            
    for el in spisok:
        if type(el) == list:
            flatten_list(el)

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print("Плоский список:", list_a)