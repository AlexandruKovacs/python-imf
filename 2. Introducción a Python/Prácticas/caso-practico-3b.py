def square(longitude):
    area = longitude * longitude
    perimeter = longitude * 4

    return f"El cuadrado con lados de {longitude}m de longitud tiene un área de {area}m2 y un perímetro de {perimeter}m"


print(square(5))
