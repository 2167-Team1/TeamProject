def subcampeon (puntajes):
  lista = list(set(puntajes))
  lista.sort()
  return lista[len(lista)-2]