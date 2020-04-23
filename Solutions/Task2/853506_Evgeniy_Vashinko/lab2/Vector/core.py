import math


class Vector :

    def __init__(self, *args) :
        if len(args) == 0 :
            self.values = (0, 0)
        else :
            self.values = args

    def __add__(self, v) :
        return Vector(*tuple(a + b for a, b in zip(self.values, v.values)))

    def __sub__(self, v) :
        return Vector(*tuple(a - b for a, b in zip(self.values, v.values)))

    def __mul__(self, v) :
        if isinstance(v, Vector) :
            return Vector(*tuple(a * b for a, b in zip(self.values, v.values)))
        elif isinstance(v, int) or isinstance(v, float) :
            return Vector(*tuple(v * b for b in self.values))

    def __rmul__(self, v) :
        if isinstance(v, int) or isinstance(v, float) :
            return Vector(*tuple(v * b for b in self.values))

    def __pow__(self, v) :
        return Vector(*tuple(a ** v for a in self.values))

    def __eq__(self, v) :
        for a, b in zip(self.values, v.values) :
            if a != b :
                return False
        return True

    def __ne__(self, v) :
        for a, b in zip(self.values, v.values) :
            if a != b :
                return True
        return False

    def norm(self) :
        return math.sqrt(sum(a ** 2 for a in self.values))

    def __lt__(self, v) :
        return self.norm() < v.norm()

    def __gt__(self, v) :
        return self.norm() > v.norm()

    def __le__(self, v) :
        return self.norm() <= v.norm()

    def __ge__(self, v) :
        return self.norm() >= v.norm()

    def __getitem__(self, index) :
        if index >= len(self.values) :
            return -1
        return self.values[index]

    def __str__(self) :
        return str(self.values)
