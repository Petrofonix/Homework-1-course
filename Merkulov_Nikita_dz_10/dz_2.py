from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, something):
        self.something = something

    @abstractmethod
    def abstract(self):
        return ''


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто необходимо: {self.something / 6.5 + 0.5: .2f} ткани'

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма необходимо: {2 * self.something + 0.3: .2f} ткани'

    def abstract(self):
        pass


a = Coat(40)
b = Costume(55)
print(a.consumption())
print(b.consumption())
