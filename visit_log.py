# Надо из списка сделать уникальный список (чтобы элементы (словари) не повторялись)
data = [
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'},
    {'id': 12, 'user': 'Anton'},
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'}
]

# 1-ый вариант
listt = []
for i in data:
    flag = False
    for ii in listt:
        if ii['id'] == i['id']:
            flag = True
            break
    if not flag:
        listt.append(i)
print(listt)

# 2-ой вариант
ff = {i['id']: i for i in data}
print(ff.values())
