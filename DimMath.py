class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "," + str(self.y)

    def of(self, array):
        return array[self.x][self.y]

    def movepoint(self, vector):
        self.x += vector.distX
        self.y += vector.distY

    def asImaginary(self):
        return Imaginary(self.x, self.y)


class Vector:
    def __init__(self, xa, ya, yb, xb):
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.distX = xb - xa
        self.distY = yb - ya

    def __str__(self):
        return (
            str(Coordinate(self.xa, self.ya))
            + " -> "
            + str(Coordinate(self.xb, self.yb))
        )


class Imaginary:
    def __init__(self, Re, Im):
        self.Im = Im
        self.Re = Re

    def __str__(self):
        return str(Re) + "+" + str(Im) + "i"

    def __add__(self, sec):
        return Imaginary(self.Re + sec.Re, self.Im + sec.Im)

    def asPoint(self):
        return Coordinate(self.Re, self.Im)