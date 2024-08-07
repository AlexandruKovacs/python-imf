from math import sqrt

nums = [9, 36, 81]


def cuadrado(num_list):
    return list(map(lambda x: sqrt(x), num_list))


print(f"Las raíces cuadradas son: {cuadrado(nums)}")
