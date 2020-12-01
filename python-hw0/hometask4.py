"""
Генерацию списков с помощью for,
которую мы изучили в прошлом файле
можно делать используя генераторы списков
Это те же самые for, но записанные короче.
Синтаксис генератора выглядит так:
new_l = [чем_заполнить for правила_фора]
Посмотрим пример переписывания
"""
l = []
for i in range(0, 25):
    l.append(i*5)
new_l = [i*5 for i in range(0, 25)]

"""
Списки вышли одинаковыми!
На первом месте стоит то, что раньше было в append
на втором не изменившийся for, который определяет как
будут меняться i
"""
"""
Или еще пример
"""

l = []
for i in range(3, 64, 5):
    l.append((i + 9) * 1.2)
new_l = [(i + 9) * 1.2 for i in range(3, 64, 5)]
"""
Списки вышли одинаковыми!
"""

"""
Переделывать можно и более простые создания списков
Так например список состоящий из восьми 1"""

l = []
for i in range(8):
    l.append(1)
new_l = [1 for i in range(8)]

"""
В таких случаях можно заметить что i
вовсе не используется и его можно заменить
на _ - это не переменная, это такая форма синтаксиса"""

l = []
for _ in range(8):
    l.append(1)
new_l = [1 for _ in range(8)]


"""
ТАк же можно переделывать и for на основе старых списков
"""

old_l = [3, 5, 1, 4, 6, 2, 2]
l = []
for i in old_l:
    l.append(i+12)

new_l = [i+12 for i in old_l]


##########################################
# TODO задание 1
##########################################
"""Переделать приведенный for"""
print("Результат задания 1 - списки должны совпасть!")
l = []
for i in range(3, 23, 2):
    l.append(i)

# здесь ваш код
new_l = []
new_l = [i for i in range(3, 23, 2)]

print(new_l)
print(l)
print(new_l == l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 2
##########################################
"""Переделать приведенный for"""
print("Результат задания 2 - списки должны совпасть!")
l = []
for i in range(12):
    l.append(2**i + 1)

# здесь ваш код
new_l = []
new_l = [2**i + 1 for i in range(12)]


print(new_l)
print(l)
print(new_l == l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 3
##########################################
"""Переделать приведенный for"""
print("Результат задания 3 - списки должны совпасть!")
old_l = [1, 3, 1, 3, 5, 2, 5, 6]
l = []
for i in old_l:
    l.append(i-16)

# здесь ваш код
new_l = []
new_l = [i-16 for i in old_l]

print(new_l)
print(l)
print(new_l == l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 4
##########################################
"""Переделать приведенный for"""
print("Результат задания 4 - списки должны совпасть!")
old_l = [1, 3, 1, 3, 5, 2, 5, 6]
l = []
for i in old_l:
    l.append(13)

# здесь ваш код
new_l = []
new_l = [13 for _ in old_l]

print(new_l)
print(l)
print(new_l == l)

##########################################
# конец задания
##########################################

"""
Переделывать в генератор списков из существующего for
проще, чем писать свои генераторы с нуля, но и это
тоже возможно, потренируемся
"""

##########################################
# TODO задание 5
##########################################
"""Напишите генератор, создающий список,
состоящих из 2оей"""
print("Результат задания 5")

# здесь ваш код
l = []
l = ['оей' for _ in range(2)]
print(l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 5
##########################################
"""Напишите генератор, создающий список,
состоящих из чисел кратных 5
[5,10,15,20,25,30]"""
print("Результат задания 5")

# здесь ваш код
l = []
l = [i*5 for i in range(1, 7)]
print(l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 6
##########################################
"""СОздайте список состоящий из степенй двойки"""
print("Результат задания 6")

# здесь ваш код
l = []
l = [2**i for i in range(5)]
print(l)

##########################################
# конец задания
##########################################