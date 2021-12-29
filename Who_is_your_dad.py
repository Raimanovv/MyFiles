'''
Задача: Напишите программу «Кто твой папа?», в которой пользователь будет
вводить имя человека, а программа — называть отца этого человека. Чтобы было
интереснее, можно «научить» программу родственным отношениям среди литературных
персонажей, исторических лиц и современных знаменитостей. Предоставьте пользователю
возможность добавлять, заменять и удалять пары «СЫН — отец».
'''

dictionary = {
        'Саша': 'Петр',
        'Петр': 'Мустафа',
        'Герч': 'Зюбр'
}
choice = None
while choice != 0:
    print(
        '''
        1 - Показать кто отец
        2 - Добавить пару
        3 - Заменить пару
        4 - Удалить пару
        5 - Выйти из программы
        ''')
    choice = int(input('Выберите пункт: '))
    if choice == 1:
        son = input('Введите имя сына: ').capitalize()
        print('Его отец', dictionary.get(son, 'не найден в списке.\n\
Если хотите добавить, выберите пункт 2'))
        if son in dictionary:
            old_dad = dictionary[son]
            print('Дедушка сына', dictionary.get(old_dad, 'не найден'))
    if choice == 2:
        son = input('Введите имя сына: ').capitalize()
        dad = input('Введите имя отца: ').capitalize()
        if son in dictionary:
            print('Такое имя сына уже есть')
            continue
        dictionary[son] = dad
    if choice == 3:
        son = input('Введите имя сына: ').capitalize()
        dad = input('Введите новое имя отца: ').capitalize()
        if son not in dictionary:
            print('Такого имени сына нету')
            continue
        dictionary[son] = dad
    if choice == 4:
        son = input('Введке имя сына: ').capitalize()
        if son not in dictionary:
            print('Такого имени сына нету')
            continue
        del dictionary[son]
    if choice == 5:
        choice = 0
for i in dictionary:
    sonn = i
    dadd = dictionary[sonn]
    print('\n', sonn, '(сын)', '-', dadd, '(отец)')
