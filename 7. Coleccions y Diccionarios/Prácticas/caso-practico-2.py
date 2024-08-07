i = int(input(f'Introduce cuántas listas vas a escribir: '))
lists = []

if i > 0:

    list_num = 1

    while list_num <= i:

        tmp = []
        word_num = 1

        while word_num <= list_num:

            word = str(input(f'Introduce la {word_num}º palabra para la lista {list_num}: ').lower())
            tmp.append(word)
            word_num += 1

        lists.append(tmp)
        list_num += 1
else:
    print(f'¡Imposible!')
