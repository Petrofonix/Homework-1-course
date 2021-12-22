class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def formula(self, weight=25, thickness=5):
        return f'{self.length} M * {self.width} M * {weight} кг * {thickness} см =' \
               f'{(self.length * self.width * weight * thickness) / 1000 } т'


a = Road(5000, 25)
print(a.formula())