my_dict = {'Roman': 1993, 'Pavel': 1989, 'Vitaliy': 1992, 'Diana': 1991}
print('Словарь: ', my_dict)
print('Существующее значение: ', my_dict['Roman'])
print('Отсутствуёщее значение: ', my_dict.get('Vladimir'))
my_dict.update({'Vladimir': 1966,
                'Lera': 2002})
print('Удалённое значение: ', my_dict.pop('Diana'))
print('Изменённый словарь: ', my_dict, '\n')

my_set ={1, 2, 2, 3.5, 5.7, 5.7, 'Roman', 'Roman', False, False}
print('Множество: ', my_set)
my_set.update([4, 7])
my_set.discard('Roman')
print('Изменённое множество: ', my_set)

