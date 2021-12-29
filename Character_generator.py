'''
Задача: Напишите программу «Генератор персонажей» для ролевой игры. 
Пользователю должно быть предоставлено 30 пунктов, которые можно распределить 
между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего 
«пула», но и возвращать их туда из характеристик, которым он решит присвоить 
другие значения.
'''

specifications = [0, 0, 0, 0]
summ = 30
summm = 30
choice = None
print('''
    Начальная характеристика:
    сила : 0
    здоровье : 0 
    мудрость : 0
    ловкость : 0
    '''
    )
while choice != '0':
    print(
    '''
    Добавить в характеристику параметр - 1
    Убрать из характеристики параметр  - 2
    Выйти из программы                 - 0
    '''
    )
    choice = input('Ваш выбор? - ')
    if choice == '0':
        print('\nДо свидания.')
    if choice == "1":
        skill = input('Куда внести значения? - ')
        amount = input('Сколько внести пунктов? - ')
        if amount == '':
            print('\nВы не написали число!')
            continue
        summm -= int(amount)
        if summm >= 0:
            summ -= int(amount)
            amount = int(amount)
            if skill == 'сила':
                specifications[0] += amount
                print('сила: +', amount)
            elif skill == 'здоровье':
                specifications[1] += amount
                print('здоровье: +', amount)
            elif skill == 'мудрость':
                specifications[2] += amount
                print('мудрость: +', amount)
            elif skill == 'ловкость':
                specifications[3] += amount
                print('ловкость: +', amount)
        else:
            print('У вас осталось всего лишь', summ, 'очков')
    if choice =='2':
        skill = input('Откуда забрать значения? - ')
        amount = input('Сколько забрать пунктов? - ')
        if amount == '':
            print('\nВы не написали число!')
            continue
        amount = int(amount)
        if skill == 'сила' and specifications[0] - amount >= 0:
            specifications[0] -= amount
            summ += int(amount)
            print('сила: -', amount)
        elif skill == 'здоровье' and specifications[1] - amount >= 0:
            specifications[1] -= amount
            summ += int(amount)
            print('здоровье: +', amount)
        elif skill == 'мудрость' and specifications[2] - amount >= 0:
            specifications[2] -= amount
            summ += int(amount)
            print('мудрость: +', amount)
        elif skill == 'ловкость' and specifications[3] - amount >= 0:
            specifications[3] -= amount
            summ += int(amount)
            print('ловкость: +', amount)
        else:
            print('У вас нету столько очков сколько вы хотите \
                   забрать с этой характеристики')
print('\nсила : {specificationss[0]}\nздоровье : {specificationss[1]}\nмудрость : {specificationss[2]}\nловкость : {specificationss[3]}'.format(specificationss=specifications))
