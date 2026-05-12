def mostrar_menu():
  print('''Bienvenido a la calculadora de matrices
1) Sumar Matrices
2) Multiplicar Matrices
3) Producto Hadamard
4) Producto Kronecker
5) Salir''')
  while True:
    try:
      opcion = int(input("\n¿Que quiere hacer?: "))
      if 1 <= opcion <= 5:
        return opcion
      else:
        print("Error: Ingrese una opcion valida")
    except ValueError:
      print("Error: Debe ingresar un numero")
