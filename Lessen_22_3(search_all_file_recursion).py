import os

def scr(name, way):
    ee = list()
    for i in os.listdir(way):
        wayy = os.path.join(way, i)
        if name == i:
            ee.append(os.path.join(way, name))
        if os.path.isdir(wayy):
            ff = scr(name, wayy)
            if ff:
                for uu in ff:
                    ee.append(uu)

    return ee

tt = scr('Новый текстовый документ.txt', os.path.abspath(os.path.join('..', 'task')))
print(tt)

for ii in tt:
    file1 = open(ii, 'w')
    file.write('Gh HHH ПРИВЕТ ТВМСТnv klcd влсмтымлтд')
    file.close()

for ii in tt:
    print('\n', ii)
    file = open(ii, 'r')
    data = file.read()
    print(data)
    file.close()
