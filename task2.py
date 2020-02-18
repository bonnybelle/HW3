# 2. Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLMNOPQRSTUVWXYZ” и w=4

s = str(input('Введите строку: '))
w = int(input('Ввелите длину: '))
j = w
zero = 0
lng = len(s)
while zero < lng:
    print(s[zero:w:])
    zero += j
    w += j
