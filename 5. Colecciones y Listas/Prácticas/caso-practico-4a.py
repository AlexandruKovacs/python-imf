lst = ['SGE', 3.0, ['A', 'B'], 10, 'FINAL']

# a)
print(type(lst[2][1]))
# <class 'str'>

# b)
print(lst[2][1])
# B

# c)
print(lst[0:3:1])
# ['SGE', 3.0, ['A', 'B']]

# d)
print(lst[0:4])
# ['SGE', 3.0, ['A', 'B'], 10]

# d)
# print(lst[1][1])
# TypeError: 'float' object is not subscriptable

# e)
# lst[2][2] = 'Z'
# print(lst)
# IndexError: list assignment index out of range
