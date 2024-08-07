nums = [-3, -2, 0, 1, 9, -5]


def verdad_mentira(num_list):
    if not list(filter(lambda n: n >= 0, num_list)):
        return True
    else:
        return False


print(f"Todos los número son menores de 0: {verdad_mentira(nums)}")
