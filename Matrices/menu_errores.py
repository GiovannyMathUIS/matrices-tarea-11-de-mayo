print('''Bienvenido a la calculadora de matrices
1) Sumar Matrices
2) Multiplicar Matrices
3) Producto Hadamard
4) Producto Kronecker
5) Salir''')
while True:
  try:
    opcion = int(input("\n¿Que quiere hacer?: "))
    if opcion == 1:
      print("Las matrices deben tener la misma dimension")
      a = matriz()
      b = matriz()
      suma(a, b)
    elif opcion == 2:
      print("La cantidad de columnas de la primera matriz deben ser la misma cantidad de filas en la segunda")
      a = matriz()
      b = matriz()
      multiplicacion(a, b)
    elif opcion == 3:
      print("Las matrices deben tener la misma dimension")
      a = matriz()
      b = matriz()
      p_h(a, b)
    elif opcion == 4:
      a = matriz()
      b = matriz()
      p_k(a, b)
    elif opcion == 5:
      print("\nGracias por usar la calculadora de matrices")
      break
    else:
      print("Error: Ingrese una opcion valida")
  except ValueError:
    print("Error: Debe ingresar un numero")
