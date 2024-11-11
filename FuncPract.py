# Максимум в списке
# Подсчет четных чисел в списке
# Уникальный список

def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

print(find_max([1, 82, 12, -5, 164, 15]))

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter +=1
    return counter

print(count_even([2, 8, 15, 13, 572, 957, 0]))

def unique(list_):
    newnique = []
    for i in list_:
        if i not in newnique:
            newnique.append(i)
    return newnique

print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
