def print_params(a, b, c):
    print(a, b, c)
    print(a + c)
print_params(2, True, 1) # Принимающая функция при вызове, должна содержать ровно столько параметров, сколько в описании


def print_params(a = 1, b = 2, c = 3):
    print(a, b, c)
print_params(2, 5, c = 'String') # Можно переопределять назначенные параметры
# Именованный параметр ('String') может идти только за позиционными
print_params(c = 'String', a = 2, b = True) # Можно сделать именованными все параметры, в разном порядке

def print_params(a, *, b, c):
    print(a, b, c)
print_params(1, b = 2, c = 6) # * обозначает именованными параметры, после себя
