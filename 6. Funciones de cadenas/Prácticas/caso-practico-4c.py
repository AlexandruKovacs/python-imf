line = 'a: b: c: d: e: f:gh '
chars = [' ', ':']

letters = list(line)

for char in chars:

    count = line.count(char)

    while count:
        letters.remove(char)

        count -= 1

letters = ', '.join(letters)

print(f"El resultado es: {letters}")
