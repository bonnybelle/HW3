# 1. Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг. Нужно решение с deque и без него.
# Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4].
from collections import deque

d = deque(input('Введите список: ').split(' '))
r = int(input('Введите шаг: '))
d1 = deque(d)
r1 = -r
d.rotate(r)
d1.rotate(r1)
print('left shift', d, '\nright shift', d1)
