# 4. Сортировать список от меньшего к большему с помощью heapq
from heapq import nsmallest

lst = [int(i) for i in input('Введите список: ').split(' ')]
ordered = nsmallest(len(lst), lst)
print(ordered)


'''
# Второй метод гораздо длиннее, не знаю насчёт скорости:

from heapq import heappush, heappop

lst = [int(i) for i in input('Введите список: ').split(' ')]
new = []
li = []
for i in lst:
    heappush(new, i)
while len(new) > 0:
    li.append(heappop(new))
print(li)
'''
# -12 21 6789 -23 0 0 1 2 34 823 123 -123 -123 23 123 80124 0 1 2 3 4
