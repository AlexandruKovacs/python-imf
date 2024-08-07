from operator import itemgetter

countries = {
    'Argentina': 40000000,
    'Brasil': 190000000,
    'España': 46000000
}

# 1º forma
sorted_dictionary = sorted(countries.items(), key=itemgetter(1), reverse=True)

print(f'El páis con más habitantes es: {sorted_dictionary[0][0]}.')

# 2º forma
list = []

for value in countries.values():
    list.append(value)

print(f'El páis con más habitantes es: {max(list)}.')
