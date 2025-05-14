
def suma_avanzada():
    entrada = input("Ingrese los números a sumar separados por espacio: ")
    try:
        numeros = [float(num) for num in entrada.split()]
        return sum(numeros)
    except ValueError:
        print("Todos los valores deben ser números.")
        return 0