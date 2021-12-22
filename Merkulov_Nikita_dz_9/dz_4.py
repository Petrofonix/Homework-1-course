from random import choice


class Car:
    direction = ['север', 'юг',
                 'восток', 'северо-восток', 'юго-восток',
                 'запад', 'северо-запад', 'юго-запад']

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f'Машина: {self.name};\nЦвет: {self.color};\nМашина полицейская?: {self.police}')

    def go(self):
        print(f'{self.name} едет.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self):
        print(f'{self.name} повернула на {choice(self.direction)}.')

    def show_speed(self):
        return f'Скорость {self.name} равна {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} равна {self.speed}.\nПревышена скорость.'
        else:
            return f'Скорость {self.name} равна {self.speed}.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} равна {self.speed}.\nПревышена скорость.'
        else:

            return f'Скорость {self.name} равна {self.speed}.'


class SportCar(Car):
    '''Nothing'''


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, police=True)


a = PoliceCar('Полицейская машина', 'Белая', 70)
b = WorkCar('Грузовик', 'синий', 40)
c = SportCar('Гоночный автомобиль', 'разнцветный', 200)
d = TownCar('Сидан', 'чёрный', 80)

list_ = [a, b, c, d]

for i in list_:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
