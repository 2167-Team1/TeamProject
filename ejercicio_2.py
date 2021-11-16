"""Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres."""

def may_x_min(texto):
    ppio= texto[0:100].swapcase()
    if len(texto)>100:
        ppio = ppio + texto[101:len(texto)]
    return ppio


