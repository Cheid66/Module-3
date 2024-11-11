a = [True, False, False]
print(any(a)) # если есть хотя бы 1 значение True, выводит True, нет - False

a = [1, 0, 0]
print(any(a))

b = '0' # В строке определяется наличие значения - True
print(any(b))

a = [1, 1, 0]
print(all(a)) # если все значения True - True, нет - False
 # Интроспекция - способность какого либо объекта получить информацию об атрибутах и методах,
 # в процессе выполнения программы
a = [1, 1, 0]
b = ''
print(dir(b)) # Показывает доступные методы
print(type(a)) # показывает тип данных

a = [1, 0, 0]
print(isinstance(a, str)) # сравнивает значение с шаблоном
print(type(a) == list) # то же самое

a = [1, 1, 1]
d = [1, 1, 1]
c = d
print(id(a)) # Id объекта (уникальный номер)
print(id(d))
print(id(c)) # изменение "c" будет влиять на "d"
print(a == d)
print(a is d) # равен, но не является
print(id(5)) # id есть у каждого значения
print(c is d)
print(help(a))
print(help(print))

def helper(): # строка документирования
    """
    Эта функция - помощник
    """
    pass

print(help(helper))
print(helper.__doc__)
