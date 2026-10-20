parol = input("Введите пароль: ")
dlina = len(parol)

if dlina < 16:
    print("Слишком короткий")
elif parol.isalpha() or parol.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")