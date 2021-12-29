class DivisionByZero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_by_null(dividend, divider):
        try:
            return dividend / divider
        except ZeroDivisionError:
            return f'Деление на ноль недопустимо'


print(DivisionByZero.divide_by_null(1000000, 0))
print(DivisionByZero.divide_by_null(10, 10))
print(DivisionByZero.divide_by_null(0, 10))
