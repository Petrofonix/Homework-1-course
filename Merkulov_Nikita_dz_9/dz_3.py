class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self.income.values())}'


a = Position('Никита', 'Меркулов', 'Студент', 1000, 200)
print(a.position)
print(a.get_full_name())
print(a.get_full_profit())
