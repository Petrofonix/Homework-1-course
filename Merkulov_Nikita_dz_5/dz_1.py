

def odd_nums(n):
    for n in range(1, n + 1, 2):
        yield n


for i in odd_nums(int(input('Введите число: '))):
    print(i)
