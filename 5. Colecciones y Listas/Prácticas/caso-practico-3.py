numbers = [3, 23, 56, 123, 55, 44, 122, 56, 78, 86]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(f"La lista original es: {numbers}")
print(f"Los números pares son: {evens}")
