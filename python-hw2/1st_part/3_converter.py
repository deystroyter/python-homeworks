# Конвертер градусов (Цельсий - Фаренгейт - Кельвин)
print("""Слайд 4. "По вариантам"
3. Создайте программу для перевода из одной системы мер в другую (Цельсий - Фаренгейт, мили -
километры, унции - граммы и т.д.).\n""")
def Cel_far(temp):
    return (temp * 9 / 5) + 32


def Far_cel(temp):
    return (5 / 9) * (temp - 32)


def Cel_kelv(temp):
    return temp + 273.15


def Kelv_cel(temp):
    return temp - 273.15


def Get_answ(type, temp):
    if type == 1:
        return temp, "°C", Cel_far(temp), "°F"
    elif type == 2:
        return temp, "°C", Cel_kelv(temp), "Кельвин"
    elif type == 3:
        return temp, "°F", Far_cel(temp), "°C"
    elif type == 4:
        return temp, "°F", Cel_kelv(Far_cel(temp)), "Кельвин"
    elif type == 5:
        return temp, "K", Kelv_cel(temp), "°C"
    elif type == 6:
        return Cel_far(Kelv_cel(temp))
    else:
        print("""Неверно введено значение!""")


user_type = int(input("""Выберите режим конвертации:
        1. Цельсий °C -> Фаренгейт °F
        2. Цельсий °C -> Кельвин K
        ---------------------------
        3. Фаренгейт °F -> Цельсий °C
        4. Фаренгейт °F -> Кельвин K
        ---------------------------
        5. Кельвин K -> Цельсий °C
        6. Кельвин K -> Фаренгейт °F
    
Ввод: """))

user_temp = float(input("""Введите исходуную температуру: """))
answ = Get_answ(user_type, user_temp)

print(answ[0], answ[1], """равно""", answ[2], answ[3])
