print("""\n1. Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...""")


# Следующий член последовательности равен сумме 2-ух предыдущих

def find_element1(n):
    prev = cur = 1
    for n in range(int(n - 2)):
        tmp = prev + cur
        prev = cur
        cur = tmp

    return cur


usern1 = 7
print(usern1, "-й член последовательности - ", find_element1(usern1))

print("""\n2. Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…""")


# Следующий член последовательности равен сумме 3-ёх предыдущих

def find_element2(n):
    prev0 = prev1 = cur = 1
    for n in range(int(n - 3)):
        tmp = cur + prev1 + prev0
        prev0 = prev1
        prev1 = cur
        cur = tmp

    return cur


usern2 = 8
print(usern2, "-й член последовательности - ", find_element2(usern2))

print("""\n3. Вывести квадраты нечетных чисел до N. (генератором списков)""")


def kvadrat_nechet3(n):
    answ = [i ** 2 for i in range(1, n + 1, 2)]
    return answ


usern3 = 10
print(kvadrat_nechet3(usern3))

print("""\n4. Вычислить сумму и произведение всех натуральных чисел от А до В
включительно.""")


def sum_and_multiply4(a, b):
    sum = 0
    multiply = 1
    for i in range(a, b + 1, 1):
        sum += i
        multiply *= i
    return sum, multiply


usera4 = 8
userb4 = 15
ans = sum_and_multiply4(usera4, userb4)
print("От", usera4, "до", userb4)
print("Сумма =", ans[0])
print("Произведение =", ans[1])


print("""\n5. Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые
между ними, потом все нечётные (генератором/ами списков)""")


def chet_nechet5(a, b):
    if a % 2 == 0:
        nechet = [i for i in range(a + 1, b + 1, 2)]
        chet = [i for i in range(a, b + 1, 2)]
    else:
        nechet = [i for i in range(a, b + 1, 2)]
        chet = [i for i in range(a + 1, b + 1, 2)]
    return nechet, chet


usera5 = 4
userb5 = 19
ans = chet_nechet5(usera5, userb5)
print("От", usera5, "До", userb5)
print("Нечётные -", ans[0])
print("Чётные -", ans[1])


print("""\n6. Исходный список содержит положительные и отрицательные числа. Требуется
положительные поместить в один список, а отрицательные - в другой
(генератором/ами списков)""")

def plus_minus6(arr):

    plus = [i for i in arr if i >= 0]
    minus = [i for i in arr if i < 0]

    return plus, minus


array = [10, -11, 24, 21, 12, -2, 2, -439, 22]
ans = plus_minus6(array)
print("Исходный массив", array)
print("Положительные +", ans[0])
print("Отрицательные -", ans[1])
