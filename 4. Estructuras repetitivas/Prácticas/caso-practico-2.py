start = 1
iterator = 5
accumulator = 0

while start <= iterator:
    number = float(input(f"Introduce el {start}º número: "))

    accumulator += number

    start += 1

media = accumulator / iterator

print(f"La media de los {iterator} números es: {media}")