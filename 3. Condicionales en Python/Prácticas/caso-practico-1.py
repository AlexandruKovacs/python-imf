import random

number = random.randrange(1, 20)

if len(str(number)) >= 2:
    print(f"El número aleatorio es {number} y tiene dos dígitos")
else:
    print(f"El número aleatorio es {number} y tiene un dígito")

