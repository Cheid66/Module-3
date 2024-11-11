# int() # целое число # --> int(input())
# float() # число с плавающей запятой #
# bool() # логические значения
# str() # строки
# list() # список
# tuple() # кортеж
# dict() # словарь
# set() # множество

# type = 1
# if type:
#     print('Ok')

salary =[2500, 3000.21655, 5000, 7500.56844, 1000.26866481]
print(round(sum(salary)/len(salary), 2), ' - Средняя зарплата в компании')
print(round(max(salary), 2), ' - Самая высокая зарплата в компании')
print(round(min(salary), 2), ' - Самая низкая зарплата в компании')

names = ['Степан', 'Гоша', 'Милана', 'Сергей', 'Сеня']
zipped = dict(zip(names, salary))
print(zipped['Степан'], ' - Зарплата Степана')
