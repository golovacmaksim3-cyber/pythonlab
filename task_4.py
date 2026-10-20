stroka = input("Введите строку: ")

perevernutaja = stroka[::-1]

if stroka == perevernutaja:
    print("Строка является палиндромом!")
else:
    print("Строка не является палиндромом.")