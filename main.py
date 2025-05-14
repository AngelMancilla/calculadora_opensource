from modulos.sumar import sumar
from modulos.restar import restar
from modulos.multiplicacion import multiplicacion
from modulos.dividir import dividir
from modulos.suma_avanzada import suma_avanzada
import os

def pedir_numero():
    try:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Ingrese un numero valido")
        return pedir_numero()
    return numero1, numero2

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione Enter para continuar...")

def menu():
    while True:
        clear()
        print("-----Calculadora OpenSource-----")
        print("""
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Suma avanzada
        6. Salir
        """)
        try:
            opcion = int(input("Ingrese la opcion: "))
        except ValueError:
            print("Ingrese un numero valido")
            continue
        if opcion == 1:
            print("\nResultado:", sumar(*pedir_numero()))
            pausar()

        elif opcion == 2:
            print("\nResultado:", restar(*pedir_numero()))
            pausar()

        elif opcion == 3:
            print("\nResultado:", multiplicacion(*pedir_numero()))
            pausar()

        elif opcion == 4:
            print("\nResultado:", dividir(*pedir_numero()))
            pausar()

        elif opcion == 5:
            print("\nResultado:", suma_avanzada())
            pausar()

        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")


def main():
    menu()

if __name__ == "__main__":
    main()
