line = str(input("Introduce una frase: "))

vowels = ['a', 'e', 'i', 'o', 'u']

letters = list(line)

for letter in letters:

    if vowels.count(letter) > 0:
        print(f"La letra {letter} es vocal.")
    elif letter.isspace():
        print(f"El caracter '{letter}' es un espacio.")
    else:
        print(f"La letra {letter} es consonante.")
