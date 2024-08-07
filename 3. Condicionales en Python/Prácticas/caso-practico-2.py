current_year = int(input("Introduce el año actual: "))
random_year = int(input("Introduce un año aleatorio: "))

if current_year > random_year:
    print(f"Desde el año {random_year} han pasado {current_year - random_year} años.")

if current_year < random_year:
    print(f"Para llegar al año {random_year} faltan {random_year - current_year} años.")

if current_year == random_year:
    print("Son el mismo año.")
