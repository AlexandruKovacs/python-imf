file = open('texts-2b.txt')

num_rows = num_words = num_chars = 0

for line in file:
    num_rows = num_rows + 1
    num_words = num_words + len(line.split())
    num_chars = num_chars + len(line)

print(f"El número de filas es: {num_rows}.")
print(f"El número de palabras es: {num_words}.")
print(f"El número de caracteres es: {num_chars}.")

file.close()
