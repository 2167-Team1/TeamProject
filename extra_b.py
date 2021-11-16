# b- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) y 
# devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. 
# Ejemplo. "Codo a Codo" 
# Debe imprimir: 
# o 4 
# c 2 
# d 2

def caracter_mas_usado(cadena):
    cadena_lista= list(cadena.lower().replace(" ","")) #para elimanr los espacios vacios y dejar el texto en minúscula
    dicc_letras = {}
    rango = 3

    for i in range(len(cadena_lista)):
        #se genera un diccionario de las letras involucradas (únicas) y su cantidad
        dicc_letras[cadena_lista[i]] = cadena_lista.count(cadena_lista[i])

    if len(dicc_letras)<3:
        #en caso de que la cantidad de letras sea menor a las 3 requeridas
        rango = len(dicc_letras)

    for i in range(rango):
        #imprime el mayor para luego quitarlo del diccionariom, de esa forma siempre quitará los mayores
        print(max(dicc_letras, key=dicc_letras.get), ":",max(dicc_letras.values()))
        del(dicc_letras[max(dicc_letras, key=dicc_letras.get)])


