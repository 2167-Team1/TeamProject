# 1 - Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las 
# operaciones matematicas basicas (+,-,*,/)

class numComplejo:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2
    def restar(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2

