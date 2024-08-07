word = str(input("Introduce una palabra: "))

vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word:
    if letter in vowels:
        print(f"La letra {letter} es una vocal.")
    elif letter == ' ':
        print("Es un espacio.")
    else:
        print(f"La letra {letter} es una consonante.")
