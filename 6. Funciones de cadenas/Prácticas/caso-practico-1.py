line = 'a: b: c: d: e: f:gh '
result = ''

letters = line.split(':')
lettersCount = len(letters) - 1

for letter in letters:

    for idx, char in enumerate(letter):

        if char != '':
            newChar = char.strip()

            if idx == lettersCount:
                result += newChar
            else:
                result += newChar + ', '

print(','.join(x.strip() for x in line.split(':')))
