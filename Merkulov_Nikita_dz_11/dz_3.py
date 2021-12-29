class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:
                print(f"Недопустимое значение - str и bool")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n.upper() == 'Y':
                    print(try_except.my_input())
                elif y_or_n.upper() == 'N':
                    return f'конец программы'
                else:
                    return f'конец программы'


try_except = Error(1)
print(try_except.my_input())
