def print_params(*params): # *args **kwargs
    print(params)


print_params(1, 2, 3, 4, 5, 6, 7)

def print_params(a, b, c):
    print(a, b, c)

list_ = [1, 2]
dict_ = {'c': 3}
print_params(*list_, **dict_)


def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

dict_ = {'a': 1, 'b': 2, 'c': 3} #Имена ключей должны соответствовать именам параметров (за исключением **kwargs)
print_params(**dict_)
