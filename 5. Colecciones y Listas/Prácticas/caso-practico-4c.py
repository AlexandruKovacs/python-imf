lst = [66.25, 333, 333, 1, 1234.5]

# a) Cuántas veces se repite 333 y 66.25 y 'x'
print(lst.count(333))
print(lst.count(66.25))
print(lst.count('x'))

# b) Insertar en la posición 2 un -1
lst.insert(2, -1)
print(lst)

# c)
lst.append(333)
print(lst)

# d)
lst.sort()
print(lst)