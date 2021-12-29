site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац',
            'div': 'Тут, наверное, какой-то блок'
        }
    }
}

def search(name, listt):
    if name in listt:
        return listt[name]

    for i in listt.values():
        if isinstance(i, dict):
            result = search(name, i)
            if result:
                break
    else:
        result = None
    return result


vv = search((input('Введите словo поиска: ')), site)
if vv:
    print(vv)
else:
    print('Такого значения нету!')