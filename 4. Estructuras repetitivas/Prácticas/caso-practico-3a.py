iterator = int(input(f"Introduce cuántos números quieres comprobar: "))

i = 1
accumulator = 0

while i <= iterator:
    number = int(input(f"Introduce el {i}º número: "))

    if number < 0:
        accumulator += 1

    i += 1

print(f"Ha introducido {accumulator} números negativos.")
