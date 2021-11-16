# Los strings son inmutables, escribir una funcion que reciba un string, 
# un indice y una letra a modificar de ese string y que devuelve el string modificado.


def reemplazar_letra(cadena, indice, letra):
    if indice < len(cadena):
        cadena = cadena[0:indice-1] + letra + cadena[indice: len(cadena)]
    return cadena

