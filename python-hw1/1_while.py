print("""1. Каждый день я пробегаю «следующую степень двойки» км.
Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км?""")


def running1(km):
    # сама двойка
    i = 2
    # c какой степени начинать
    day = 0
    while km > 0:
        km -= i ** day
        day += 1
    return day


userKm1 = 1000
print("Ответ:", userKm1, "км за", running1(userKm1), "дней")

print("""2. Каждый день я пробегаю «следующее простое число» км. 
Сколько дней пройдет, покая в сумме пробегу 1000 км? 10000 км? 
(дополнительная задача, понять, как отличается от номера 1)""")


def running2(km):
    # первое число
    prost = 1
    # cчётчик дней
    day = 0
    while km > 0:
        while True:
            prost += 1
            num = 2
            while True:
                if (prost % num) == 0:
                    if prost == num:
                        break
                    else:
                        break
                else:
                    num += 1
            if prost == num:
                break
        km -= prost
        day += 1
    return day


userKm2 = 1000
print("Ответ:", userKm2, "км за", running2(userKm2), "дней")

print("""3. Начав тренировки, спортсмен в первый день пробежал 10 км.
Для увеличения выносливости ему необходимо повышать норму бега 
через одну тренировку на 15% от нормы предыдущей тренировки.
Спортсмен тренируется каждый день. Какой суммарный путь 
он пробежит за 30 дней.""")


def running3(days):
    dist = 10
    dpd = 10
    daycount = 1
    while daycount <= days:
        if (daycount % 2) == 0:
            dpd = dpd * 1.15
        dist += dpd
        daycount += 1
    return dist


userdays = 30
print("Ответ:", running3(userdays), "км за", userdays, "дней")

print("""4. Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый следующий день
он увеличивал дневную норму на 10% от нормы предыдущего дня.
Через сколько дней:
а) спортсмен будет пробегать в день больше 20 км;
b) пробежит суммарный путь 100 км.""")


def running4(userdpd, userdist):
    l = [0, 0]
    dist = 10
    dpd = 10
    daycount = 1
    while daycount <= 30:
        if (dpd > userdpd) & (l[0] == 0):
            l[0] = daycount
        if (dist >= userdist) & (l[1] == 0):
            l[1] = daycount
        dpd = dpd * 1.10
        dist += dpd
        daycount += 1
    return l


userdpd4 = 20
userdist4 = 100

answer = running4(userdpd4, userdist4)
print("Ответ: a)", answer[0], "дней \n", "\tb)", answer[1], "дней")
