class Stationery:
    def __init__(self, title='какой-нибудь рисунок'):
        self.title = title

    def draw(self):
        print(f'Начал рисовать {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title}')


class Marker(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title}')


a = Stationery()
b = Pen('линия')
c = Pencil('штрихи')
d = Marker('круги')

list_ = [a, b, c, d]

for i in list_:
    i.draw()