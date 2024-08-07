people = ['Amy', 'Alice', 'Bobby', 'Charlie', 'Connie', 'David']
results = []


def start_with_c(words):
    for word in words:
        if word.lower().startswith('c'):
            results.append(word)
    return results


print(f"Las palabaras que empiezan por C son: {start_with_c(people)}")
