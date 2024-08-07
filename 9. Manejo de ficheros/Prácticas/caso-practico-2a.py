file = open('nums-2a.txt')
result = 0

for line in file:

    line_splits = line.strip().split(',')
    str_list = list(filter(None, line_splits))
    int_list = list(map(int, str_list))

    for line_split in int_list:

        if int(line_split) % 2 != 0:
            result = result + int(line_split)

print(f"La suma de todos los impares es: {result}.")

file.close()
