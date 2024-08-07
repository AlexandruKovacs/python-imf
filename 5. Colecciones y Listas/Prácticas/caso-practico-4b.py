lst = ['A', 'B', 'C', 1, 2, ['LUNES', 'MARTES']]

# a) Añadir la letra z
new_lst = lst.copy()
new_lst.append('Z')
print(new_lst)

# b) Indicar la longitud de la lista
print(len(lst))

# c)
print(lst[::4])
# ['A', 2]

# d)
print(lst[0:3:2])
# ['A', 'C']

# e)
print(lst[-1][0])
# LUNES

# f)
print(lst[2::1])
# ['C', 1, 2, ['LUNES', 'MARTES']]
