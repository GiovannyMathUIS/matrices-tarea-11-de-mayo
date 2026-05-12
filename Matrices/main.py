
import menu as me
import matriz as ma
import operaciones as op

def ejecutar():
    while True:
        opcion = me.mostrar_menu()

        if opcion == 5:
            print("\nGracias por usar la calculadora de matrices")
            print("Saliendo...")
            break

        print("\nIngrese los datos de la Matriz A:")
        A = ma.matriz()
        print("\nIngrese los datos de la Matriz B:")
        B = ma.matriz()

        try:
            if opcion == 1:
                print("Las matrices deben tener la misma dimension")
                op.suma(A, B)
            elif opcion == 2:
                print("La cantidad de columnas de la primera matriz deben ser la misma cantidad de filas en la segunda")
                op.multiplicacion(A, B)
            elif opcion == 3:
                print("Las matrices deben tener la misma dimension")
                op.p_h(A, B)
            elif opcion == 4:
                op.p_k(A, B)
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
