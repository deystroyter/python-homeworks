print("""1. Нарисовать рамочку шириной w символов и
высотой h символов.""")


def drawing1(w, h):
    for i in range(0, h):
        if (i == 0) | (i == h - 1):
            print(w * "*")
        else:
            print("*" + (w - 2) * " " + "*")


drawing1(5, 4)
print("\n")


print("""2. Пускай символ, которым рисуется рамочка –
тоже входной параметр.""")


def drawing2(w, h, symbol):
    for i in range(0, h):
        if (i == 0) | (i == h - 1):
            print(w * symbol)
        else:
            print(symbol + (w - 2) * " " + symbol)


drawing2(5, 4, "o")
print("\n")


print("""3. Нарисовать рамочку шириной w символов и
высотой h символов, и толщиной f символов. (оформить в виде функции)""")


def drawing3(w, h, f):
    for _ in range(0, f):
        print(w * "*")
    for _ in range(0, h - f * 2):
        print(f * "*" + (w - 2 * f) * " " + f * "*")
    for _ in range(0, f):
        print(w * "*")


drawing3(7, 6, 2)
print("\n")
