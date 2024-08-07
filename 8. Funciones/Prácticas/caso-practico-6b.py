def sumar_mayores(x1, x2, x3):
    nums = []
    nums.extend([x1, x2, x3])

    sorted_xyz = sorted(nums)

    largest = sorted_xyz[-1]
    second_largest = sorted_xyz[-2]

    return largest + second_largest


print(f"La suma de los dos mayores es: {sumar_mayores(4, 5, 7)}")