def matriz():
  while True:
    b = input("Ingrese las filas separadas por ';': ").split(";")
    matriz = []
    value = True
    try:
      for i in range(len(b)):
        c = b[i].split()
        if len(c) == 0:
          print("Error: debes digitar algun numero")
          value = False
          break
        else:
          a = list(map(float,c))
          matriz.append(a)
      if value == False:
        continue

      for j in range(len(matriz)):
        if len(matriz[j]) != len(matriz[0]):
          value = False
          break
      if value == True:
        return matriz
      else:
        print("Error: La cantidad de columnas debe ser igual para todas las filas")
    except ValueError:
      print("Error: Debes poner numeros")
