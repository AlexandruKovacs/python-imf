for n in range(0, 26):
    if n % 2 != 0:
        print(f"El número impar es {n}.")


number = 1
result = ''

while number <= 25:
    if number % 2 != 0:
        result += '%i ' % number
    number += 1

print(result)
