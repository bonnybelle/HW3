lst = list(input('Введите список: ').split(' '))
r = int(input('Введите шаг: '))
lst1 = list(lst)
r1 = -r

while r > 0 and r1 < 0:
    v = lst1.pop(-1)
    lst1.insert(0, v)
    lst.append(lst.pop(0))
    r -= 1
    r1 += 1
print('left shift', lst1, '\nright shift', lst)
