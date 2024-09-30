def funkc_with_params(a, b = 2, c = 3): # Значение по умолчанию присваивается всегда после переменных!!!
    print(a + b + c)


funkc_with_params(3, 3)
funkc_with_params(3)
funkc_with_params(3)
funkc_with_params(3)

def funkc_with_params(a, b = 2, c = []):
    c.append(a)
    print(c)

funkc_with_params(3)
funkc_with_params(3)
funkc_with_params(3)
funkc_with_params(3)

def funkc_with_params(a, b = 2, c = None):
    if c is None:
        c = []
        c.append(a)
    print(c)

funkc_with_params(5)
funkc_with_params(3)
funkc_with_params(9)
funkc_with_params(7)