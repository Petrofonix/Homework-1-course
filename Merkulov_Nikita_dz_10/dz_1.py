

class Matrix:
    def __init__(self, list_):
        self.list_ = list_

    def __str__(self):
        for row in self.list_:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.list_)):
            for i_2 in range(len(other.list_[i])):
                self.list_[i][i_2] = self.list_[i][i_2] + other.list_[i][i_2]
        return Matrix.__str__(self)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
c = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
d = Matrix([[1, 2], [3, 4]])
print(d.__str__())
print(a.__str__())
print(c.__str__())
print(b.__str__())
print(a.__add__(c))
