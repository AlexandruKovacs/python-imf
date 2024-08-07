cities = ['Almería', 'Madrid', 'Barcelona', 'Mérida', 'Murcia', 'Guadalajara', 'Marbella', 'Málaga', 'Vigo', 'Cuenca']
result = []

for city in cities:
    if city.lower().startswith('m'):
        result.append(city)

print(f"Las ciudades que empiezan por la letra M son: {result}")
