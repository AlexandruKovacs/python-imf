file = open('marks-1b.txt')

for line in file:

    line_split = line.strip().split(':')
    name = line_split[0]

    marks = map(float, line_split[1:])
    avg = sum(marks) / len(marks)

    if avg:
        print(f"{name}: REPROBADO")
    else:
        print(f"{name}: APROBADO")
