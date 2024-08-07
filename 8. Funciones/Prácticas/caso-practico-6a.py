word = str(input(f"Introduce una palabra: "))
i = int(input(f"Introduce las veces que quieres que se repita: "))


def repeat_word(word, i):
    while i > 0:
        print(word)
        i = i - 1


print(f"Las palabra repetida es: {word}")

repeat_word(word, int(i))
