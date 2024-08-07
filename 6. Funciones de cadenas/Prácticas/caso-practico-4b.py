sentence = '0000000000000000 es un ejemplo de string con zeros ¡!! 00000000'
char = '0'

count = sentence.count(char)
chars = list(sentence)

while count:
    chars.remove(char)

    count -= 1

chars = ''.join(chars)

# Otra forma
# sentence.strip('0')

print(f"El resultado sin el caracter {char} es: {chars}")
