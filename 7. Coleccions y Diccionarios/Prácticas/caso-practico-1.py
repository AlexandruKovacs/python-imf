from operator import itemgetter

dictionary = {}
i = 0

while i < 3:
    word = str(input(f'Introduce la {i + 1}º palabra: ').lower())

    if word in dictionary:
        print(f'La palabra {word} ya está en diccionario. Prueba con otra.')
    else:
        dictionary[word] = len(word)
        i = i + 1

sorted_dictionary = sorted(dictionary.items(), key=itemgetter(1), reverse=True)

print(f'La palabra más larga es: {sorted_dictionary[0][0]}.')
