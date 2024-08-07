from decimal import Decimal

with open('marks-1a.txt', 'r+') as file:

    lines = file.readlines()
    file.truncate(0)

    for line in lines:

        line = line.strip()
        marks = line.split(':')
        avg = Decimal(0)
        count = 0

        for index in range(1, len(marks)):
            mark = marks[index].strip()

            if mark:
                avg += Decimal(mark)
                count += 1

        if count > 0:
            avg /= count

        if avg >= 4.0:
            marks.append('APROABDO\n')

        if avg < 4.0:
            marks.append('REPROBADO\n')

        for mark in marks:
            file.write(f"{mark}:")
