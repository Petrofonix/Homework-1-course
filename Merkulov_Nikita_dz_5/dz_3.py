tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

together = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))

print(*together, sep='\n')
print(f'Доказательство того, что генератор истощён: {list(together)}')
