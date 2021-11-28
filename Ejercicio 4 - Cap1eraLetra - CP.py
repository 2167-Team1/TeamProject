# Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula)

completo = input("Escriba nombre y apellido: ")

def capitalizarPrimeraLetra(completo):
    return completo.title()

print (capitalizarPrimeraLetra(completo))