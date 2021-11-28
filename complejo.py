class Complejo(numero):
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f'{self.r}, {self.i}i'

    def __suma__(self, otro):
        return Complejo(self.r + otro.r, self.i + otro.i)

    def __resta__(self, otro):
        return Complejo(self.a - otro.a, self.i - otro.i)

    def __producto__(self, otro):
        return Complejo((self.r * otro.r) - (self.i * otro.i),
            (self.i * otro.r) + (self.r * otro.i))

    def __cociente_(self, otro):
        r = (otro.r**2 + otro.i**2)
        return Complejo((self.r*otro.r - self.i*otro.i)/r,
            (self.i*otro.r + self.r*otro.i)/r)


