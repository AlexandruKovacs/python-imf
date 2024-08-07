
my_dict = {
    'manzana': 4.50,
    'pera': 2.50,
    'uva': 1.25
}

print(f'Estado del diccionario: {my_dict}')

#a) Agregar un cuarto elemento.
my_dict['fresa'] = 3

print(f'Estado del diccionario: {my_dict}')

#b) Imprimir la cantidad de elementos del diccionario.
count = len(my_dict)

print(f'Cantidad de elementos del diccionario: {count}')

#c) Borrar un elemento del diccionario.
my_dict.pop('pera')

print(f'Estado del diccionario: {my_dict}')

#d) Imprimir todas las claves.
for (key, value) in my_dict.items():
    print(f'Clave del diccionario: {key}')

#e) Imprimir todos los valores.
for (key, value) in my_dict.items():
    print(f'Valor del diccionario: {value}')

#f) Imprimir claves y valores.
for (key, value) in my_dict.items():
    print(f'Clave-valor del diccionario: {key}-{value}')

#g) Borrar el diccionario.
my_dict.clear()

print(f'Estado del diccionario: {my_dict}')

del my_dict

print(f'Estado del diccionario: {my_dict}')
