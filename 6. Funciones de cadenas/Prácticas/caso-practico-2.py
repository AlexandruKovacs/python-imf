web = str(input('Introduce una página web: '))

domain = web.split(".", 1)

if domain[1]:
    print(f"El dominio de la página web es: {domain[1]}")
else:
    print(f"El dominio de la página web es: {web}")
