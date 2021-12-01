

def thesaurus(*args):
    dict_names = {}
    for i in sorted(args):
        first_letter = i[0]
        if first_letter not in dict_names:
            dict_names[first_letter] = []
        if first_letter in dict_names:
            dict_names[first_letter].append(i)
    return dict_names


print(thesaurus('Иван', 'Мария', 'Михаил', 'Игорь', 'Петр', 'Илья'))
