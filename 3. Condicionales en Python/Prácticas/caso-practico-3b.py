number = int(input("Introduce un número: "))

# Primera forma
if number % 2 == 0:
    print(f"El número {number} es par.")
else:
    print(f"El número {number} es impar.")

# Segunda forma
print(f"El número {number} es par." if number % 2 == 0 else f"El número {number} es impar.")
