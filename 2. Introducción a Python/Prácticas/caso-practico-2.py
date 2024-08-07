
number = int(input("Introduce un número: "))

quotient = number // 2
rest = number % 2

# divmod devuelve el resultado en formato (x, y)
result = divmod(number, 2)

print(f"El cociente y el resto del número {number} son {quotient} y {rest} respectivamente.")