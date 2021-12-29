class ComplexNumbers:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b'

    def __add__(self, other):
        print(f'Сумма равна:')
        return f'z = {self.a + other.a} + {self.b + other.b} = {(self.a + other.a) + (self.b + other.b)}'

    def __mul__(self, other):
        print(f'Произведение равно:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} = ' \
               f'{(self.a * other.a - (self.b * other.b)) + self.b * other.a}'

    def __str__(self):
        return f'z = {self.a} + {self.b}'


z_1 = ComplexNumbers(10, -7)
z_2 = ComplexNumbers(4, 8)
print(z_1 + z_2)
print(z_1 * z_2)
