def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [True, 15, 'пончик']
print_params(*values_list)


values_dict = {'a': 16, 'b': False, 'c': 'Игорь'}
print_params(**values_dict)


values_list_2 = ['pelmen', False]
print_params(*values_list_2, 159753)