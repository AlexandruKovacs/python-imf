sentence = 'blah, lots, of, spaces, here'

clean = []

words = sentence.split(',')

for word in words:
    clean.append(word.strip())

print(f"EL número de palabras es: {len(clean)}")
