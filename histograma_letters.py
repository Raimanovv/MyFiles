def histogram(text):
	dictt = dict()
	for i in text:
		if i in dictt:
			dictt[i] += 1
		else:
			dictt[i] = 1
	return(dictt)

text = input('Введите текст:').lower()
histo = histogram(text)
print(histo)

for i in sorted(histo.keys()):
	print(i, '=', histo[i])

print('Максимальная частота:', max(histo.values()))
