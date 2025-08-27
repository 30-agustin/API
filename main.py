# API Numero


def trivia_fetch(num):
    
   # Recibe un número y devuelve un diccionario con curiosidades (trivia) sobre ese número.
   
    
    trivia = {
        "number": num,                # <- Se mantiene en inglés por los tests
        "el numero es par": num % 2 == 0,       # True si es par
        "el numero es impar": num % 2 != 0,     # True si es impar
        "El numero al cuadrado es igual a": num ** 2,         # El número al cuadrado
        "digitos": len(str(abs(num))) # Número de dígitos (ignora el signo)
    }

    # Trivia personalizada para algunos números
    if num == 42:
        trivia["dato curioso"] = "42 es 'la respuesta a la vida, el universo y todo lo demás' según Douglas Adams."
    elif num == 1000:
        trivia["dato curioso"] = "1000 en números romanos se escribe como M."
    elif num == 7:
        trivia["dato curioso"] = "El 7 es considerado un número de la suerte en muchas culturas."
    elif num == 13:
        trivia["dato curioso"] = "El 13 suele asociarse con la mala suerte, pero en Italia es de buena fortuna."
    else:
        trivia["dato curioso"] = f"El número {num} no tiene trivia especial, ¡pero sigue siendo interesante!"

    return trivia


def main():
    print("¡Hola estudiantes!")
    try:
        entrada = int(input("Ingresa un número: "))
        resultado = trivia_fetch(entrada)

        print("\n Trivia del número ingresado:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")


if __name__ == "__main__":
    main()
