class Person:

    def __init__(self, name, dni, address, phone):
        self.name = name
        self.dni = dni
        self.address = address
        self.phone = phone

    def getName(self):
        return self.name

    def getDni(self):
        return self.dni

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def __str__(self):
        return f"El nombre de la persona es {self.name}, su DNI es {self.dni}, su dirección es {self.address}, su teléfono es {self.phone}"


class Student(Person):

    def __init__(self, name, dni, address, phone, mark):
        super().__init__(name, dni, address, phone)
        self.mark = mark

    def getMark(self):
        print(self.mark)

    def __str__(self):
        return f"{super().__str__()}, y su nota es {self.mark}."


num_person = 2
i = 1
persons = []

while i <= num_person:

    name = str(input(f"Introduce el nombre de la {i}º persona: "))
    dni = str(input(f"Introduce el DNI de la {i}º persona: "))
    address = str(input(f"Introduce la dirección de la {i}º persona: "))
    phone = str(input(f"Introduce el teléfono de la {i}º persona: "))
    mark = str(input(f"Introduce la nota de la {i}º persona: "))

    student_obj = Student(name, dni, address, phone, mark)
    persons.append(student_obj)

    print(student_obj)

    i = i + 1
