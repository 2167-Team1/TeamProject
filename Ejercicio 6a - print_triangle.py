number = int(input("ingrese el numero de filas de su triangulo "))

def print_triangle(number):
    for i in range(1, number + 1):
        print(str(i) * i)

print_triangle(number)
