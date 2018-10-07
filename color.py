import numbers

# Module that implements RGBA colors, for easy additiona and scaling


class Color(object):
    def __init__(self, *args):
        self.r, self.g, self.b, self.a = [0]*4
        if len(args) == 1:
            if len(args[0]) == 3:
                self.r, self.g, self.b = args[0]
            elif len(args[0]) == 4:
                self.r, self.g, self.b, self.a = args[0]
            else:
                raise ValueError("Incorrect sequence length!")
        elif len(args) == 3:
            self.r, self.g, self.b = args
        elif len(args) == 4:
            self.r, self.g, self.b, self.a = args
        else:
            raise ValueError("Incorrect sequence length!")
        self.__bound()

    def __bound(self):
        self.r = int(max(0, min(255, self.r)))
        self.g = int(max(0, min(255, self.g)))
        self.b = int(max(0, min(255, self.b)))
        self.a = int(max(0, min(255, self.a)))

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a)

        elif isinstance(other, numbers.Real):
            return Color(self.r + other, self.g + other, self.b + other, self.a + other)

    def __sub__(self, other):
        if isinstance(other, Color):
            return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.a - other.a)

        elif isinstance(other, numbers.Real):
            return Color(self.r - other, self.g - other, self.b - other, self.a - other)

    def __mul__(self, other):
        return Color(self.r * other, self.g * other, self.b * other, self.a * other)

    def __iter__(self):
        return ColorIterator(self)

    def multuple(self, l):
        return (int(self.r*l), int(self.g*l), int(self.b*l), int(self.a*l))


class ColorIterator(object):
    def __init__(self, c):
        self.l = [c.r, c.g, c.b, c.a]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 4:
            raise StopIteration
        self.i += 1
        return self.l[self.i-1]


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
ORANGE = Color(255, 128, 0)
