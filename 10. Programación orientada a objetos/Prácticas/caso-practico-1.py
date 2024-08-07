class Entidad:

    def __init__(self, number=0, director="", clients=""):
        self.number = number
        self.director = director
        self.clients = clients

    def __str__(self):
        print(f"El número de entidad es {self.number}, su director {self.director} y sus clientes son: {self.clients}")


entidades = []

file = open('people.txt')

for line in file:
    line_splits = line.strip().split(';')

    number = int(line_splits[0])
    director = line_splits[1]
    clients = line_splits[2]

    entidad = Entidad(number, director, clients)

    entidades.append(entidad.__str__())

