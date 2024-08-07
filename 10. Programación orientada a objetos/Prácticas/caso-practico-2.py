class Dog:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def __str__(self):
        print(f"El nombre del perro es {self.name} y su peso es {self.weight}")


dogs = []

file = open('dogs.txt')

for line in file:

    line_splits = line.strip().split(';')

    name = line_splits[0]
    weight = int(line_splits[1])

    dog_obj = Dog(name, weight)
    dogs.append(dog_obj)


dogs.sort(key=lambda dog: dog.weight, reverse=True)

print(f"El perro más pesado se llama {dogs[0].getName()} y tiene un peso de {dogs[0].getWeight()} kg.")



