a = 5 # Глобальные имена
b = 10

def printer():
    global a, b
    a = 'Str' # Локальные имена
    b = 'Str 2'
    c = 15 # Локальные имена
    d = 20
    print(c, d, 'local')
    print(a, b, 'global')



print(a, b)
printer()
print(a, b)